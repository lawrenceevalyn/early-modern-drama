# What this Program Does

This program will count all the <w> tags (for words) that are within <l>, <lg>, or <p> tags (for line, linegroup, or paragraphs) and will associate those counts with the who="" information of the <sp> speaker tag within which those words appear. It goes through the whole "corpus" folder and produces one row of spreadsheet data per play, with speakers sorted from most words to fewest.

# How to Run this Program

These instructions assume that you are unfamiliar with GitHub and running software from the command line; I have attempted to clarify each of the small steps which are often taken for granted in technical explanations, but if I have left anything out that confuses you, please let me know so I can describe more fully.

## 1. Download this whole repository to your computer.

You don't need to clone the repository, since you won't be editing the code, just running it. Download the ZIP and unzip it, and you should see a collection of files just like on this website!

## 2. Get into the command line

[This tutorial](https://www.davidbaumgold.com/tutorials/command-line/) has more information -- once you've found and opened your command line interface, you need to navigate to 'be' in the same place as the folder containing all of these program files.

On my computer, that means typing the following:

cd ~/Desktop/early-modern-drama

You can type "ls" to list what's around you, and if it's the same files you see on this website, you're in the right place.

## 3. Run the "RUNME.py" program

Try the following command:

python RUNME.py

If it started spewing TCP numbers at you, the program is running! It takes about eight minutes, and will print all 510 TCP numbers so you know it's still running and roughly where you are at the process. At the end, it will print some information about what it did, and error messages if anything went wrong (if it did, email me!)

If none of that happened, you probably need to [install Python](https://www.python.org/download/releases/2.7/)

## 4. The program does all the work!

You don't have to specify your input -- the program will automatically run on everything it finds in the "corpus" folder. (So you can change the stuff in the corpus folder as much as you like to see how it changes your counts!) It will automatically create a file called output_corpus.csv and put all the data there. If there's already a file called output_corpus.csv, it will overwrite that one, so be careful!

Have fun!

