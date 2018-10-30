# CS3200 (Fall 2018 section 2) Setup Instructions for Jupyter Activities

We are using Jupyter notebooks for various activities in our classes. Jupyter notebooks (formerly known as IPython notebooks) are a flexible tool to create and share code, comments, formulae, and outputs (e.g. for SQL queries).  

You can find a 3rd party Jupyter tutorial [here](https://www.dataquest.io/blog/jupyter-notebook-tutorial/), and more tips and tricks [here](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).  

If you have trouble with these instructions, please post your issues with screenshots on Piazza or stop by during office hours.


## Acknowledgements 
We have adapted these notebooks from [Chris Re](https://cs.stanford.edu/people/chrismre/) and [Peter Bailis](http://www.bailis.org/) - many thanks to them!

## Step 1: GitHub, Git, and Pip

1. To obtain our class files from GitHub, you have two choices. 
	1. You can install [Git](https://git-scm.com/downloads). Git is a version control system that allows us to distribute and collaboratively edit files. Using Git lets you easily retrieve the latest updates that we post. (Check out this simple [guide](https://rogerdudler.github.io/git-guide/) if you are not familiar with Git.)

	2. You can download a zip file from the repository on GitHub. Be aware that you will have to be careful re-download the zip file whenever we post updates.

2. Install [pip](https://pip.pypa.io/en/stable/installing/), a package manager for python.

## Step 2: Install Jupyter Notebook and libraries

1. Check out our class activities repository to your local computer. As mentioned, either use git to obtain the repo...

	```bash
	# From a suitable local directory...
	git clone https://github.com/northeastern-datalab/cs3200-activities.git
	```

	... or obtain a zip file of the repo and expand it. 

2. To install necessary python dependencies:

	```python
	cd cs3200-activities/jupyter
	pip install -r requirements.txt
	```

	If you obtained a zip file, it will have the git branch in its name, so you should instead use ("`cd cs3200-activities-master`")

	Depending on your folder permissions, and your Python installation you may need to use `sudo pip install ...`, or use `pip3` instead of `pip`.

	If you would like to install only for the current user, you can use `pip install --user ...`

	*** If you get an error relating to `BUILDING MATPLOTLIB... the following required packages can not be built: freetype`, you are missing some system libraries required for compiling Matplotlib. The easiest fix is to use [Homebrew](https://brew.sh/), and do `brew install pkg-config freetype`, and then re-try this step with `pip`.


3. Be sure you now have `jupyter` command available in your environment. Try `jupyter --version`

	If you get a command not found error, you may simply need to adjust your environment variables.

    * On Mac/Linux, your `$PATH` variable should include the location where `pip` installs libraries.  
    	If it does not, you may need to add a line like the following to your `~/.bashrc` file (Note - the folder locations mentioned here may be different on your machine!):
		```bash
		export PATH=${PATH}:/usr/local/bin
		```

    * On Windows, you may need to adjust your environment variables in a similar manner.

## Step 3: Launch Jupyter

1. Once the dependencies are installed, launch jupyter by navigating to this directory and doing:

	```bash
	cd cs3200-activities/jupyter
	jupyter notebook
	```

2. Be sure to save any changes you wish to keep. If you are using Git, you could make yourself a local branch and merge the changes we push to the master branch. Alternatively, you can save useful code snippets and modified files somewhere else on your local computer. 