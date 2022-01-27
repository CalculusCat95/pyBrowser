## imports system module, which gives you access to system commands (like stuff you can do in the terminal, basically
import sys 
## this changes where this file is being run (I think) so that it can see the server file to import it
sys.path.append("Server")
## this basically just brings the code from the server file and runs it. we have to have a main.py file (because replit), but we want our server file, so yeah.
import server
