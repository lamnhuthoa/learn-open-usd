
from pxr import Usd, UsdGeom, UsdLux, UsdPhysics, Gf

"""
    # Retrieve the schema info for a registered schema
    Usd.SchemaRegistry.FindSchemaInfo()

    # Retrieve the schema typeName
    Usd.SchemaRegistry.GetSchemaTypeName()
"""


# IsA Schemas
# UsdGeomSphere
"""
UsdGeom defines schemas for representing geometric objects, such as meshes, cameras, and curves as mentioned above. 
It also includes schemas for transformations, visibility, and other common properties.
"""

file_path = 'assets/16_schemas.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, '/WorldTransform')

# Define a sphere in the stage
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))

# Get and Set the radius attribute of the sphere
sphere.GetRadiusAttr().Set(10)


# UsdLuxDiskLight
"""
UsdLux defines schemas for representing light sources in a scene. It includes schemas such as sphere lights, disk lights, and distant lights, which were discussed in the lesson on USD lights.

Examples include UsdLuxDiskLight, UsdLuxRectLight, and UsdLuxSphereLight. These schemas bring properties relevant to each light type (e.g. radius for UsdLuxDiskLight). 
These attributes in combination with the attributes defined by the LightAPI schema (e.g. Intensity) allow us to fully define a light.
"""

# Define a disk light in the stage
disk_light: UsdLux.DiskLight = UsdLux.DiskLight.Define(stage, world_xform.GetPath().AppendPath("Lights/DiskLight"))
	
# Get all Attribute names that are a part of the DiskLight schema
dl_attribute_names = disk_light.GetSchemaAttributeNames()
	
# Get and Set the radius and intensity of the disk light prim
disk_light.GetRadiusAttr().Set(0.4)  # from DiskLight typed schema
disk_light.GetIntensityAttr().Set(1000)  # from LightAPI

# API Schemas
# UsdPhysicsRigidBodyAPI
"""
UsdPhysicsRigidBodyAPI adds physics properties to any UsdGeomXformable object for simulation such as rigid body dynamics.
"""

cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
# Apply a UsdPhysics Rigidbody API on the cube prim
cube_rb_api = UsdPhysics.RigidBodyAPI.Apply(cube.GetPrim())
	
# Get the Kinematic Enabled Attribute 
cube_rb_api.GetKinematicEnabledAttr()
	
# Create a linear velocity attribute of value 5
cube_rb_api.CreateVelocityAttr(Gf.Vec3f(5, 0, 0))

stage.Save()