# Define a Scope
from pxr import Usd, UsdGeom, Gf

file_path = 'assets/17-scopes.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# World container (transformable)
world = UsdGeom.Xform.Define(stage, "/World")

num_a_prims = 2
num_b_prims = 2


# Two organizational scopes (non-transformable grouping prims)
a_scope = UsdGeom.Scope.Define(stage, world.GetPath().AppendPath("A_Scope"))
b_scope = UsdGeom.Scope.Define(stage, world.GetPath().AppendPath("B_Scope"))

# Populate the scopes with some geometry
for a in range(num_a_prims):
    sphere = UsdGeom.Sphere.Define(stage, a_scope.GetPath().AppendPath(f"A_Sphere_{a}"))
    UsdGeom.XformCommonAPI(sphere).SetTranslate(Gf.Vec3d(a * 2.5, 0, 0))
    
for b in range(num_b_prims):
    cube = UsdGeom.Cube.Define(stage, b_scope.GetPath().AppendPath(f"B_Cube_{b}"))
    UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(b * 2.5, -2.5, 0))
    
# Deactivate the A_Scope
a_scope.GetPrim().SetActive(False)

stage.Save()