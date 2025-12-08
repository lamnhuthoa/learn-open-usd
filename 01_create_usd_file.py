# Activity 1: Create a USD File and Load it as a Stage

# Import the `Usd` module from the `pxr` package:
from pxr import Usd

# Define a file path name
# OpenUSD stage refers to a top-level USD file that serves as a container for organizing a hierarchy of elements called prims
# Stages aren't files, but a unified scenegraph populated from multiple data sources called layers.
file_path = "assets/first_stage.usda"

# Create a stage at the given file_path:
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

print(stage.ExportToString(addSourceFileComment=True))