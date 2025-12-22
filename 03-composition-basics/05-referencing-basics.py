"""
    # Return a UsdReferences object for managing references on a prim
    prim.GetReferences()

    # Add a reference to the specified asset and prim path
    references.AddReference(assetPath, primPath) 

    # Remove all references from a prim
    references.ClearReferences()
"""

# Example 1: Adding a Reference
# References are a composition arc. References are like links to separate pieces of a project, 
# allowing to include and reuse these pieces without copying them.

from pxr import Usd, UsdGeom, Gf

# Create a new wstage and define a cube
file_path = 'assets/24-01-referencing-basics-cube.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, '/Cube')
stage.SetDefaultPrim(cube.GetPrim())
stage.Save()

# Create a second file path and stage, define a world  and a sphere
second_file_path  = 'assets/24-02-referencing-basics-shapes.usda'
second_stage: Usd.Stage = Usd.Stage.CreateNew(second_file_path)
world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(second_stage, '/WorldTransform')
UsdGeom.Sphere.Define(second_stage, world_xform.GetPath().AppendPath("Sphere"))

# Define a reference prim and set its translation
reference_prim = second_stage.DefinePrim(world_xform.GetPath().AppendPath("Cube_Ref"))

# Add a reference to the "cube.usda" file:
reference_prim.GetReferences().AddReference("./24-01-referencing-basics-cube.usda")
# Position the cube
UsdGeom.XformCommonAPI(reference_prim).SetTranslate(Gf.Vec3d(5, 0, 0))

second_stage.Save()