---
toc:
  depth_from: 1
  depth_to: 2
  ordered: false
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [**Background**](#background)
- [**Environment Setup**](#environment-setup)
  - [**Python3**](#python3)
  - [**Jupyter Notebook and or JupyterLab**](#jupyter-notebook-and-or-jupyterlab)
  - [**Visual Studio Code**](#visual-studio-code)
  - [**Git**](#git)
- [**Other Resources**](#other-resources)
  - [**Google Colab as Alternative to Jupyter Notebook**](#google-colab-as-alternative-to-jupyter-notebook)

<!-- /code_chunk_output -->

# **Background**

In this session, we will focus on demonstrating the following key aspects of **ML Engineering**

- Environment Setup
  - Python3
  - Jupyter Notebook and or JupyterLab
  - Visual Studio Code
  - Git
  - Virtual Environments
  - (Optional)
    - Spyder
    - PyCharm
    - Anaconda
- Define the Problem
- Data Source and Engineering
- Exploratory Data Analysis
- Feature Engineering
- Algorithm Selection
- Model Training
- Model Evaluation
- Hyperparameter Tuning
- Model Deployment
- Model Monitoring

# **Environment Setup**

## **Python3**

Depending on your machine's operating system, there are corresponding ways to install `Python3`. If you are on Mac, \*it is worth a while to check if it is already installed on your machine:

1. Open your _Spotlight_ search with `Command + Space` and open _Terminal_.
2. Type `python3 --version` and hit `Enter`. If you see something like `Python 3.7.3`, you are good to go. Otherwise, you will need to install `Python3` on your machine.

By simply going to [Python.org](https://www.python.org/downloads/), it will automatically detect your operating system and provide you with the latest version of `Python3`. Make sure to **download the LATEST version** of `Python3` and **NOT** `Python2`.

If you are on Mac, you can also install `Python3` via [Homebrew](https://brew.sh/). If you are on Windows, you can also install `Python3` via [Chocolatey](https://chocolatey.org/).

## **Jupyter Notebook and or JupyterLab**

Once `Python3` is installed on your machine, you can install `Jupyter Notebook` and or `JupyterLab` via `pip3`:

<ol>
<li>
    Depending on your OS:
    <ol type="a">
        <li><b>MacOS</b>: Open your <i>Spotlight</i> search with <code>Command + Space</code> and open <i>Terminal</i>.</li>
        <li><b>Windows</b>: Open your <i>Start</i> search with <code>Windows Key</code> and open <i>Command Prompt</i>.</li>
    </ol>
    Check that <code>Python</code> is indeed installed by running <code>python3 --version</code> in your <i>Terminal</i>.
</li>

<br>

<li> You can choose to install **either** or **both** of the following. <code>Jupyter Notebook</code> is the original version of the notebook, while <code>JupyterLab</code> is the newer version of the notebook. <code>JupyterLab</code> is more powerful and has more features than <code>Jupyter Notebook</code>. However, <code>JupyterLab</code> is still in beta and is not as stable as <code>Jupyter Notebook</code>. <code>Jupyter Notebook</code> is more stable and is the recommended version for beginners.
    <ol type="a">
        <li>Type <code>pip3 install jupyter notebook</code> and hit <code>Enter</code>.</li>
        <li>Type <code>pip3 install jupyterlab</code> and hit <code>Enter</code>.</li>
    </ol>
You can find **more information** about each of these along with some *installation* notes by going to the following links:
    <ul>
        <li><a href="https://jupyter.org/install">Jupyter Notebook</a></li>
        <li><a href="https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html">JupyterLab</a></li>
    </ul>
<br>

Here's a summative comparison of the two:

<table border="1">
        <thead>
            <tr>
                <th>Feature</th>
                <th>Jupyter Notebook</th>
                <th>JupyterLab</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Interface</td>
                <td>Single-document interface</td>
                <td>Flexible, integrated, and extensible multi-document interface</td>
            </tr>
            <tr>
                <td>File Explorer</td>
                <td>Basic</td>
                <td>Advanced with drag-and-drop</td>
            </tr>
            <tr>
                <td>Text Editor</td>
                <td>Basic</td>
                <td>Advanced with syntax highlighting and automatic language detection</td>
            </tr>
            <tr>
                <td>Extensions</td>
                <td>Limited</td>
                <td>Supports a wide range of extensions</td>
            </tr>
            <tr>
                <td>Code Consoles</td>
                <td>Not available</td>
                <td>Available, allows to run code interactively</td>
            </tr>
        </tbody>
    </table>
</li>

<br>
<li>
    Once both <code>Python3</code> and <code>Jupyter Notebook</code> are installed, we can <b>instantiate the server</b> to write and run the Notebooks. While on your <i>Terminal</i> or <i>Command Prompt</i>, simply type <code>jupyter notebook</code> and hit <code>Enter</code>. This will open a new tab on your default browser with the following URL: <code>http://localhost:8888/tree</code>. You can now create a new Notebook by clicking on the <code>New</code> button on the top right corner and selecting <code>Python 3</code>.
</li>
</ol>

## **Visual Studio Code**
Personally, I prefer using this for the following reasons
- considerably a **full-fledged IDE** with a lot of features that I can use not just for **ML/AI Engineering** but also for **Software Engineering** or **Web Development**
- it is both **web-based** and **desktop-based** which allows me to code on the go
- it has a **built-in terminal** which allows me to run my code without having to switch to another window (such as **separately** opening a **Terminal** or **Command Prompt**)
- it has a **built-in Git** which allows me to **commit** and **push** my code to **GitHub** without having to switch to another window (such as **separately** opening **GitHub Desktop** or **Git Bash**)
- it has a **built-in Jupyter Notebook** which allows me to write and run my **Notebooks** without having to switch to another window (such as **separately** opening a **Jupyter Notebook** or **JupyterLab**)
- there is a **rich marketplace** of **extensions** that I can use to **customize** my **IDE** to my liking

Installation is soooo simple:
1. Go to [Visual Studio Code](https://code.visualstudio.com/) and download the latest version for your operating system.
2. Once downloaded, open the installer and follow the instructions.
3. Once installed, open the application and you are good to go!

## **Git**
Git is a free and open source distributed **version control system** designed to handle everything from small to very large projects with speed and efficiency. **VERSION CONTROL** is pretty important especially if you are working on a team as it allows you to
- share codebase with your team
- **track** and **compare** changes which allows your team or your organization keep track of updates and changes to the codebase made by each member
- **revert** changes which allows your team or your organization to go back to a previous version of the codebase in case of any errors or bugs
- allows you to put a separation between your **local** and **remote** codebase which allows you to work on your codebase locally and then push it to the remote codebase once you are done with your changes (or experiment with your own things before pushing it to the remote codebase)

For simplicity, we will use `Github` with `git` to have both a **user-interface** to browse shared codebases and a **command-line interface** to manage our own codebases.
- `git` is the **command-line interface** that allows you to track, commit, push, revert, compare, and do other things to your codebase
- `Github` is the **user-interface** that allows you to browse, compare, and do other things to your codebase

1. Create an account on [Github](https://github.com/).
2. Download and install [Github Desktop](https://desktop.github.com/).
3. Once installed, open the application and sign in using your Github account.
4. You can find the instructions on how to use `Github Desktop` by going to the following link: [Github Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop).

If you want to use `git` on your **Terminal** or **Command Prompt**, you can do so by installing `git` on your machine.
1. You can find the instructions on how to install `git` on your machine by going to the following link: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Once installed, you can check that `git` is indeed installed by running `git --version` in your **Terminal** or **Command Prompt**.
3. You can find the instructions on how to use `git` by going to the following link: [Git](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics).

# **Other Resources**
One important component of your arsenal would be **data sources**. Although there are *tons* of open-source data sources available online, it is important to know where to look for them. Here are some of the resources that I use to find data sources:
- [Kaggle](https://www.kaggle.com/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Awesome Public Datasets](https://github.com/topics/awesome-public-datasets)
- [Data.gov](https://www.data.gov/)
- [Data.world](https://data.world/)
- [Datahub](https://datahub.io/)
- [Dataquest](https://www.dataquest.io/blog/free-datasets-for-projects/)
- [Data is Plural](https://tinyletter.com/data-is-plural)
- [Amazon Web Services (AWS) Public Datasets](https://aws.amazon.com/datasets/)
- [Microsoft Research Open Data](https://msropendata.com/)a

> For our first demo, we will get dataset from **Kaggle** which means, it is better to create an account on [Kaggle](https://www.kaggle.com/) if you haven't already.

1. Create an account on [Kaggle](https://www.kaggle.com/).
2. Once logged in, go to the following link: [Kaggle Datasets](https://www.kaggle.com/datasets).
3. You can now browse through the available datasets and download the ones that you want to use for your projects.
4. Generate an API token by going to your account settings and clicking on the `Create New API Token` button under the `API` section. This is so that we can download datasets from **Kaggle** using `kaggle` on our **Terminal** or **Command Prompt**.
5. You can find the instructions on how to use `kaggle` by going to the following link: [Kaggle API](https://github.com/Kaggle/kaggle-api).

## **Google Colab as Alternative to Jupyter Notebook**

This open-source tool is very useful especially for *collaborative* work. Furthermore, you can quickstart your workflow *without need of downloading `Python3` into your machine*. Right off the bat, you can code.

However, since this uses shared cloud resources, you are limited to the specs of the publicly available virtual machines. Some limitations of this include
- limited RAM = difficulty dealing with virtual machines
- limited disk space = you can't upload very big datasets to work with
- limited GPU = you can't train very big models

Nevertheless, **big datasets** can still be uploaded as long as the are saved in your Google Drive. But since there's still limited RAM, working on pre-processing the large dataset is still a big challenge.