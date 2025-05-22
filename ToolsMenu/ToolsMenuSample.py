# This script is supposed to be added to the E3.series Tools menu
# To do so follow these steps:
#   1. Click on "Tools" in the menu bar
#   2. Select Customize
#   3. Change to the tab "Add-ons"
#   4. Add a new Add-on by clicking on the small button on the top right
#   5. Enter a name
#   6. Select the runtime to run the script, most probable: "C:\Users\<User>\AppData\Local\Programs\Python\Python311\pythonw.exe" (use pythonW instead of python to suppress the cmd window)
#   7. Add the name and path of your script as Argument
#   8. Change to Commands tab
#   9. Choose the category "Add-ons"
#  10. Drag&Drop the new Command to wherever you want it
import e3series
import e3series.tools
import sys

runningE3s = e3series.tools.get_running_e3s()
if( len(runningE3s) > 1 or len(runningE3s) == 0):           # As the tools menu currently cannot pass information to the script which e3 to use we make sure 
    exit(1)                                                 # only one instance is running and therefore it is clear which instance to use
e3 = e3series.Application()                                 # Connect to that instance
sys.stdout = e3series.tools.E3seriesOutput(e3, sys.stdout)  # Redirect all print commands to E3.series
print("Hello from python!")