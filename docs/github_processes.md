# Github Processes

Here is a list of how to contribute to our repo, and some basic info on how to use common git/github features. This will be done using the command line, so make sure your machine [has git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). On Windows, this uses Powershell or Git Bash (that is installed with git). On Mac/Linux, this is in the terminal.

If you ever are unsure of what to do or how to do something, please just ask.

### Working at Home on the Repo

###### Starting
Find a directory to work in. Enter on the command line:```git clone https://github.com/cartermyers/URSell.git```.
This will create a directory with all of the current files on github.

###### Saving (Committing)
To save any changes you've made on your computer (such as adding files, modifying files), use ```git add <files>``` and then ```git commit -m "meaningful meassge"```. This change is only visible on your computer, and no files have been uploaded to Github yet. Commits should be used for when a significant (but not necessarily big) change has occurred. This could be something like adding a function, or completing a specific part of code. In short, commits are like saving the files in git.

<b>CAUTION:</b> be sure you are on the right branch (see below) before making any commits.

###### Experimenting (new branch)
New branches are used whenever new features need to be added, or bugs need to be fixed, or any big changes happen that may break the code. Basically, a branch is a copy of the current repository that you can play around with and make changes without messing around with the code on the original branch (in most cases, ```master```).
To create a new branch, run ```git branch <branch_name>```. To see all of the branches currently made, run ```git branch```. To switch over to a branch to use it, run ```git checkout <branch_name>```. You must be on a branch (i.e. you must checkout to that branch) to make any changes to it or to commit to it.

<b>NOTE:</b> this all only takes place on your own machine. To upload a specific branch to github, run ```git push origin <branch_name>```. This will create a new branch on github (if there isn't one already), and it's easy for everyone to see/use/add to the changes you've made without breaking any of the main code.

###### Getting Changes
To get changes from the website, simply run ```git pull``` which is basically like recloning the repository.
If you have made any changes on your own, however, this made lead to <b>merge conflicts</b>. Because merge conflicts can be confusing or hard to deal with, just ask someone for help.

###### Sending Changes
To upload changes you've made on your computer, use ```git push origin <branch>``` where <branch> is
the branch you have committed the changes to. This changes the files on Github for everyone.

### Contributing to Github

Here are some (proposed) standards we should maintain while using Github.

1. The `master` branch will always be functional. Do not modify this branch unless you are sure it will not break it.

2. For any new features, bug fixes, etc. please open a new branch (one per feature/bug/etc.).
Here is the process for contributing:

    1. Create a new branch with a meaningful name (like `log_in` or `fix_add_post`).

    EX: ```git branch log_in``` or ```git checkout log_in```

    2. Add commits to the branch as necessary (i.e. "save" when done minor changes)

    EX: (on branch ```log_in```) ```git add <files>``` then ```git commit -m "Add js login validation"```

    3. When the new feature is complete, open a Pull Request (PR) to merge it back on the `master` branch.

      EX: ```git push origin log_in``` then go online to Github and select "Open a pull request"

    4. Have at least one other group member review the changes and test them. This group member will comment that they've done so.

    5. Merge the PR. If there are merge conflicts and you don't know how to resolve them, leave a comment and we'll look at them together as a group.

Again, these standards are just a suggestion to maintain and add to our code cleanly and orderly. If there's any process you guys don't like or think it's unnecessary, bring it up and the group can talk about it.
