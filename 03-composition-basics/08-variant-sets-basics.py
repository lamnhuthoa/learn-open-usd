# https://docs.nvidia.com/learn-openusd/latest/composition-basics/variant-sets.html

# On a prim:
prim.GetVariantSets() # -> UsdVariantSets
vsets = prim.GetVariantSets()
vset  = vsets.AddVariantSet("name")  # -> UsdVariantSet (create or get)
vset.AddVariant("ChoiceA")  # add a variant
vset.SetVariantSelection("ChoiceA") # select a variant

# Author opinions inside a variant:
with vset.GetVariantEditContext():
    # All specs authored in this 'with' go inside the selected variant
    ...

# Other useful calls:
vset.GetVariantNames()  # ["ChoiceA", "ChoiceB", ...]
vset.GetVariantSelection()  # currently selected name or ""
vset.ClearVariantSelection()  # remove selection at edit target