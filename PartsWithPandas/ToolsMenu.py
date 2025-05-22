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
import pandas as pd
from tkinter import filedialog
import BomColumnNames

def export_bom() -> None:
    runningE3s = e3series.tools.get_running_e3s()
    if( len(runningE3s) > 1 or len(runningE3s) == 0):           # As the tool menu currently cannot pass information to the script which e3 to use we make sure 
        exit(1)                                                 # only one instance is running and therefore it is clear which instance to use
    e3 = e3series.Application()                                 # Connect to that instance
    job = e3.CreateJobObject()
    if(job.GetId()==0):
        exit(1)                                                 # If no project is open we exit the script  
    bom = job.GetBomPartList("", "4.1", 0, "", "", "", [""])[1] # Get the BOM from E3.series
    pandaBom = pd.DataFrame(bom)                                # Create a pandas DataFrame from the BOM
    pandaBom.rename(columns=BomColumnNames.get_bom_default_column_names(), inplace=True) # Rename the columns
    pandaBom = pandaBom[["Designation", "Assignment", "Location", "Component Name", "Device Type", "Quantity"]] # Definition which columns should be included
    destination = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]) # Ask the user for a destination file
    pandaBom.to_excel(destination)

if __name__ == "__main__":
    export_bom()