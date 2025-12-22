from pxr import Usd, UsdGeom, Gf

file_path = 'assets/06-getting-attribute-values.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

# Get the attributes of the cube prim
cube_attrs = cube.GetPrim().GetAttributes()
for attr in cube_attrs:
    print(attr)

# Get the size, display color, and extent attributes of the cube
cube_size: Usd.Attribute = cube.GetSizeAttr()
cube_displaycolor: Usd.Attribute = cube.GetDisplayColorAttr()
cube_extent: Usd.Attribute = cube.GetExtentAttr()

print(f"Size: {cube_size.Get()}")
print(f"Display Color: {cube_displaycolor.Get()}")
print(f"Extent: {cube_extent.Get()}")

'''
Usd.Prim(</World/Cube>).GetAttribute('doubleSided')
Usd.Prim(</World/Cube>).GetAttribute('extent')
Usd.Prim(</World/Cube>).GetAttribute('orientation')
Usd.Prim(</World/Cube>).GetAttribute('primvars:displayColor')
Usd.Prim(</World/Cube>).GetAttribute('primvars:displayOpacity')
Usd.Prim(</World/Cube>).GetAttribute('purpose')
Usd.Prim(</World/Cube>).GetAttribute('size')
Usd.Prim(</World/Cube>).GetAttribute('visibility')
Usd.Prim(</World/Cube>).GetAttribute('xformOp:translate')
Usd.Prim(</World/Cube>).GetAttribute('xformOpOrder')
Size: 2.0
Display Color: None
Extent: [(-1, -1, -1), (1, 1, 1)]
'''

stage.Save()