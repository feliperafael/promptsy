
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
- Generate few-shot examples for prompts using the `FewShotPromptGenerator`, allowing for improved context and response generation based on specified expected outputs.

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

# Create an instance of Prompt
prompt = Prompt(
    name="hello_world",
    description="An example prompt",
    template="Hello, {name}!"
)

# Save the prompt using the Prompt's save method
prompt.save()  # Não é necessário passar o PromptManager

# Load the prompt using the Prompt's load method
loaded_prompt = Prompt.load("hello_world")  # Não é necessário passar o PromptManager

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
prompt.save(name)  # O método save agora é chamado diretamente no objeto Prompt
```

### Loading a Prompt

```python
loaded_prompt = Prompt.load(name)  # O método load agora é chamado diretamente na classe Prompt
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
prompt_toddlers_story_time.save()

# Create an instance of PromptEnhancer
enhancer = PromptEnhancer()

# Enhance the prompt
enhanced_prompt = enhancer.enhance_prompt(prompt_toddlers_story_time)

print("Enhanced Prompt:")
print(enhanced_prompt.template)
```

### Saving Enhanced Prompts

The enhanced prompts are automatically saved in the `enhanced_prompts` directory.

## Example Usage of FewShotPromptGenerator

Here’s an example of how to use the `FewShotPromptGenerator` to generate few-shot examples for a sentiment analysis prompt:

```python
from promptsy.auto_few_shot_generator import FewShotPromptGenerator
from promptsy.prompt import Prompt

# Create an instance of Prompt for sentiment analysis
sentiment_analysis_prompt = Prompt(
    name="sentiment_analysis",
    description="Generate a sentiment analysis prompt",
    template="You are a sentiment analysis prompt generator. Generate a prompt for sentiment analysis for the following text: {text}"
)

# Create an instance of FewShotPromptGenerator
few_shot_generator = FewShotPromptGenerator(model_name="gpt-4o-mini")

# Generate few-shot examples using the sentiment analysis prompt
num_examples = 3
expected_outputs = ["negative", "positive", "neutral"]
sentiment_analysis_prompt_with_examples = few_shot_generator.generate_examples(
    prompt_initial=sentiment_analysis_prompt,
    num_examples=num_examples,
    expected_outputs=expected_outputs,
    return_examples=False
)

print("Formatted Prompt with Few-Shot Examples:")
print(sentiment_analysis_prompt_with_examples.template)

# Optionally, you can call the OpenAI API with the generated prompt
final_prompt = sentiment_analysis_prompt_with_examples.format(text="I am so happy today, but I am tired!")
print(final_prompt)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/feliperafael/promptsy).

## License

This project is licensed under the [MIT License](LICENSE).
