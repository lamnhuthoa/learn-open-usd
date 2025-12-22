# Example 2: Referencing an External Asset
from pxr import Usd, UsdGeom

file_path = 'assets/24-03-referencing-basics-asset-ref.usda'
asset_ref_stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define a root Xform named "World"
world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(asset_ref_stage, '/World')

# Define a child Xform named "Geometry" under the "World" Xform
geometry_xform: UsdGeom.Xform = UsdGeom.Xform.Define(asset_ref_stage, world_xform.GetPath().AppendPath("Geometry"))

# Define a new Xform named "Box" under the root "Geometry" Xform
box_xform: UsdGeom.Xform = UsdGeom.Xform.Define(asset_ref_stage, geometry_xform.GetPath().AppendPath("Box"))
box_prim: Usd.Prim = box_xform.GetPrim()

# Add a reference to a USD file containing a box geometry
# box_prim.GetReferences().AddReference("./cubebox_a02/Railway_Signal_Box_No.usdz")
box_prim.GetReferences().AddReference("./Scenes/Templates/Basic/clean_cloudy_sky_and_floor.usd")

asset_ref_stage.Save()