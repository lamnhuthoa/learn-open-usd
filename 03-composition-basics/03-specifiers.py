# https://docs.nvidia.com/learn-openusd/latest/composition-basics/specifiers.html
"""
Specifiers in OpenUSD convey the intent for how a prim or a prim spec should be interpreted in the 
composed scene. The specifier can be one of three values: *def*, *over* or *class*.
"""

# def, which is short for define , defines the prim in the current layer. def indicates a prim exists and concretely defined on the stage.

# over, which is short for override , holds overrides for opinions that already exist in the composed scene 
# on another layer. The over will not translate back to the original prim, and is what enables non-
# destructive editing workflows, such as changing a property of a prim, like its color, in another layer.

# A class prim essentially signals that it is a blueprint. class prims abstract and contain opinions that 
# are meant to be composed onto other prims. It’s worth noting that class prims are intended as the 
# target of a reference, payload, inherit, or specialize composition arc or as a relationship target for a 
# PointInstancer. These are concepts we’ll cover in a later lesson.

# How to get or set a prim's specifier using Python

"""
    # Get a prim's specifier
    prim.GetSpecifier()

    # Set a prim's specifier
    prim.SetSpecifier(specifier)
"""

# Example 1: Authoring defs and a class in a base layer
from pxr import Usd, UsdGeom, Sdf, Gf

file_path = 'assets/22-specifiers.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Create a simple scene with two cubes
world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world_xform.GetPrim())

box_prim_cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("Box"))
box_prim_cube.GetSizeAttr().Set(2.0)

box_2_prim_cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("Box_2"))
box_2_prim_cube.GetSizeAttr().Set(2.0)
box_2_api = UsdGeom.XformCommonAPI(box_2_prim_cube)
box_2_api.SetTranslate(Gf.Vec3d(5, 0, 0))

# Define a class prim with a displayColor primvar 
class_prim = stage.CreateClassPrim(world_xform.GetPath().AppendPath("_Look/_green"))
class_prim_primvar_api = UsdGeom.PrimvarsAPI(class_prim)
class_prim_primvar_api.CreatePrimvar("displayColor", Sdf.ValueTypeNames.Color3fArray).Set([Gf.Vec3f(0.1, 0.8, 0.2)])

# Inspect specifiers
print("box specifier:", box_prim_cube.GetPrim().GetSpecifier())  # Sdf.SpecifierDef
print("box_2 specifier:", box_2_prim_cube.GetPrim().GetSpecifier())  # Sdf.SpecifierDef
print("class_prim specifier:", class_prim.GetSpecifier())  # e.g. Sdf.SpecifierClass

stage.Save()