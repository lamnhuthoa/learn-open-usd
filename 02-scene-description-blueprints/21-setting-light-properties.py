"""
Define two new prims, SphereLight and DistantLight, and set a few properties for them.
"""

from pxr import Gf, Usd, UsdGeom, UsdLux

file_path = "assets/21-setting-light-properties.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
geom_scope: UsdGeom.Scope = UsdGeom.Scope.Define(stage, "/Geometry")
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, geom_scope.GetPath().AppendPath("Box"))

# Define a `Scope` Prim in stage at `/Lights`:
lights_scope: UsdGeom.Scope = UsdGeom.Scope.Define(stage, "/Lights")

# Define a `Sun` prim in stage as a child of `lights_scope`, called `Sun`:
distant_light = UsdLux.DistantLight.Define(stage, lights_scope.GetPath().AppendPath("Sun"))
# Define a `SphereLight` prim in stage as a child of lights_scope called `SphereLight`:
sphere_light = UsdLux.SphereLight.Define(stage, lights_scope.GetPath().AppendPath("SphereLight"))

# Configure the distant light's emissive attributes:
distant_light.GetColorAttr().Set(Gf.Vec3f(1.0, 0.0, 0.0)) # Light color (red)
distant_light.GetIntensityAttr().Set(120.0) # Light intensity
# Lights are Xformable
if not (distant_light_xform_api := UsdGeom.XformCommonAPI(distant_light)):
    raise Exception("Prim not compatible with XformCommonAPI")
distant_light_xform_api.SetRotate((45.0, 0.0, 0.0))

# Configure the sphere light's emissive attributes:
sphere_light.GetColorAttr().Set(Gf.Vec3f(0.0, 0.0, 1.0)) # Light color (blue)
sphere_light.GetIntensityAttr().Set(50000.0) # Light intensity
# Lights are Xformable
if not (sphere_light_xform_api := UsdGeom.XformCommonAPI(sphere_light)):
    raise Exception("Prim not compatible with XformCommonAPI")
sphere_light_xform_api.SetTranslate((5.0, 10.0, 0.0))

stage.Save()