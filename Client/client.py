## imports the requests module, which we use to get the files from websites.
import requests 

## main function, we'll use this to start the program when we package it into an installer
def main():  

## welcome message
    print("""Welcome to PyBrowser 1.0! \n This glorious wonder of technology allows you to load a 
    Python application from the web and execute it on your computer. It functions similarly to a standard web browser,
    but allows you to run real apps.""")
## loops forever, so that multiple programs can be loaded
    while True:

        ## gets the url to load, or loads the library.
        url = input("Enter a URL to load, or type 'library' to view a library of presaved apps: \n")

## checks if we're using the library
        if url == "library":
## if so, asks which program to use
            reply = input("Choose a URL from our preselected library: \n" 
                        "- press 1 for a semi-functional choose your own adventure story. \n"
                        )
## checks which program to use
            if reply == '1':
                url = "https://pybrowser.jons2.repl.co/served.py"
## the 'try' thing prevents it from stopping if there's an error
            try:
## gets the python file from the url
                r = requests.get(url, allow_redirects=True)
## runs the file with the python interpreter
                exec(r.content)
## executes this if there's an error
            except:
## error message
                print("There was an error. Please make sure you entered the correct URL and the file being accessed does not contain an error")
## runs main function (for testing), the start menu shortcut will call it for us when it's installed, so this part won't matter
main()
