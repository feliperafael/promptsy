import pytest
from promptsy.prompt import Prompt
from unittest import mock

def test_prompt_initialization():
    prompt = Prompt(
        name="test_prompt",
        description="A test prompt",
        template="Hello, {name}!"
    )
    assert prompt.name == "test_prompt"
    assert prompt.description == "A test prompt"
    assert prompt.template == "Hello, {name}!"

def test_prompt_format():
    prompt = Prompt(
        name="test_prompt",
        description="A test prompt",
        template="Hello, {name}!"
    )
    formatted_prompt = prompt.format(name="John")
    assert formatted_prompt == "Hello, John!"

def test_prompt_str_representation():
    prompt = Prompt(
        name="test_prompt",
        description="A test prompt",
        template="Hello, {name}!"
    )
    assert str(prompt) == "test_prompt: A test prompt"

def test_prompt_to_dict():
    prompt = Prompt(
        name="test_prompt",
        description="A test prompt",
        template="Hello, {name}!"
    )
    prompt_dict = prompt.to_dict()
    assert prompt_dict == {
        'name': 'test_prompt',
        'description': 'A test prompt',
        'template': 'Hello, {name}!'
    }

def test_prompt_from_dict():
    prompt_dict = {
        'name': 'test_prompt',
        'description': 'A test prompt',
        'template': 'Hello, {name}!'
    }
    prompt = Prompt.from_dict(prompt_dict)
    assert prompt.name == "test_prompt"
    assert prompt.description == "A test prompt"
    assert prompt.template == "Hello, {name}!"

def test_prompt_save_and_load():
    manager_mock = mock.Mock()
    prompt = Prompt(
        name="test_prompt",
        description="A test prompt",
        template="Hello, {name}!"
    )
    prompt.save(manager_mock)
    manager_mock.save.assert_called_once_with(prompt.to_dict(), prompt.name)

    manager_mock.load.return_value = prompt.to_dict()
    loaded_prompt = Prompt.load(manager_mock, "test_prompt")
    assert loaded_prompt.name == prompt.name
    assert loaded_prompt.description == prompt.description
    assert loaded_prompt.template == prompt.template
