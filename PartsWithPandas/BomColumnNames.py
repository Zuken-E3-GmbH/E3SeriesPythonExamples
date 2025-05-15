def get_bom_default_column_names() -> dict:
    '''
    Returns a dictionary giving the names of the default colums in a bom returned by JobInterface.GetBomPartList()
    Not all columns are included in all versions of the BOM.
    '''
    return { 
            0: "GID",
            1: "Key Attribute",
            2: "Designation",
            3: "Assignment",
            4: "Location",
            5: "Owner GID",
            6: "Owner Type",
            7: "Device Type",
            8: "BOM Type",
            9: "Component GID",
            10: "Component Name",
            11: "Component Version",
            12: "Sheet GID",
            13: "Sheet Grid",
            14: "Parent Structure Node GID",
            15: "Quantity",
            16: "Has option or variant",
            17: "Option combination expression",
            18: "Option combination expression GID",
            19: "Option variant expression",
            20: "Option variant expression GID",
            21: "Length",
            22: "Only exists in variant",
            23: "Only exists in variant GID",
            24: "Does not exist in variant",
            25: "Does not exist in variant GID",
            26: "Bom type 2" 
        }