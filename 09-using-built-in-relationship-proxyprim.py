from pxr import Usd, UsdGeom

file_path = 'assets/09-using-built-in-relationship-proxyprim.usda'
stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

# Define a "high cost" Sphere Prim under the World Xform
high: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("HiRes"))

# Define a "low cost" Cube Prim under World Xform
low: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Proxy"))

UsdGeom.Imageable(high).GetPurposeAttr().Set("render")
UsdGeom.Imageable(low).GetPurposeAttr().Set("proxy")

# Author the proxy link on the render Prim
UsdGeom.Imageable(high).GetProxyPrimRel().SetTargets([low.GetPath()])

# Tools that honor proxyPrim should draw the proxy in preview
draw_prim = UsdGeom.Imageable(high).ComputeProxyPrim() # Returns Usd.Prim
print("Preview should draw:", str(draw_prim[0].GetPath() if draw_prim else high.GetPath()))

stage.Save()