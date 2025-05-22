import e3series
import e3series.tools as e3Tools

# Start up a new instance of E3.series and load the cooling water pump project
e3pid = e3Tools.start(["/formboard", "/language=44", "C:\\Users\\Public\\Documents\\Zuken\\E3.series_2025\\data\\Pumpe\\Cooling water pump complete.e3s"]).pid
e3 = e3series.Application(e3pid)
job = e3.CreateJobObject()
con =job.CreateConnectionObject()
pin1 = job.CreatePinObject()
pin2 = job.CreatePinObject()
dev1 = job.CreateDeviceObject()
dev2 = job.CreateDeviceObject()

e3.ClearOutputWindow()
conIds = job.GetConnectionIds()[1]

for conId in conIds:
    con.SetId(conId)

    if con.IsValid():
        pinIds = con.GetPinIds()[1]
        pin1.SetId(pinIds[0])
        dev1.SetId(pinIds[0])

        pin2.SetId(pinIds[1])
        dev2.SetId(pinIds[1])
        
        e3.PutInfo(0, f"From: {dev1.GetName()}:{pin1.GetName()} To: {dev2.GetName()}:{pin2.GetName()}", con.GetId())    # Print device and pin names for each connection with a jumpable link
    else:
        job.SetHighlightColour(13)
        e3.PutInfo(0, "Ambigiuous connection", con.GetId())