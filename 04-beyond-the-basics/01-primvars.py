"""
    # Constructs a UsdGeomPrimvarsAPI on UsdPrim prim
    primvar_api = UsdGeom.PrimvarsAPI(prim)

    # Creates a new primvar called displayColor of type Color3f[]
    primvar_api.CreatePrimvar('displayColor', Sdf.ValueTypeNames.Color3fArray)

    # Gets the displayColor primvar
    primvar = primvar_api.GetPrimvar('displayColor')

    # Sets displayColor values
    primvar.Set([Gf.Vec3f(0.0, 1.0, 0.0)])

    # Gets displayColor values
    values = primvar.Get()
"""

# Example 1: Primvar interpolation (constant, uniform, vertex)
from pxr import Usd, UsdGeom, Gf

# Create stage and default prim
file_path = 'assets/26-primvars.usda'
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

# Two-quad mesh topology  (6 points, 2 faces)
mesh_vertex_locs = [
    Gf.Vec3f(-1, 0, 0),
    Gf.Vec3f(0, 0, 0),
    Gf.Vec3f(0, 1, 0),
    Gf.Vec3f(-1, 1, 0),
    Gf.Vec3f(1, 0, 0),
    Gf.Vec3f(1, 1, 0),
]
face_vertex_counts = [4, 4]
face_vertex_indices = [0, 1, 2, 3,  1, 4, 5, 2]

per_prim_color = [Gf.Vec3f(0.5, 0.0, 0.5)]
per_face_colors = [Gf.Vec3f(0.0, 0.0, 1.0), Gf.Vec3f(1.0, 0.0, 0.0)]
per_vertex_colors = [
    Gf.Vec3f(0.0, 0.0, 1.0), Gf.Vec3f(0.5, 0.0, 0.5), Gf.Vec3f(0.5, 0.0, 0.5),
    Gf.Vec3f(0.0, 0.0, 1.0), Gf.Vec3f(1.0, 0.0, 0.0), Gf.Vec3f(1.0, 0.0, 0.0)
]

# Define interpolation mode and colors
example_meshes = {
    "PerPrim": {
        "interpolation": UsdGeom.Tokens.constant,
        "colors": per_prim_color
    },
    "PerFace": {
        "interpolation": UsdGeom.Tokens.uniform,
        "colors": per_face_colors
    },
    "PerVertex": {
        "interpolation": UsdGeom.Tokens.vertex,
        "colors": per_vertex_colors
    }
}

for i, (example_mesh, color_details) in enumerate(example_meshes.items()):
    mesh_prim = UsdGeom.Mesh.Define(stage, world.GetPath().AppendPath(example_mesh))
    mesh_prim.CreatePointsAttr(mesh_vertex_locs)
    mesh_prim.CreateFaceVertexCountsAttr(face_vertex_counts)
    mesh_prim.CreateFaceVertexIndicesAttr(face_vertex_indices)
    UsdGeom.XformCommonAPI(mesh_prim).SetTranslate(Gf.Vec3d(i * 2.5, 0, 0))

    mesh_disp_color_primvar = mesh_prim.GetDisplayColorPrimvar()
    mesh_disp_color_primvar.SetInterpolation(color_details["interpolation"])
    mesh_disp_color_primvar.Set(color_details["colors"])

stage.Save()