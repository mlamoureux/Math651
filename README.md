# Math651_3
Third try is the charm.

This is a third attempt to figure out the workflow for Git and Github.
Three words to look up in the glossary are Branch, Clone, and Fork.

Note that the master files all live "in the cloud" on the Github server, that we access through the web.
When collaborating, if you want to make changes, you should create a "branch" which is like a copy of the files,
that you can play with and change at will. (Without affecting the master files). Then you make a "pull" request
to the system, so the owner guy (HEAD?) can decide whether to merge your changes from your branch back into the master files.

We also want to work locally (on our own computer) on these files. Create a branch, then clone it to get files onto your computer disk. Do all your editting on your own computer, then "sync" your files to get your branch "on the cloud" updated. Now your branch is updated, but no one else knows about it. So you make a "pull" request, to ask the owner to update everything onto the master files.

I don't see why you can't use the "cloud" repository directly from the computer. You can make little edits from the browser (on github.com) but that seems pretty limited. 

Anyhow, let's try this out. 

-----------------
Well, I'm not sure I understood that. I cloned the GitHub repository onto my laptop using the command:

   git clone https://github.com/mlamoureux/Math651_3.git
   
Then I added a .pdf file into the new folder that was created in my laptop. 
To get that loaded onto the remote server, I had to issue three commands on the laptop

   git add *
   
   git commit -m "adding the .pdf file, I hope"
   
   git push origin master
   
It took a surprising long time to complete, but eventually it did complete, and now the .pdf file is on the remote server.

----------------
Now, how do I get files from the server onto my local copy?

-- first, I will create a simple text file on the remote server using github.com (called ATextFile). Commit it, of course. 

-- then I enter one command on the laptop, to move the new stuff onto the laptop. The command is

  git pull
  
That was it. It brought in the new file, and also updated the README file because I was editting it on the remote server.

All this information is available in a really nice instruction set here: http://rogerdudler.github.io/git-guide/
I recommend reading all of it. 
