from pxr import Usd

stage: Usd.Stage = Usd.Stage.CreateNew("assets/13-getting-validating-defining-prims-at-path.usda")
stage.DefinePrim("/hello")
stage.DefinePrim("/hello/world")

# get the primitive at the path "/hello" from the current stage
hello_prim: Usd.Prim = stage.GetPrimAtPath("/hello")

# Get the primitive at the path "/hello/world" from the current stage
hello_world_prim: Usd.Prim = stage.GetPrimAtPath("/hello/world")

# Get the primitive at the path "/world" from the current stage
# Note: This will return an invalid prim because "/world" does not exist, but if changed to "/hello/world" it will return a valid prim
world_prim: Usd.Prim = stage.GetPrimAtPath("/world")

# Print whether the primitive is valid
print("Is /hello a valid prim? ", hello_prim.IsValid())
print("Is /hello/world a valid prim? ", hello_world_prim.IsValid())
print("Is /world a valid prim? ", world_prim.IsValid())

stage.Save()

'''
Is /hello a valid prim?  True
Is /hello/world a valid prim?  True
Is /world a valid prim?  False
'''