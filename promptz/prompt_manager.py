import os
import yaml
from colorama import init, Fore, Style

init()  # Initialize colorama

class PromptManager:
    """
    A class for managing prompts stored in YAML files.

    Args:
        base_directory (str): The base directory where the prompts will be stored. Defaults to 'prompts'.
    """

    def __init__(self, base_directory='prompts'):
        """
        Initialize the PromptManager with the specified base directory.

        Args:
            base_directory (str): The base directory where the prompts will be stored. Defaults to 'prompts'.
        """
        self.base_directory = base_directory
        os.makedirs(base_directory, exist_ok=True)

    def _get_file_path(self, name):
        """
        Get the file path for a prompt with the given name.

        Args:
            name (str): The name of the prompt.

        Returns:
            str: The file path for the prompt.
        """
        parts = name.split('.')
        if len(parts) < 2:
            directory_path = os.path.join(self.base_directory, 'custom')
            file_name = f"{name}.yaml"
        else:
            directory_path = os.path.join(self.base_directory, *parts[:-1])
            file_name = f"{parts[-1]}.yaml"
        
        return os.path.join(directory_path, file_name)

    def save(self, prompt, name):
        """
        Save a prompt to a YAML file.

        Args:
            prompt (dict): The prompt data to be saved.
            name (str): The name of the prompt.
        """
        file_path = self._get_file_path(name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as file:
            yaml.dump({'text': prompt}, file)
        print(f"Prompt saved to {file_path}")

    def load(self, name):
        """
        Load a prompt from a YAML file.

        Args:
            name (str): The name of the prompt.

        Returns:
            dict: The loaded prompt data.

        Raises:
            FileNotFoundError: If the prompt file does not exist.
        """
        file_path = self._get_file_path(name)
        
        if not os.path.exists(file_path):
            error_message = f"Prompt file {file_path} does not exist."
            print(Fore.RED + error_message + Style.RESET_ALL)
            raise FileNotFoundError(error_message)
        
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data.get('text', '')

    def list_prompts(self):
        """
        List all the available prompts.

        Returns:
            list: A list of prompt names.
        """
        prompts = []
        for root, _, files in os.walk(self.base_directory):
            for file in files:
                if file.endswith('.yaml'):
                    relative_path = os.path.relpath(os.path.join(root, file), self.base_directory)
                    prompts.append(relative_path.replace(os.path.sep, '.').replace('.yaml', ''))
        return prompts