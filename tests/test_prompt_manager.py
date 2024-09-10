import os
import pytest
from promptsy.prompt_manager import PromptManager

@pytest.fixture
def prompt_manager():
    return PromptManager(base_directory='test_prompts')

def test_prompt_manager_initialization(prompt_manager):
    assert prompt_manager.base_directory == 'test_prompts'
    assert os.path.exists('test_prompts')

def test_get_file_path(prompt_manager):
    file_path = prompt_manager._get_file_path('custom_prompt')
    assert file_path == os.path.join('test_prompts', 'custom', 'custom_prompt.yaml')

    file_path = prompt_manager._get_file_path('examples.hello_world')
    assert file_path == os.path.join('test_prompts', 'examples', 'hello_world.yaml')

def test_save_prompt(prompt_manager):
    prompt_manager.save({'text': 'Hello, {name}!'}, 'custom_prompt')
    file_path = os.path.join('test_prompts', 'custom', 'custom_prompt.yaml')
    assert os.path.exists(file_path)

    with open(file_path, 'r') as file:
        content = file.read()
        assert 'text: Hello, {name}!' in content

def test_load_prompt(prompt_manager):
    prompt_manager.save({'text': 'Hello, {name}!'}, 'custom_prompt')
    loaded_prompt = prompt_manager.load('custom_prompt')
    assert loaded_prompt == {'text': 'Hello, {name}!'}

def test_load_non_existent_prompt(prompt_manager):
    with pytest.raises(FileNotFoundError):
        prompt_manager.load('non_existent_prompt')

def test_list_prompts(prompt_manager):
    prompt_manager.save({'text': 'Hello, {name}!'}, 'examples.hello_world')
    prompt_manager.save({'text': 'Goodbye, {name}!'}, 'examples.goodbye')
    prompt_manager.save({'text': 'Custom prompt'}, 'custom_prompt')

    prompts = prompt_manager.list_prompts()
    assert 'examples.hello_world' in prompts
    assert 'examples.goodbye' in prompts
    assert 'custom.custom_prompt' in prompts
