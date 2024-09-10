
# Promptsy

Promptsy is a Python library designed for managing and organizing prompts for language models in a structured way. It provides a convenient method to store, retrieve, and format prompts using YAML files.

## Features

- Save prompts to YAML files with a specified name and directory structure
- Load prompts from YAML files by name
- Format prompts with dynamic values using keyword arguments
- Automatically create directories for prompts if they don't exist
- List all available prompts in the specified base directory
- Colorized error messages for better visibility
- Enhance prompts using OpenAI's language model

## Installation

To install Promptsy, you can use pip:

```bash
pip install promptsy
```

## Configuration

Before using the `PromptEnhancer`, you need to set up your OpenAI API key. You can do this by setting the `OPENAI_API_KEY` environment variable. Here’s how to set it:

### On Windows

```bash
set OPENAI_API_KEY=your_api_key_here
```

### On macOS/Linux

```bash
export OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

Here's a basic example of how to use Promptsy:

```python
from promptsy.prompt import Prompt
from promptsy.prompt_manager import PromptManager

# Create an instance of PromptManager
manager = PromptManager()

# Create an instance of Prompt
prompt = Prompt(
    name="hello_world",
    description="An example prompt",
    template="Hello, {name}!"
)

# Save the prompt using the PromptManager
prompt.save(manager)

# Load the prompt using the PromptManager
loaded_prompt = Prompt.load(manager, "hello_world")

print(loaded_prompt)  # Output: hello_world: An example prompt
print(loaded_prompt.format(name="Taylor Swift"))  # Output: Hello, Taylor Swift!
```

## Prompt Manager

The `PromptManager` class is responsible for managing the storage and retrieval of prompts. It provides methods for saving prompts to YAML files, loading prompts from YAML files, and listing all available prompts.

### Initialization

```python
manager = PromptManager(base_directory='prompts')
```

- `base_directory` (optional): The base directory where the prompts will be stored. Defaults to `'prompts'`.

### Saving a Prompt

```python
manager.save(prompt, name)
```

- `prompt` (dict): The prompt data to be saved.
- `name` (str): The name of the prompt.

### Loading a Prompt

```python
loaded_prompt = manager.load(name)
```

- `name` (str): The name of the prompt to load.
- Returns: The loaded prompt data.

### Listing Prompts

```python
prompts = manager.list_prompts()
```

- Returns: A list of prompt names.

## Prompt Enhancer

The `PromptEnhancer` class allows you to enhance prompts using OpenAI's language model. It generates improved versions of prompts based on the original template.

### Initialization

```python
enhancer = PromptEnhancer(api_key='your_api_key_here')
```

- `api_key` (str, optional): OpenAI API key. If None, it tries to retrieve from the environment variable.
- `model_name` (str, optional): The name of the model to be used (default: "gpt-4o-mini").

### Enhancing a Prompt

```python
enhanced_prompt = enhancer.enhance_prompt(prompt)
```

- `prompt` (Prompt): A Prompt object containing the original prompt template.
- Returns: A new Prompt object with the enhanced template.

### Example Usage of Prompt Enhancer

Here’s an example of how to use the `PromptEnhancer` with the `prompt_toddlers_story_time`:

```python
from promptsy.prompt import Prompt
from promptsy.prompt_manager import PromptManager
from promptsy.prompt_enhancer import PromptEnhancer

# Create an instance of PromptManager
manager = PromptManager()

# Create an instance of Prompt for toddlers story time
prompt_toddlers_story_time = Prompt(
    name="toddlers_story_time",
    description="Write a bedtime story for toddlers",
    template="You are a bedtime story teller for toddlers. Write a story for a toddler about a {animal} that goes on an adventure to {place}."
)

# Save the original prompt
prompt_toddlers_story_time.save(manager)

# Create an instance of PromptEnhancer
enhancer = PromptEnhancer()

# Enhance the prompt
enhanced_prompt = enhancer.enhance_prompt(prompt_toddlers_story_time)

print("Enhanced Prompt:")
print(enhanced_prompt.template)
```

### Saving Enhanced Prompts

The enhanced prompts are automatically saved in the `enhanced_prompts` directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/feliperafael/promptsy).

## License

This project is licensed under the [MIT License](LICENSE).
