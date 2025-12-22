from pxr import Usd, UsdGeom, Gf

# Open stage from timecode sample example 1
stage: Usd.Stage = Usd.Stage.Open("assets/11-timecode-sample-ex1.usda")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Get(stage, "/World/Sphere")

# Clear any existing translation
if translate_attr := sphere.GetTranslateOp().GetAttr():
    translate_attr.Clear()
    
# Create XformCommonAPI object for the sphere
sphere_xform_api = UsdGeom.XformCommonAPI(sphere)

# Set translation of the sphere at time 1
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=1)
# Set translation of the sphere at time 30
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -4.50, 0), time=30)
# Set translation of the sphere at time 45
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -5.00, 0), time=45)
# Set translation of the sphere at time 50
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -3.25, 0), time=50)
# Set translation of the sphere at time 60
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=60)

# if scale_attr := sphere.GetScaleOp().GetAttr():
#     scale_attr.Clear()

# sphere_xform_api = UsdGeom.XformCommonAPI(sphere)
# # Set scale of the sphere at time 1
# sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=1)  
# # Set scale of the sphere at time 30
# sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=30)   
# # Set scale of the sphere at time 45
# sphere_xform_api.SetScale(Gf.Vec3f(1.00, 0.20, 1.25), time=45)   
# # Set scale of the sphere at time 50
# sphere_xform_api.SetScale(Gf.Vec3f(0.75, 2.00, 0.75), time=50)  
# # Set scale of the sphere at time 60
# sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=60) 

# Export to a new flattened layer for this example.
stage.Export("assets/11-timecode-sample-ex2.usda", addSourceFileComment=False)