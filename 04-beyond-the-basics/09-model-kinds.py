# Example 1: Traversal with Model Kinds
from pxr import Usd, UsdGeom, Kind, Gf

# Create a stage and model root
file_path = 'assets/31-model-kinds-component.usda'
stage = Usd.Stage.CreateNew(file_path)
world_xform = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world_xform.GetPrim())

# Make /World a group so children can be models
Usd.ModelAPI(world_xform.GetPrim()).SetKind(Kind.Tokens.group)

# Non-model branch: Markers (utility geometry, no kind)
markers = UsdGeom.Scope.Define(stage, world_xform.GetPath().AppendChild("Markers"))

points = {
    "PointA": Gf.Vec3d(-3, 0, -3), "PointB": Gf.Vec3d(-3, 0, 3),
    "PointC": Gf.Vec3d(3, 0, -3), "PointD": Gf.Vec3d(3, 0, 3)
    }
for name, pos in points.items():
    cone = UsdGeom.Cone.Define(stage, markers.GetPath().AppendChild(name))
    UsdGeom.XformCommonAPI(cone).SetTranslate(pos)
    cone.CreateDisplayColorPrimvar().Set([Gf.Vec3f(1.0, 0.85, 0.2)])

# Model branch: a Component we want to place as a unit
component = UsdGeom.Xform.Define(stage, world_xform.GetPath().AppendChild("Component"))
Usd.ModelAPI(component.GetPrim()).SetKind(Kind.Tokens.component)
body = UsdGeom.Cube.Define(stage, component.GetPath().AppendChild("Body"))
body.CreateDisplayColorPrimvar().Set([(0.25, 0.55, 0.85)])
UsdGeom.XformCommonAPI(body).SetScale((3.0, 1.0, 3.0))

# Model-only traversal: affect models, ignore markers
for prim in Usd.PrimRange(stage.GetPseudoRoot(), predicate=Usd.PrimIsModel):
    if prim.IsComponent():
        xformable = UsdGeom.Xformable(prim)
        if xformable:
            UsdGeom.XformCommonAPI(xformable).SetTranslate((0.0, 2.0, 0.0))

# Show which prims were considered models
model_paths = [p.GetPath().pathString for p in Usd.PrimRange(stage.GetPseudoRoot(), predicate=Usd.PrimIsModel)]
print("Model prims seen by traversal:", model_paths)

stage.Save()