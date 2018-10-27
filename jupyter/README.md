# CS3200 (Fall 2018 section 2) Setup Instructions for Jupyter Activities

We are using Jupyter notebooks for various activities in our classes. Jupyter notebooks (formerly known as IPython notebooks) are a flexible tool to create and share code, comments, formulae, and outputs (e.g. for SQL queries).  

You can find a 3rd party Jupyter tutorial [here](https://www.dataquest.io/blog/jupyter-notebook-tutorial/), and more tips and tricks [here](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).  

If you have trouble with these instructions, please post your issues with screenshots on Piazza or stop by during office hours.


## Acknowledgements 
We have adapted these notebooks from [Chris Re](https://cs.stanford.edu/people/chrismre/) and [Peter Bailis](http://www.bailis.org/) - many thanks to them!

## Step 1: Install Git and Pip

1. Install [Git](https://git-scm.com/downloads).  
 Git is a version control system that allows us to distribute and collaboratively edit files.  
 Check out this simple [guide](https://rogerdudler.github.io/git-guide/) if you are not familiar with Git.

2. Install [pip](https://pip.pypa.io/en/stable/installing/), a package manager for python.

## Step 2: Install Jupyter Notebook and libraries

1. Check out our class activities repository to your local computer.

	```bash
	# From a suitable local directory...
	git clone https://github.com/northeastern-datalab/cs3200-activities.git
	```

2. To install necessary python dependencies:

	```python
	cd cs3200-activities/jupyter
	pip install -r requirements.txt
	```
 Depending on your folder permissions, you may need to use `sudo pip install ...`.  
 If you would like to install only for the current user, use `pip install --user ...`

3. Be sure you now have `jupyter` command available in your environment.

 Try the following:
```bash
jupyter --version
```

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

2. To avoid overwriting your local changes, be sure to practice Git.  
 You can make yourself a local branch to keep track of your changes.  
 If you are not comfortable with Git, you can save your modified copy of these files elsewhere on your computer.
