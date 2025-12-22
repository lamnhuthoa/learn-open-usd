# Example 1: Traversing Through the Stage
from pxr import Usd, UsdGeom

# Open the USD Stage from the specified file
stage: Usd.Stage = Usd.Stage.Open('assets/32-stage-traversal.usda')

# Traverse and print the paths for the visited prims
for prim in stage.Traverse():
    print(prim.GetPath())
    

print("\n")

# Example 2: Traversing USD Content for Specific Prim Types
scope_count = 0
xform_count = 0
# Traverse through each prim in the stage
for prim in stage.Traverse():
    # Check if the prim is of type Scope
    if UsdGeom.Scope(prim):
        scope_count += 1
        print("Scope Type: ", prim.GetName())
    # Check if the prim is of type Xform
    elif UsdGeom.Xform(prim):
        xform_count += 1
        print("Xform Type: ", prim.GetName())

print("Number of Scope prims: ", scope_count)
print("Number of Xform prims: ", xform_count)

print("\n")

# Example 3: Traversing through the Children of a Prim

# get te default prim of the stage (/World in this case)
default_prim: Usd.Prim = stage.GetDefaultPrim()

# Iterate through all children of the default prim
for child in default_prim.GetAllChildren():
    # Print the path of each child prim
    print(child.GetPath())
    
    
print("\n")

# Example 4: Traversing Using Usd.PrimRange
prim_range = Usd.PrimRange(stage.GetPrimAtPath("/World/Box"))
for prim in prim_range:
    print(prim.GetPath())