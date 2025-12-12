"""
    # Used to define a new Xform prim at a specified path on a given stage
    UsdGeom.Xform.Define(stage, path)

    # Retrieves the order of transformation operations, which is crucial for understanding how multiple transformations are combined. Different orders can yield different results, so understanding XformOpOrder is important. 
    xform.GetXformOpOrderAttr()
        
    # Adds a new transform operation to the Xform prim, such as translation or rotation, with specified value   
    xform.AddXformOp(opType, value)
"""

# UsdGeom and Xform
from pxr import Usd, UsdGeom, Gf

# Create a new Usd stage with root layer named "xform_prim.usda":
file_path = 'assets/18-xform.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define a new Xform prim at path '/World':
world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, '/World')

# Save changes to the current stage to its root layer
stage.Save()
print(stage.ExportToString(addSourceFileComment=False))
"""
    #usda 1.0

    def Xform "World"
    {
    }
"""