# St.-Johns-Sorting
## To User
Here are the steps to use this program:

1. Download Python 3 from [here](https://www.python.org/downloads/) by selecting the latest Python 3 download (3.?.?) for your operating system. This should be at the top of your screen. Follow all installation instructions.

2. Click on the green Clone or Download button above here and click Download ZIP. Open the ZIP file in Finder/Windows Explorer/etc.

3. Open the command line. (On a Mac, this is called Terminal, on a Windows, it is called Command Prompt.)

4. Run these programs in the shell. Make sure to type them exactly as written, then press enter:

   ~~~~
   cd Downloads/St.-Johns-Sorting-Master
   python3
   exec(open("main.py").read())
   sort_preceptorials()
   ~~~~
   
5. Follow instructions in program.

## To Developers
Follow step 1 above to download Python 3.

Are you AceAttorneyMaster111 or Lionclaw49? If not, click Fork at the top of the page and follow instructions.

Click the green Clone or Download button, copy the link given, follow Step 3 above, and run `git clone <link you copied> <folder you want it to be in>`.
#### How To Use Git
1. Make changes to files
2. Run `git add <file you edited>`
   * If you deleted a file connected to Git, run `git rm <file deleted>`.
   * Instead of moving or renaming a file normally, use `git mv <file> <destination or new name>`
3. If you are done changing files, run `git commit -m "<some message for what you changed>"` and `git push`. This will bring all your changes online.
4. Periodically, make sure you `git pull` to be sure you are updated with all changes other people have made.

If you are not AceAttorneyMaster111 or Lionclaw49, click Pull Request on the main Github screen and write a message. One of us will review your code and choose whether to accept it into the main code. Also, periodically make sure you click Compare (the button next to Pull Request) for the same reason as #4.

#### Our Spec
> Preceptorial Python Project: 
> Every year in the fall, all Juniors and Seniors at St John's College are sorted into "preceptorials"--small groups of varying numbers (usually 3-12) working with a Tutor on a single book or focused topic. Students list at least three preferences for which preceptorial they'd like to be in. They are not supposed to rank their preferences, but may indicate one or two that they'd more strongly prefer. (If it turns out to be easier, we could change the system and have them give us their preferences in ranked order, and then set parameters so that we try to put as many students in their first choice, then their second, etc.)
> Sorting:
> I need a small, well-written program that can run on a variety of computer systems, preferably in Python, that will take a list of students and their preferences, and match them up with a single preceptorial each. The list of students, their preferences, and available preceptorials will be available in database form, so can be exported or copy/pasted into a list parameter within a program; or the program can be designed to request this from a user or to draw it from a database. 
> Rules:
> All students must be sorted into one and only one section.
> There can be from 3-12 students in each section.
> Students may mark a preference as strongly preferred, and we would prefer to sort these first so that they get their strong preference.
> We would prefer to have a fairly even distribution of men and women in each section, but perhaps this could be done by me by hand after the program has generated a few solutions.
> 
> 
> Example:
> There are 150 students and there are 15 preceptorial sections. Each student chooses 3 preferences (ideally there will be a way to account for people who star one of their preferences to indicated they'd strongly prefer that preceptorial--we would strongly prefer to sort them into the preceptorials they strongly prefer: maybe after using a line of code to import the list, a second line of code could be used to run through this list and identify the strongly preferred, and to sort these first). Each student must end up in only one preceptorial, ideally there will be around 10 students in each preceptorial, but this can range from 3-12 students in each).
> 
> Practice example (if you can get this smaller example to work, the bigger, real example should work too; if this works, maybe try adding strongly preferred marks to some of the preferences, and seeing if you can get that to work too):
> There are 15 students, who each choose three preferred classes from a list of five offerings. All students must be placed in one of their preferred classes, aiming for an even distribution of 3 students per class--but crucially, this can vary: there can be 2-5 students per class (that is, your odds that there is a solution to the problem are much greater). There will probably be multiple solutions, so if you might want to add some random method of sorting people. For example, take the original list of students in alphabetical order, then use a command to randomize that list (so that it isn't always the case that the students that come first alphabetically always get sorted into their preferences first.).
> 
> Classes:
> Robotics (Ro)
> Programming (Pr)
> Linux (L)
> iOS/Android (iA)
> Raspberry Pi (RP)
> Students:
> Anna: RP, Ro, Pr
> Bob: iA, L, Pr
> Chris: L, RP, Ro
> Dave: RP, L, Pr
> Ezekiel: L, iA, Pr
> Felicity: Pr, RP, iA
> George: Ro, Pr, L
> Hugh: RP, iA, L
> Iona: iA, L, Pr
> Jenna: RP, iA, L
> Kyle: L, Pr, Ro
> Lyle: RP, L, Ro
> Marie: RP, iA, L
> Ned: L, Pr, iA
> Orlando: Pr, Ro, RP
