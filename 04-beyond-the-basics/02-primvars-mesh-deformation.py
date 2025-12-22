# Example 2: Store “rest state” and “deformation” as Primvars
from pxr import Usd, UsdGeom, Sdf, Gf

# set up time sampling parameters
start_tc = 1
end_tc = 90
time_code_per_second = 30

# create stage and default prim
file_path = 'assets/27-primvars-mesh-deformation.usda'
stage = Usd.Stage.CreateNew(file_path)
stage.SetStartTimeCode(start_tc)
stage.SetEndTimeCode(end_tc)
stage.SetTimeCodesPerSecond(time_code_per_second)
world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

# define base mesh
mesh_vertex_locs = [
    Gf.Vec3f(0, 0, 0),
    Gf.Vec3f(1, 0, 0),
    Gf.Vec3f(1, 1, 0),
    Gf.Vec3f(0, 1, 0)
]
face_vertex_counts = [4]
face_vertex_indices = [0, 1, 2, 3]

# create mesh prim
plane = UsdGeom.Mesh.Define(stage, world.GetPath().AppendPath("Plane"))
plane.CreatePointsAttr(mesh_vertex_locs)
plane.CreateFaceVertexCountsAttr(face_vertex_counts)
plane.CreateFaceVertexIndicesAttr(face_vertex_indices)
UsdGeom.XformCommonAPI(plane).SetTranslate(Gf.Vec3d(2, 0, 0))
plane.GetDisplayColorPrimvar().Set([Gf.Vec3f(0.1, 0.8, 0.1)])

# set the rest_state for the mesh
plane_privar_api = UsdGeom.PrimvarsAPI(plane)
plane_privar_api.CreatePrimvar(
    "rest_state",
    Sdf.ValueTypeNames.Float3Array,
    UsdGeom.Tokens.vertex).Set(mesh_vertex_locs)

# set the rest_state for the mesh
plane_privar_api = UsdGeom.PrimvarsAPI(plane)
plane_privar_api.CreatePrimvar(
    "rest_state",
    Sdf.ValueTypeNames.Float3Array,
    UsdGeom.Tokens.vertex).Set(mesh_vertex_locs)

# set deformation for vertex locations as a primvar
deformation = [
    Gf.Vec3f(0.0, 0.0, 0.0),
    Gf.Vec3f(-0.3, 0.4, 0.0),
    Gf.Vec3f(-0.3, 0.4, 0.0),
    Gf.Vec3f(0.0, 0.0, 0.0),
]
plane_privar_api = UsdGeom.PrimvarsAPI(plane)
plane_privar_api.CreatePrimvar(
    "deformation",
    Sdf.ValueTypeNames.Float3Array,
    UsdGeom.Tokens.vertex).Set(deformation)

new_points = [
    p + o for p, o in zip(
        mesh_vertex_locs,
        plane_privar_api.GetPrimvar("deformation").Get())]

print("Original vertex locations:", mesh_vertex_locs)
print("\nDeforming mesh with primvar 'deformation':", deformation)
print("\nNew vertex locations:", new_points)

# Time-sample Mesh.points from rest to deformed
plane_points = plane.GetPointsAttr()
plane_points.Set(mesh_vertex_locs, Usd.TimeCode(start_tc))
plane_points.Set(new_points, Usd.TimeCode(end_tc))

stage.Save()