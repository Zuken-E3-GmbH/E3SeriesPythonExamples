import e3series
import e3series.tools as e3Tools

def add_new_database():
    running = e3Tools.get_running_e3s()
    if len(running) != 1:       # As this is supposed to be added to the tools menu the E3.series instance must be unique
        exit(1)
    e3 = e3series.Application()
    e3.Database
