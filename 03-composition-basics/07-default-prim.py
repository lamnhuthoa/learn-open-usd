"""
#usda 1.0
(
    defaultPrim = "Car"
)

def Xform "Car" {
    def Mesh "Body" {
        double3[] points = [(0, 0, 0), (2, 0, 0), (2, 1, 0), (0, 1, 0)]
        int[] faceVertexCounts = [4]
        int[] faceVertexIndices = [0, 1, 2, 3]
    }
}

def Xform "Building" {
    def Mesh "Structure" {
        double3[] points = [(0, 0, 0), (5, 0, 0), (5, 10, 0), (0, 10, 0)]
        int[] faceVertexCounts = [4]
        int[] faceVertexIndices = [0, 1, 2, 3]
    }
}
"""


# The default prim is set using the SetDefaultPrim() method on a USD stage. This method accepts any 
# Usd.Prim, but the prim must be a top-level prim on the stage. Here’s a simple example:

"""
    from pxr import Usd, UsdGeom, Sdf

    # Create a new USD stage
    stage = Usd.Stage.CreateInMemory()

    # Define a top-level Xform prim
    default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()

    # Set the Xform prim as the default prim
    stage.SetDefaultPrim(default_prim)

    # Export the stage to a string to verify
    usda = stage.GetRootLayer().ExportToString()
    print(usda)

    # Check that the expected default prim was set
    assert stage.GetDefaultPrim() == default_prim
"""

# Example 1: Setting a default prim
# SetDefaultPrim() sets the default prim for the stage’s root layer.
# A *defaultPrim* is layer metadata. If the stage’s root layer is used as a reference or payload it is best practice to set a default prim.

from pxr import Usd

file_path = "assets/25-default-prim.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
stage.DefinePrim("/hello")
stage.DefinePrim("/hello/world")
hello_prim: Usd.Prim = stage.GetPrimAtPath("/hello")

# Set the default primitive of the stage to the primitive at "/hello":
stage.SetDefaultPrim(hello_prim)

stage.Save()