# CrewAI

## A simple CrewAI example
This simple example creates a single agent (Writer) which receives a tech topic and creates a small blog-post. The output is a markdown file.
The important thing here is the integration with ollama. Ollama allows easy access to a list of LLMs.

### Ollama set-up 
- Install Ollama. You can find information at [Ollama](https://ollama.com/) or [Ollama_github](https://github.com/ollama/ollama)
- Download one model with the ollama pull {name_of_the_model} e.g. `ollama pull gemma:2b` to download and use locally the **gemma:2b** model
- Create a Modelfile. Authors of CrewAI suggest you create a custom modelfile. So, create a file named **customModelfile**. Inside write:
    -   ```
        FROM gemma:2b
        PARAMETER temperature 0.8
        PARAMETER stop Result
        ```
    - `ollama create CrewAI -f ./customModelfile`  note: Replace *./customModelfile* with your actual path.

- Make sure that the model exist by showing all the models you have available with the following command:
    - `ollama list`
- Make sure that ollama is running with the following command:
    - `ollama run CrewAI`
    - To leave the chat write on the terminal */bye*

### Create your prefered virtual environment
- Use the command in your terminal: *python -m venv /path/to/new/virtual/environment* and then activate the venv. 
- `python -m venv .venv`
- Windows version: `venv\Scripts\activate`
- Then install all depedencies by: `pip3 install -r requirements.txt`
- Then create a new folder inside your working folder **e.g. Crew**.
- Then paste the following files inside:
    - .env
    - main.py
- Create a new folder inside and name it : **blog-posts**

### Set up you *.env* file
- The only thing you need to change is the *OPENAI_MODEL_NAME=*. Make sure that you put the name you gave in the custom model. **e.g. CrewAI**

### Run the **main.py**
- cd into the Crew folder: `cd crew`
- `python main.py`