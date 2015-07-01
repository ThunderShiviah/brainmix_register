from fabric.api import *
from fabric.contrib.console import confirm

def create_sphinx_pages():
    """
    Create a new branch with Sphinx documentation ready to be published
    using GitHub's Pages system.

    Example usage:

        $ fab make_sphinx_branch

    Before you can publish your docs, you need to commit them to the repo.

        $ git add .
        $ git commit -am "First commit"

    Then publish the files by pushing them up to GitHub.

        $ git push origin gh-pages

    Then the docs will appear on GitHub at:

        http://<your_account_name>.github.com/<your_repo_name>/

    """
    # CREATE CLEAN GH-PAGES BRANCH AND CHECK IT OUT
    local("git branch gh-pages")                           # create the new branch
    local("git checkout gh-pages")                         # move into it
    local("git symbolic-ref HEAD refs/heads/gh-pages")     # clear it out
    local("rm .git/index")
    local("git clean -fdx")

    # INSTALL SPHINX AND SETUP PROJECT
    local("pip install sphinx")                            # install sphinx
    local("pip freeze > requirements.txt")                 # save dependencies
    local("sphinx-quickstart")                             # start sphinx project
    local("touch .nojekyll")                               # create .nojekyll file 
    
    # PATCH SPHINX MAKEFILE 
    local("echo '' >> Makefile")
    local("echo 'BUILDDIR      = ./' >> Makefile")
    local("echo '' >> Makefile")
    local("echo 'html:' >> Makefile")
    local("echo '\t$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)' >> Makefile")
    local("echo '\t@echo' >> Makefile")
    local("echo '\t@echo \"Build finished. The HTML pages are in $(BUILDDIR)\"' >> Makefile")

    # MAKE THE BRANCH FOR FIRST TIME
    local("make html")