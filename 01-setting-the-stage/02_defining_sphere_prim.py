# Activity 2: Defining a Cube in the Stage
from pxr import Usd, UsdGeom

file_path = 'assets/02-defining-sphere-prim.usda'

stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define a prim of type `Sphere` at path `/sphere`:
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, "/sphere")
sphere.CreateRadiusAttr().Set(2)

# Save the stage:
stage.Save()