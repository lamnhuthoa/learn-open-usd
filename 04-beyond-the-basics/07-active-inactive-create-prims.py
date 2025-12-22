# Example 1: Setting prims as active/inactive

from pxr import Usd, UsdGeom, UsdLux

# Create a new USD stage with the specified file path
file_path = 'assets/30-active-inactive.usda'
stage = Usd.Stage.CreateNew(file_path)

# Create the prim hierarchy
# /World
world = UsdGeom.Xform.Define(stage, "/World")

# /World/Box
box = UsdGeom.Xform.Define(stage, "/World/Box")

# /World/Box/Geometry
geometry = UsdGeom.Xform.Define(stage, "/World/Box/Geometry")

# /World/Box/Geometry/Cube
cube = UsdGeom.Cube.Define(stage, "/World/Box/Geometry/Cube")

# /World/Box/Materials
materials = UsdGeom.Scope.Define(stage, "/World/Box/Materials")

# /World/Box/Materials/BoxMat
box_mat = UsdGeom.Scope.Define(stage, "/World/Box/Materials/BoxMat")

# /World/Environment
environment = UsdGeom.Xform.Define(stage, "/World/Environment")

# /World/Environment/SkyLight
sky_light = UsdLux.DomeLight.Define(stage, "/World/Environment/SkyLight")

# Set the default prim to /World
stage.SetDefaultPrim(world.GetPrim())

# Save the stage
stage.Save()

print(f"Created USD file: {file_path}")
print(f"Default prim: {stage.GetDefaultPrim().GetPath()}")
print("\nPrim hierarchy:")
for prim in stage.Traverse():
    print(f"  {prim.GetPath()}")
