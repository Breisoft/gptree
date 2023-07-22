from gptree.tree import FileExplorer

import os

import subprocess

def cli():

    gui = os.path.join(os.path.dirname(__file__), 'gui')

    streamlit_app = os.path.join(os.path.join(gui), 'streamlit_app.py')


    current_dir = os.getcwd()
    os.environ['GPTREE_DIR'] = current_dir  # Set the environment variable

    subprocess.run(["streamlit", "run", streamlit_app])

def get_files():

    file_explorer = FileExplorer()

    return file_explorer.get_python_files()

def get_full_prompt(prompt):
    cwd = os.getcwd()

    full_prompt = f"""{prompt}\n\n"""

    for path, src in get_files():
        path = path.replace(f"{cwd}{os.path.sep}", "")

        full_prompt += f"{path}:\n"

        full_prompt += f"```py\n {src}```\n\n"

    return full_prompt