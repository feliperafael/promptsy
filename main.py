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

loaded_prompt = Prompt.load(manager, "hello_world")

