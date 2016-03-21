# Math651

Let's document how I made this repository on Github.

1. I created a folder on my laptop with all the files and folders I wanted to include.
2. I opened a terminal window, and cd'd to the new folder
3. In the command line, I did this sequence of commands:
 - git init
 - git add *
 - git commit -m "First commit with all files"
 - git remote add origin https://github.com/mlamoureux/Math651.git
 - git push -u origin master
 - 
 
That's it. Now the repository exists up on my github site. 


-----------------
To copy that repository on Github onto your own laptop, open a terminal window in your laptop
and cd to the folder or directory where you want to put the copy of the repository.
Now typ ein this command:

   git clone https://github.com/mlamoureux/Math651.git
   
This will copy all the stuff in the repository onto your laptop.

You can make whatever changes you want on your laptop. But, if you want to push this back to the repository on Github, do this:

   git add *
   
   git commit -m "adding the .pdf file, I hope"
   
   git push origin master
   .

----------------
Now, if someone has made changes to the master repository on Github, you can pull those onto your laptop as follows:

-- on your laptop, cd into the directory where all your files are (the ones that came down in the clone command). Then type:

  git pull
  
That is it. This brings in all the new stuff onto your laptop. 

All this information is available in a really nice instruction set here: http://rogerdudler.github.io/git-guide/
I recommend reading all of it. 
