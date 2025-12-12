# Example 2: Non-destructive over edits and class inherit
from pxr import Usd, UsdGeom, Sdf

new_file_path = 'assets/23-specifiers-over.usda'
base_file_path = '22-specifiers.usda' # path relative to the new file

stage = Usd.Stage.CreateNew(new_file_path)

# Base is weaker than the root layer (root opinions are strongest)
stage.GetRootLayer().subLayerPaths = [base_file_path]

prim_path = "/World/Box"

# Author an override for the same prim
stage.OverridePrim(prim_path)

# Get the cube and change its size
box_prim_cube = UsdGeom.Cube.Get(stage, prim_path)
box_prim_cube.GetSizeAttr().Set(4.0)

# Compose the class onto the box using an inherit arc
box_prim_cube.GetPrim().GetInherits().AddInherit(Sdf.Path("/World/_Look/_green"))

# SdfPrimSpec handles, ordered strong to weak
print("Box Prim Cube Stack:", box_prim_cube.GetPrim().GetPrimStack())
for prim_spec in box_prim_cube.GetPrim().GetPrimStack():
    print(" - layer:", prim_spec.layer.identifier.split('/')[-1], "specifier:", prim_spec.specifier)

stage.Save()