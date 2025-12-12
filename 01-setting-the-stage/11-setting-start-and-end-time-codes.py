# Import the necessary modules from the `pxr` library:
from pxr import Usd, UsdGeom, Gf

# Open stage from starting point usda
stage: Usd.Stage = Usd.Stage.Open("assets/11-timecode-sample.usda")

# Set the `start` and `end` time codes for the stage:
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(60)

# Export to a new flattened layer for this example.
stage.Export("assets/11-timecode-sample-ex1.usda", addSourceFileComment=False)