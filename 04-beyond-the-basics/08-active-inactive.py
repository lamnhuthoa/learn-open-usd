from pxr import Usd

# Open the USD stage from the specified file
file_path = 'assets/30-active-inactive.usda'
stage = Usd.Stage.Open(file_path)

# Iterate through all the prims on the stage
# Print the state of the stage before deactivation
print("Stage contents BEFORE deactivating:")
for prim in stage.Traverse():
    print(prim.GetPath())
    
# Get the "/World/Box" prim and deactivate it
box = stage.GetPrimAtPath("/World/Box")
# Passing in Flase to SetActivate() will set the prim as Inactive and passing in True will set it as Active
box.SetActive(False)

print("\n\nStage contents AFTER deactivating:")
for prim in stage.Traverse():
    print(prim.GetPath())
    
"""
    Stage contents BEFORE deactivating:
    /World
    /World/Box
    /World/Box/Geometry
    /World/Box/Geometry/Cube
    /World/Box/Materials
    /World/Box/Materials/BoxMat
    /World/Environment
    /World/Environment/SkyLight


    Stage contents AFTER deactivating:
    /World
    /World/Environment
    /World/Environment/SkyLight
"""