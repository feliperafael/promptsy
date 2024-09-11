from promptsy.auto_few_shot_generator import FewShotPromptGenerator
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

def enhance_prompt_recursively(prompt, iterations=3):
    enhanced_prompt = prompt
    for _ in range(iterations):
        enhanced_prompt = enhancer.enhance_prompt(enhanced_prompt)
    return enhanced_prompt

# Enhance the prompt recursively
prompt_toddlers_story_time_enhanced = enhance_prompt_recursively(prompt_toddlers_story_time, iterations=3)

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
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content.strip()

# Call the API using the prompts
response_toddlers_story_time = call_openai_api(prompt_toddlers_story_time.template)
response_toddlers_story_time_enhanced = call_openai_api(prompt_toddlers_story_time_enhanced.template)

print(Fore.YELLOW + "\nResponse for toddlers_story_time:")
print(response_toddlers_story_time)

print(Fore.GREEN + "\nResponse for toddlers_story_time_enhanced:")
print(response_toddlers_story_time_enhanced)


# Example usage of FewShotPromptGenerator
few_shot_generator = FewShotPromptGenerator(model_name="gpt-4o-mini")


sentiment_analysis_prompt = Prompt(
    name="sentiment_analysis",
    description="make a sentiment analysis prompt",
    template="You are a sentiment analysis prompt generator. Generate a prompt for sentiment analysis for the following text: {text}"
)

# Generate few-shot examples using the toddlers story time prompt
num_examples = 3
expected_outputs = ["negative", "positive", "neutral"]
sentiment_analysis_prompt_with_examples = few_shot_generator.generate_examples(
    prompt_initial=sentiment_analysis_prompt,
    num_examples=num_examples,
    expected_outputs=expected_outputs,
    return_examples=False
)


print(Fore.RED +"\nFormatted Prompt with Few-Shot Examples:")
print(sentiment_analysis_prompt_with_examples.template)

final_prompt = sentiment_analysis_prompt_with_examples.format(text="I am so happy today, but I am tired!")
print(final_prompt)
# Optionally, you can call the OpenAI API with the generated prompt
response_with_examples = call_openai_api(final_prompt)
print(Fore.CYAN + "\nResponse with Few-Shot Examples:")
print(response_with_examples)

