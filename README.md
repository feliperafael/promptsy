# Promptsy

Promptsy is a Python library designed for managing and organizing prompts for language models in a structured way. It provides a convenient method to store, retrieve, and format prompts using YAML files.

## Features

- Save prompts to YAML files with a specified name and directory structure
- Load prompts from YAML files by name
- Format prompts with dynamic values using keyword arguments
- Automatically create directories for prompts if they don't exist
- List all available prompts in the specified base directory
- Colorized error messages for better visibility

## Installation

To install Promptsy, you can use pip:

```bash
pip install promptsy
```

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

## Prompt

The `Prompt` class represents a prompt and provides methods for formatting and saving/loading prompts.

### Initialization

```python
prompt = Prompt(name, description, template)
```

- `name` (str): The name of the prompt.
- `description` (str): A brief description of the prompt.
- `template` (str): The template string for the prompt.

### Formatting a Prompt

```python
formatted_prompt = prompt.format(**kwargs)
```

- `**kwargs`: Keyword arguments to be used for formatting the template.
- Returns: The formatted prompt string.

### Saving a Prompt

```python
prompt.save(manager)
```

- `manager` (PromptManager): The PromptManager instance to use for saving the prompt.

### Loading a Prompt

```python
loaded_prompt = Prompt.load(manager, name)
```

- `manager` (PromptManager): The PromptManager instance to use for loading the prompt.
- `name` (str): The name of the prompt to load.
- Returns: The loaded Prompt instance.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/feliperafael/promptsy).

## License

This project is licensed under the [MIT License](LICENSE).