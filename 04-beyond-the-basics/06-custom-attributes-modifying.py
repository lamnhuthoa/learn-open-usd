from pxr import Usd

file_path = 'assets/29-1-custom-attributes.usda'
stage: Usd.Stage = Usd.Stage.Open(file_path)
box_prim = stage.GetPrimAtPath('/World/Packages/Box')

# Get the weight attribute
weight_attr: Usd.Attribute = box_prim.GetAttribute("acme:weight")
# Set the value of the weight attribute
weight_attr.Set(4.25)

# Print the weight of the box
print("Wegith of Box:", weight_attr.Get())

stage.Save()