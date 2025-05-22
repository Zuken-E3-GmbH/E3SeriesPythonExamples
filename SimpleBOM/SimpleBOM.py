# Python example implementing the assignment of the AE-Training 2025 presentation on creating a BOM using vbs
import e3series
from natsort import natsorted

class Material: # Class to hold the material information, could be axpanded with further information
    def __init__(self, cmp, dev):
        self.component = cmp
        self.device = dev

    def __str__(self):
        return f"{self.device}\t{self.component}"

def CreateMaterialfromBomPart(part):
    return Material(part[10], part[2])

def main():
    e3 = e3series.Application() # Connect to a running E3.series
    job = e3.CreateJobObject()

    bom = job.GetBomPartList("", "4.1",  0, "", "", "", "")[1]
    parts = {}                  # Dictionary which holds al parts and automatically orders them by component name
    for part in bom:            # Add all parts to the dictionary
        material = CreateMaterialfromBomPart(part)
        if material.component not in parts.keys():
            parts[material.component] = []
        parts[material.component].append(material)

    for k in natsorted(parts.keys()):   # Iterate over all keys (componentt names) sorted in a natural way)
        print(f"{len(parts[k])}\t{parts[k][0].component}", end="\t")
        sep  = ""
        for d in parts[k]:
            print(f"{sep} {d.device}", end="")
            sep = ","           # after the first element additional elements get a leading comma
        print()

if __name__ == "__main__":
    main()