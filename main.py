from promptsy.prompt import Prompt
from promptsy.prompt_manager import PromptManager
from promptsy.prompt_enhancer import PromptEnhancer
from openai import OpenAI

from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

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
loaded_prompt = manager.load("hello_world")

print(loaded_prompt)  # Output: hello_world: An example prompt
print(loaded_prompt.format(name="Taylor Swift"))  # Output: Hello, Taylor Swift!


prompt_toddlers_story_time = Prompt(
    name="toddlers_story_time",
    description="Write a bedtime story for toddlers",
    template="You are a bedtime story teller for toddlers. Write a story for a toddler about a {animal} that goes on an adventure to {place}."
)

# Create an instance of PromptEnhancer
enhancer = PromptEnhancer(model_name="gpt-4o-mini")

# Enhance the prompt
prompt_toddlers_story_time_enhanced = enhancer.enhance_prompt(prompt_toddlers_story_time)

print("Original Prompt:")
print(prompt_toddlers_story_time.template)

print("\nEnhanced Prompt:")
print(prompt_toddlers_story_time_enhanced.template)

def call_openai_api(prompt, max_tokens=800):
    import os
    from openai import OpenAI  # Import the OpenAI class

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OpenAI API key not provided and OPENAI_API_KEY environment variable not set.")
    
    client = OpenAI(api_key=api_key)  # Initialize the OpenAI client

    response = client.chat.completions.create(  # Use the client to make the API call
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt.template}],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content.strip()

# Call the API using the prompts
response_toddlers_story_time = call_openai_api(prompt_toddlers_story_time)
response_toddlers_story_time_enhanced = call_openai_api(prompt_toddlers_story_time_enhanced)

print(Fore.YELLOW + "\nResponse for toddlers_story_time:")
print(response_toddlers_story_time)

print(Fore.GREEN + "\nResponse for toddlers_story_time_enhanced:")
print(response_toddlers_story_time_enhanced)
