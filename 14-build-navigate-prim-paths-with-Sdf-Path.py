from pxr import Usd, UsdGeom, Sdf

stage = Usd.Stage.CreateNew('assets/14-build-navigate-prim-paths-with-Sdf-Path.usda')

# Build prim paths via Sdf.Path
world_path = Sdf.Path('/World')
geometry_path = world_path.AppendChild("Geometry")  # /World/Geometry
sphere_path = geometry_path.AppendChild("Sphere")  # /World/Geometry/Sphere

looks_path = world_path.AppendChild("Looks")  # /World/Looks
material_path = looks_path.AppendChild("Material")  # /World/Looks/Material

# Define prims at those paths
stage.DefinePrim(world_path)
stage.DefinePrim(geometry_path)
UsdGeom.Sphere.Define(stage, sphere_path)
stage.DefinePrim(looks_path)
stage.DefinePrim(material_path)

# Path checks and basic navigation
print("sphere_path IsPrimPath:", sphere_path.IsPrimPath())
print("sphere_path parent:", sphere_path.GetParentPath())
print("Geometry prim valid:", stage.GetPrimAtPath(geometry_path).IsValid())
print("\nmaterial_path IsPrimPath:", material_path.IsPrimPath())
print("material_path parent:", material_path.GetParentPath())
print("Looks prim valid:", stage.GetPrimAtPath(looks_path).IsValid())

stage.Save()

'''
sphere_path IsPrimPath: True
sphere_path parent: /World/Geometry
Geometry prim valid: True

material_path IsPrimPath: True
material_path parent: /World/Looks
Looks prim valid: True
'''