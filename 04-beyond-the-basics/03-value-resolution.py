"""
    from pxr import Usd, UsdGeom

    # Open a stage
    stage = Usd.Stage.Open('example.usd')

    # Get a prim
    prim = stage.GetPrimAtPath('/World/MyPrim')

    # Get an attribute
    attr = prim.GetAttribute('myAttribute')
    # Usd.TimeCode.Default() is implied
    default_value = attr.Get()
    # Get the value at time code 100.
    animated_value = attr.Get(100)
    # Use EarliestTime to get earliest animated values if they exist
    value = attr.Get(Usd.TimeCode.EarliestTime())
"""

# Example 1: Attribute Value Resolution and Animation
from pxr import Usd, UsdGeom

# Time settings
start_tc = 1
end_tc = 120
cube_anim_start_tc = 60
mid_t = (cube_anim_start_tc + end_tc) // 2
time_code_per_second = 30

# Stage setup
file_path = 'assets/28-1-value-resolution.usda'
stage = Usd.Stage.CreateNew(file_path)
stage.SetTimeCodesPerSecond(time_code_per_second)
stage.SetStartTimeCode(start_tc)
stage.SetEndTimeCode(end_tc)

# World, Default Prim, and Ground
world_xform = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world_xform.GetPrim())
UsdGeom.XformCommonAPI(world_xform).SetRotate((-75, 0, 0))

# Create Ground Cube
ground = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("Ground"))
UsdGeom.XformCommonAPI(ground).SetScale((10, 5, 0.1))
UsdGeom.XformCommonAPI(ground).SetTranslate((0, 0, -0.1))

# Static cube with schema-defined default scale (no scale op authored)
static_default_cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("StaticDefaultCube"))
static_default_cube.GetDisplayColorAttr().Set([(0.2, 0.2, 0.8)])
static_default_cube_xform_api = UsdGeom.XformCommonAPI(static_default_cube)
static_default_cube_xform_api.SetTranslate((8, 0, 1))
UsdGeom.Xformable(static_default_cube).AddScaleOp()  # add scale op but do not author a value

# select a non-default cube scale value
cube_set_scale = (1.5, 1.5, 1.5)

# Static cube with an authored default scale (no time samples)
static_cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("StaticCube"))
static_cube.GetDisplayColorAttr().Set([(0.8, 0.2, 0.2)])
static_cube_xform_api = UsdGeom.XformCommonAPI(static_cube)
static_cube_xform_api.SetScale(cube_set_scale)  # set static_cube scale
static_cube_xform_api.SetTranslate((-8, 0, 1.5))

# Animated cube: same default as StaticCube plus time samples
anim_cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendChild("AnimCube"))
anim_cube.GetDisplayColorAttr().Set([(0.2, 0.8, 0.2)])
anim_cube_xform_api = UsdGeom.XformCommonAPI(anim_cube)
anim_cube_xform_api.SetScale(cube_set_scale)  # SAME as static_cube
anim_cube_xform_api.SetTranslate((0, 0, 1.5))

# Author time samples for scale and translate
# anim_cube_xform_api.SetScale(cube_set_scale, Usd.TimeCode(start_tc))
anim_cube_xform_api.SetScale((2.5, 2.5, 2.5), Usd.TimeCode(cube_anim_start_tc))  # first animated sample
anim_cube_xform_api.SetScale((5, 5, 5), Usd.TimeCode(end_tc))  # last sample
anim_cube_xform_api.SetTranslate((0, 0, 2.5), Usd.TimeCode(cube_anim_start_tc))
anim_cube_xform_api.SetTranslate((0, 0, 5.0), Usd.TimeCode(end_tc))

# Read back using resolved scale values
_, _, default_cube_fallback_scale, _, _ = UsdGeom.XformCommonAPI(static_default_cube).GetXformVectors(Usd.TimeCode.Default())
_, _, static_cube_default_scale, _, _ = static_cube_xform_api.GetXformVectors(Usd.TimeCode.Default())
_, _, anim_cube_default_scale, _, _ = anim_cube_xform_api.GetXformVectors(Usd.TimeCode.Default())
_, _, anim_cube_earliest_scale, _, _ = anim_cube_xform_api.GetXformVectors(Usd.TimeCode.EarliestTime())
_, _, anim_cube_tc1_scale, _, _ = anim_cube_xform_api.GetXformVectors(Usd.TimeCode(start_tc))
_, _, scale_mid, _, _ = anim_cube_xform_api.GetXformVectors(Usd.TimeCode(mid_t))

# Illustrate that Get() is the same as Get(Usd.TimeCode.Default())
no_time_code_is_default = static_cube.GetSizeAttr().Get() == static_cube.GetSizeAttr().Get(Usd.TimeCode.Default())

print(f"When querying a value Get() is the same as Get(Usd.TimeCode.Default()): {no_time_code_is_default}\n")

print(f"Scale - StaticDefaultCube (no authored xformOp:scale -> schema fallback):  {default_cube_fallback_scale}")  # returns identity fallback value.
print(f"Scale - StaticCube (authored default at Default time):  {static_cube_default_scale}")  # returns the user authored default value.
print(f"Scale - AnimCube (authored default at Default time):  {anim_cube_default_scale}")  # returns the user authored default value.
print(f"Scale - AnimCube at EarliestTime t={cube_anim_start_tc}:  {anim_cube_earliest_scale}")  # first authored time sample value
print(f"Scale - AnimCube at t={start_tc} (before first sample, clamped):  {anim_cube_tc1_scale}")  # resolved value prior to authored value.
print(f"Scale - AnimCube at mid_t={mid_t} (interpolated):  {scale_mid}")  # interpolated between samples

stage.Save()