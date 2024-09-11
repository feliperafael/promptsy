from setuptools import setup, find_packages

setup(
    name='promptsy',
    version='0.1.3.2',
    description='A Python library for managing and organizing prompts for Large Language Models (LLMs)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Felipe Rafael de Souza',
    author_email='felipe@evakub.com.br',
    url='https://github.com/feliperafael/promptsy',
    packages=find_packages(),
    include_package_data=True,  # Inclui arquivos de dados
    package_data={
        'promptsy': ['prompts/*.yaml'],  # Inclui todos os arquivos YAML na pasta prompts
    },
    install_requires=[
        'PyYAML',
        'colorama',
        'openai',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='prompts llm-prompts prompt-management large-language-models',
)
