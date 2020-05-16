# Week 2: Notes

- Not installing sublime text
  - I've used [Atom](https://atom.io) for about 3yrs now and enjoy using it
  - Would rather only have to use one text editor for everything I do
  - Feel I'll work best in an environment I'm familiar with


### Anaconda
- Am very familiar with Python, but have never worked in R
  - Only in programming assignments
- Installed Anaconda via Homebrew
  - ```brew cask install anaconda```
  - Navigator installed and opened fine
    - Do not have all of the application shown in screenshot --> can you choose to add more applications later?
  - Apparently it didn't install correctly elsewhere --> ```-bash: conda: command not found``` when I try to check the version
    - I moved on to check Python --> I have a hard set version of Python2 installed because my first year CS prof hated Python3
    - Reinstalled all versions of python via Homebrew ```brew install python``` and ensured I have Python3
  - Returned to problem with Anaconda installed
    - Turns out I just needed to navigate to directory of install and agree to the terms and conditions


### Wget
- Had wget installed from data science workshop I've attended --> instead made sure wget was up to date with ```brew upgrade wget```
- Basic usage
  - Initial request took seconds
  - Second request with flags took 16m 56s
    - How could this process potentially be spead up without overwhelming the server?
    - What would happen if bandwidth limits are loosened?
- Wget with list of URLs
  - Made new directory ```wget-LAGfonds```
  - Navigated to directory in command line
  - Created ```urls.txt``` within that directory and used vim to add urls to file
- Using python to generate list
  - I am anticipating a for loop
  - Named directory ```wget-war-diaries``` for consistency
  - This request only took 5m 20s to load 80 jpg files


### APIs
- Getting material out of an API
  - I have never put metadata in a python programming
    - In programs like this, what should be commented and what should be metadata?
- I like extracting data with python, it's very nice step-by-step programming
- **Challenge for self if time permits**: modify code to output in readable format


### OCR
- Excited to work with OCR and learn R
- R Studio will not install --> cannot open application due to certain elements missing or not installing incorrectly according to pop up
  - Think this is (another) issue with my Anaconda install
  - Wiped Anaconda from system using ```anaconda-clean``` then ```rm -rf ~/anaconda3``` and ```rm -rf ~/opt```
  - Reinstalled but RStudio still would not launch so I tried installing from command line via ```conda install -c r rstudio ``` rather than using Anaconda-Navigator
  - Still did not install but warning appeared stating ```Unable to create environments file. Path not writable to environment location.```
  - Google says this a common issue with Anaconda Navigator not installing with the correct edition of Python/R
    - SOLUTION: Created new environment manually with correct python environment and R --> correct version of RStudio installed and was able to launch
- Installing packages within RStudio
  - Packages were not installing because of error ```Configuration failed because poppler-cpp was not found.```
  - It was prompting me to manually install each dependancy for each package manually via Homebrew
  - SOLUTION: Anaconda's RStudio is abandoned --> too many bugs, least complex solution is to just directly download RStudio
- Single Image OCR
  - Went smoothly
  - Getting use to working in IDE --> need to find a workflow that works best for me
  - Multiple panes are overwhelming
- Multi Image OCR
  - Problem at ```lapply``` step
    - Runs but then expects more input
    - No error
    - SOLVED: Function was missing closing brackets

### Bonus Activity: Speech to text
- Kras tutorial for accessing google API out of date which led to some confusion
  - No need to create free tier account if you already have a google account
  - Then good until 6th step --> you only have the option to select "Service Account"
  - You start at a page where you name the service account + generate key
  - Next page is selecting role --> there is currently no option to create a JSON file here
  - Next page at bottom is the option to create a key --> have to select button to create key and then side pop-up shows with option to select JSON download file that autosaves to computer
- Git repo does not clone with a /parts folder --> when I initially tried to break up audio file I got the error ```Could not write header for output file #0 (incorrect codec parameters ?): No such file or directory```
  - Created folder /parts then tried again and it worked
- The final step using slow.py to transcribe threw an extensive error that began with ```wave.Error: file does not start with RIFF id``` and finalized ```ValueError: Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format```
  - Confirmed .wav file was correct format through ```file [filename]```
  - Files were not corrupted
  - Changing version of Python environment did not help
  - Found thread by Prof. Graham that proposed possible python install conflicts then reinstallation of ffmpeg --> I couldn't find any conflicts thus reinstalling ffmpeg made no difference
  - CONCLUSION: I have surrendered to this activity, I could not find a productive solution that made it work :(
    - Will try again later on my own time
