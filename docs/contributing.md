# Contributing to https://MediaStack.Guide

Anyone can easily join and contribute to the https://MediaStack.Guide GitHub repo, to improve the overall documentation / website by following these steps.

First, you will need an active GitHub.com account if you are looking to push changes / updates back to the https://MediaStack.Guide repo on GitHub

Setting up your environment to run MkDocs for Development / Contribution to https://MediaStack.Guide

**Download and Install Microsoft Visual Studio Code**
 - https://code.visualstudio.com/download

**Download and Install Git for Windows**
 - https://git-scm.com/download/win

**Download and Install Python**
 - https://www.python.org/downloads

**Download and Install Miniconda**
 - https://docs.conda.io/en/latest/miniconda.html

**Goto Visual Studio Code Extentions (Ctrl+Shift+X) and Install:**
 - Python (by Microsoft) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Or at: https://marketplace.visualstudio.com/items?itemName=ms-python.python
 - Python Environment Manager &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager
 - Start git-bash &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash
 - GitHub Repositories &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub
 - GitHub Pull Requests and Issues &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
 - YAML &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
 - shell-format    https://marketplace.visualstudio.com/items?itemName=foxundermoon.shell-format

**Optional Visual Studio Code Extentions:**
 - Azure Repos (Optional for TFVC) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-repos
 - WSL (optional)  - If using WSL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Or at: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
 - WSL Recommender - If using WSL &nbsp; &nbsp; &nbsp; &nbsp; Or at: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl-recommender
 
**Test all of the programs are working correctly:**
 - Open Windows Start Menu, you should be able to see:
   - Anaconda Prompt (Miniconda3)
   - Git Bash
   - Python 3.11 (64-bit)

 - Start "Git Bash" and run these commands to see if they're in the environment path (may need a reboot if this is the first time running them)
   - Execute "conda"
   - Execute "pip"
   - Execute "py --version"

>The above tests should confirm you have the correct packages installed and the paths are working, in order to create the Conda environment needed to host the MkDocs files while editing / contributing on your local system.


Start "Git Bash" from the Windows Start Menu, and create a folder to replicate any GitHub repos to.. i.e. "C:\GitHub"

```
mkdir C:\GitHub
cd C:\GitHub
git clone https://github.com/geekau/mediastack.guide.git
cd mediastack.guide
code .
```

Visual Studio will now open and ask you to trust the files you have pull from GitHub into the "C:\GitHub\mediastack.guide" folder - Select Yes to trust the folder.


**Select Python Intepreter**

In Visual Studio Code opening the Command Palette (Ctrl+Shift+P), start typing "Python: Select Interpreter" - Press Enter

Select: "Python 3.9... ('base') C:\ProgramData\Miniconda3\python.exe **Conda**"

**Select Terminal Intepreter**

In Visual Studio Code opening the Command Palette (Ctrl+Shift+P), start typing "Terminal: Select Default Profile" - Press Enter and select: "Git Bash"

From the top menu, select "Terminal" --> "New Terminal" (Ctrl+Shift+`), the new terminal should now be "Git Bash".

**Setup Python environment to support the downloaded MediaStack.Guide files**

From the Git Bash terminal, type ls -la, you should be inside the "C:\GitHub\mediastack.guide" folder, and be able to see the following files:

- init_setup.sh - Script to built a local Python environment on your system for development / testing
- requirements.txt - Includes the files needed as part of the local environment (MkDocs, Material for MkDocs, Awesome Pages for MkDocs etc..)
- runtime.txt - Sets the Conda sets the Python version to 3.7, so all developers contributing on MediaStack.Guide repo are all using the same version

As this is the first time using the Git Bash terminal, you may need to initialiase it with the following command, then closing / restarting the terminal window:

```
conda init bash
```

If you are in the correct folder and can see all of these files, then you can execute the following command in the Git Bash terminal to build your environment:

```
bash init_setup.sh
```

>This will take a few minutes to build your local environment, depending on your Internet speed.

**Activate the virtual environment for the mediastack.guide project**

In order to run any of the commands / scripts which have now been set up in the "ENV" environment, you need to activiate the environment with the following command:

```
conda activiate ./env
```

Now the environment has been activated, you can call commands from that environment, to help you develop and test using the environment which is now standardised for all contributing developers.

Type the following command to run a local webserver on port 8888, which will serve all of the MkDocs files from your working copy

```
mkdocs serve
```

You should see the following output:
```
$ mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.02 seconds
INFO     -  [12:00:00] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [12:00:00] Serving on http://127.0.0.1:8000/
```

You should be able to open a web browser on http://127.0.0.1:8000/ and see all of the files you have pulled down from the repository, and they will automatically update on the local web server as you make any file saves to your local copy of the repository.

>Press CTRL+C to exit the mkdocs server

**Project development branches on GitHub**

If you make changes to your local copies of the files and want to "push" them back up to the GitHub repository, there are currently three branches being used for development / release:

- commits:  This is the branch that all community contributions should be pushed to.
- preview:  The review committee will pull changes which have been uploaded to the commit branch, into the preview branch, in order to stage any updates, prior to going into the main branch.
- main:  This is the "main" / production branch, that is linked to the https://MediaStack.Guide web server, and all updates will be reviewed rigoursly prior to merging from the preview branch.


**Viewing development / production branches on the website**

- main:   https://MediaStack.Guide
- preview:  https://
- commits:  https://


**Open Markdown preview window in the side window**

In Visual Studio Code opening the Command Palette (Ctrl+Shift+P), start typing "Markdown: Open Preview to the Side" - Press Enter


**Environments are not working**

If the commands for conda, pip, bash, py etc... are not working, you may need to add these folders to your "PATH" system environment variable, and restart your computer:
```
C:\Program Files\Python311\
C:\Program Files\Python311\Scripts\
C:\ProgramData\Miniconda3
C:\ProgramData\Miniconda3\Scripts
C:\ProgramData\Miniconda3\shell\condabin
```

**Additional guidance on how to set up Python and Conda with Visual Studio Code**

Setup Anaconda (Python) to Work With Visual Studio Code on Windows:
 - https://opensourceoptions.com/blog/setup-anaconda-python-to-work-with-visual-studio-code-on-windows/

Python for Visual Studio Code:
 - https://docs.anaconda.com/anaconda/user-guide/tasks/integration/python-vsc/


**Some guidance on how to work collaboratively with others, using Visual Studio Code and GitHub**

Good reading on how to Collaborate on GitHub using Visual Studio Code
 - https://code.visualstudio.com/docs/sourcecontrol/overview
 - https://code.visualstudio.com/docs/sourcecontrol/github
 - https://code.visualstudio.com/docs/sourcecontrol/faq

signing commits
https://ona.io/home/signing-git-commits-using-your-gpg-key/

git config --global commit.gpgsign true
