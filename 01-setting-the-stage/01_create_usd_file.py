# Activity 1: Create a USD File and Load it as a Stage

# Import the `Usd` module from the `pxr` package:
from pxr import Usd, UsdGeom

# Define a file path name
# OpenUSD stage refers to a top-level USD file that serves as a container for organizing a hierarchy of elements called prims
# Stages aren't files, but a unified scenegraph populated from multiple data sources called layers.
file_path = 'assets/01-first_stage.usda'

# - creates a new empty USD Stage where 3D scenes are assembled.
# - .usda are human-readable UTF-8 text.
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
print(stage.ExportToString())

# https://openusd.org/release/glossary.html#usdglossary-prim
UsdGeom.Cube.Define(stage, '/cube')
stage.Save()