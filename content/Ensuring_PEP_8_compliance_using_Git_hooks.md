Title: Ensuring PEP 8 compliance using Git hooks
Date: 2014-08-20 15:11
Tags: python
SUmmary: Making your Python code more readable

PEP 8 is the Python language's style guide. It is accepted by the community as the best standards for any Python code. `Pylint` is a program for checking Python style. We can ensure all of our Python code is clean and elegant using Git hooks. 

## What are hooks?

Git hooks are essentially scripts that run before or after you perform various actions in `git`. Some examples are a script that runs before a commit, after a commit, or after a merge. These scripts are stored in a repository's `.git/hooks` folder. They can be written in a variety of languages but are most commonly written in Bash, Python, Ruby, or Perl.

## PEP 8 Compliance

We can check our code for compliance using `pylint` and `pep8`. To install these use the following commands. 

```
pip install pep8
apt-get install pylint
```
You may also need to use `sudo` if you are not the root user when executing these commands. If you are on a Red Hat based linux system use `yum` instead of `apt-get`. If you are on OS X or Windows then [go do some Googling](http://lmgtfy.com/?q=how+to+install+linux). 

## Step 1: The script

Before we can do anything we need to write our script. It needs to check each Python source file against `pep8` followed by `pylint`. If `pep8` finds any errors or if `pylint` has a score less than 9.00/10 it should exit with a failed status code. You can decide what score your code should pass with in `pylint`, but I like 9/10 as it means the code is near perfect. Ideally it would pass with 10/10 but sometimes that just is not possible. 

<script src="https://gist.github.com/ThaWeatherman/f7ae231e85d74b62e049.js?file=pre-commit"></script>

This is our final script. It is a little rough around the edges but I had to do some hacky things to extract the `pylint` score.

## Step 2: Add it to your repo

Now that we have a working script we need the git repository to recognize the hook. Make your script executable using
> chmod 744 pre-commit

where `pre-commit` is the name of your script. Now move it to the repository's `.git/hooks` folder and it is good to go! Note that for every repository you want to use this hook in you must add this script.

## Step 3: Commit as normal

You can test that it works by trying to do a commit. Because it is the `pre-commit` script it will run before the commit is finalized. If it passes then the code is committed, otherwise it will fail and tell you why it failed. 

You can use the following example code to demonstrate that it works. The first file is a fully compliant example while the other is vile. Initialize a git repo, add the `pre-commit` script and these two files, then try a commit and see what happens. 

<script src="https://gist.github.com/ThaWeatherman/f7ae231e85d74b62e049.js?file=good.py"></script>

<script src="https://gist.github.com/ThaWeatherman/f7ae231e85d74b62e049.js?file=bad.py"></script>

## Additional reading

If you would like to understand each of these topics better please read through the following links. 

- [Git hooks](http://githooks.com/)
- [PEP 8](http://legacy.python.org/dev/peps/pep-0008/) the style guide
- [PEP 257](http://legacy.python.org/dev/peps/pep-0257/) docstring conventions
- [PEP 20](http://legacy.python.org/dev/peps/pep-0020/) Zen of Python
