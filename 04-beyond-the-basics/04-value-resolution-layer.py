# Example 2: Custom Data snd Relationship Value Resolution
from pxr import Usd, UsdGeom
import os

# --- Layer 1 (weaker)
layer_1_path = 'assets/28-2-value-resolution-layer-1.usda'
layer_1_stage = Usd.Stage.CreateNew(layer_1_path)

layer_1_xform = UsdGeom.Xform.Define(layer_1_stage, "/World/XformPrim")
layer_1_xform_prim = layer_1_xform.GetPrim()

# "/World/XformPrim" custom data
layer_1_xform_prim.SetCustomDataByKey("source", "layer_1")
layer_1_xform_prim.SetCustomDataByKey("opinion", "weak")
layer_1_xform_prim.SetCustomDataByKey("unique_layer_value", "layer_1_unique_value") # only authored in layer_1

# Relationship contribution from base
look_a = UsdGeom.Xform.Define(layer_1_stage, "/World/Looks/LookA")
layer_1_xform_prim.CreateRelationship("look:targets").AddTarget(look_a.GetPath())
layer_1_stage.Save()

# --- Layer 2 (stronger)
layer_2_path = 'assets/28-3-value-resolution-layer-2.usda'
layer_2_stage = Usd.Stage.CreateNew(layer_2_path)

layer_2_xform = UsdGeom.Xform.Define(layer_2_stage, "/World/XformPrim")
layer_2_xform_prim = layer_2_xform.GetPrim()

# "/World/XformPrim" custom data
layer_2_xform_prim.SetCustomDataByKey("source", "layer_2")
layer_2_xform_prim.SetCustomDataByKey("opinion", "strong")

# Relationship contribution from override
look_b = UsdGeom.Xform.Define(layer_2_stage, "/World/Looks/LookB")
layer_2_xform_prim.CreateRelationship("look:targets").AddTarget(look_b.GetPath())
layer_2_stage.Save()

# --- Composed tage. First sublayer listed (layer_2) is strongest
composed_path = 'assets/28-4-value-resolution-composed.usda'
composed_stage = Usd.Stage.CreateNew(composed_path)
composed_stage.GetRootLayer().subLayerPaths = [os.path.basename(layer_2_path), os.path.basename(layer_1_path)]

xform_prim = composed_stage.GetPrimAtPath("/World/XformPrim")
resolved_custom_data = xform_prim.GetCustomData()

# resoled custom data;
print("Resolved CustomData:")
for key, value in resolved_custom_data.items():
    print(f"- '{key}': '{value}'")

# resolved relationship targets:
targets = xform_prim.GetRelationship("look:targets").GetTargets()
print(f"\nResolved relationship targets: {[str(t) for t in targets]}") # both LookA and LookB

composed_stage.Save()

# Write out the composed stage to a single file for inspection
explicit_composed_path = "assets/28-5-value-resolution-composed-explicit.usda"
txt = composed_stage.ExportToString(addSourceFileComment=False)
with open(explicit_composed_path, 'w') as f:
    f.write(txt)