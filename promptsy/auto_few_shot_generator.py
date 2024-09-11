import os
from openai import OpenAI
from promptsy.prompt import Prompt
from promptsy.prompt_manager import PromptManager
from pydantic import BaseModel
from typing import List,Optional

class Example(BaseModel):
    question: str
    answer: str

class FewShotPromptGenerator:
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gpt-4o-mini"):
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key is None:
                raise ValueError("OpenAI API key not provided and OPENAI_API_KEY environment variable not set.")
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        self.prompt_manager = PromptManager()
        self.auto_few_shot_prompts_directory = 'auto_few_shot_prompts'
        os.makedirs(self.auto_few_shot_prompts_directory, exist_ok=True)


    def generate_examples(self, prompt_initial: Prompt, num_examples: int = 5, expected_outputs: Optional[List[str]] = None, return_examples=False) -> str:
        """
        Generates a formatted prompt with few-shot examples based on the initial prompt and expected outputs.

        :param prompt_initial: The initial Prompt object for the LLM.
        :param num_examples: Number of examples to generate.
        :param expected_outputs: Optional list of expected outputs (e.g., ['positive', 'negative', 'neutral']). If not provided, the model will generate general responses.
        :param return_examples: Optional return examples
        :return: Formatted prompt with examples.
        """
        # Use the template from the Prompt object
        prompt_template = prompt_initial.template
        examples = [self.generate_example(prompt_template, expected_outputs) for _ in range(num_examples)]
        
        formatted_prompt = self._format_few_shot_prompt(prompt_template, examples)
       
        prompt_initial.template = self.__call_llm_reformat_prompt(formatted_prompt)

        self.save_few_shot_prompt(prompt_initial)  # Save the original Prompt object

        if return_examples:
            return prompt_initial, examples
        
        
        return prompt_initial

    def generate_example(self, prompt_initial: str, expected_outputs: Optional[List[str]] = None) -> Example:
        """
        Generates an input-output example using the LLM based on the initial prompt and expected outputs.

        :param prompt_initial: The initial prompt for the LLM.
        :param expected_outputs: Optional list of expected outputs.
        :return: An Example object containing the question and answer.
        """
        response = self._call_llm(prompt_initial, expected_outputs)
        return Example(**response)
    
    def __call_llm_reformat_prompt(self, prompt: str):
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": f"""
               You are a prompt formatter specialist. Your task is to create a formatted prompt for a given task using the following structure (DO NOT CREATE NEW EXAMPLES):
                    # Structure
                        1 - Prompt Instructions
                        2 - Examples
                        3 - User input included in curly braces variables to completitions
                        

                # Now is your time to format the prompt
                {prompt}

            """}],
            stream=False,
        )
        return response.choices[0].message.content.strip()

        pass
    def _call_llm(self, prompt: str, expected_outputs: Optional[List[str]] = None) -> dict:
        """
        Calls the LLM to generate input-output examples based on the provided prompt and expected outputs.

        :param prompt: The initial prompt for the LLM.
        :param expected_outputs: Optional list of expected outputs.
        :return: Dictionary with generated question and answer.
        """
        if expected_outputs:
            expected_output_str = ", ".join(expected_outputs)
            system_message = (
                f"You are an AI assistant tasked with generating diverse and unbiased input-output examples "
                f"for the provided prompt. You must strictly limit the outputs to one of the following values: {expected_output_str}. "
                "Ensure that the examples represent a wide variety of contexts, but the output must always be one of these values. "
                "Do not generate outputs outside of the provided values. Avoid stereotypes or biases."
            )
            user_message = (
                f"Generate an input-output example for the following prompt: {prompt}. "
                f"The output must strictly be one of the following values: ({expected_output_str}). "
                "Ensure the output fits one of these categories and nothing else."
            )
        else:
            system_message = (
                "You are an AI assistant tasked with generating diverse and unbiased input-output examples "
                "for the provided prompt. Ensure that the examples represent a wide variety of contexts, "
                "avoiding any stereotypes or biases."
            )
            user_message = f"Generate a diverse and unbiased input-output example for the following prompt: {prompt}."

        completion = self.client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            response_format=Example,
        )
        
        return completion.choices[0].message.parsed.dict()

    def _format_few_shot_prompt(self, prompt_initial: str, examples: List[Example]) -> str:
        """
        Formats the prompt with a list of examples for few-shot learning.

        :param prompt_initial: The initial prompt for the LLM.
        :param examples: List of Example objects.
        :return: Formatted prompt with examples.
        """
        formatted_examples = ""
        for idx, example in enumerate(examples, start=1):
            formatted_examples += (
                f"## Example {idx}\n"
                f"{example.question}\n"
                f"{example.answer}\n\n"
            )
        return f"{prompt_initial}\n\n# Examples\n{formatted_examples}\n\n# Output\n"
    
    def save_few_shot_prompt(self, prompt: Prompt):
        """
        Saves the generated few-shot prompt using the PromptManager.
        
        :param prompt: The formatted few-shot prompt to be saved.
        """
        # Directly save the existing Prompt object
        self.prompt_manager.save(prompt, os.path.join(self.auto_few_shot_prompts_directory, prompt.name))
        print(f"Few-shot prompt saved using PromptManager: {prompt.name}")
