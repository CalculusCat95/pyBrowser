import urllib.request

print(""""Welcome to PyBrowser 1.0! \n This glorious wonder of technology allows you to load a 
Python application from the web and execute it on your computer. It functions similarly to a standard web browser,
but allows you to run real apps.""")

while True:

    url = input("Enter a URL to load, or type 'library' to view a library of presaved apps: \n")

    if url == "library":
        reply = input("Choose a URL from our preselected library: \n" 
                    "- press 1 for a semi-functional choose your own adventure story. \n"
                    "- press 2 for a test window application. \n"
                    )

        if reply == '1':
            url = "https://pybrowser.jons2.repl.co/Server/test%20apps/served.py"

        elif reply == '2':
            url = "https://pybrowser.jons2.repl.co/Server/test%20apps/tktest.py"

    response = urllib.request.urlopen(url)
    exec(response.read())
