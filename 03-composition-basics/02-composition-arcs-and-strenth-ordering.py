# https://docs.nvidia.com/learn-openusd/latest/composition-basics/strength-ordering.html
"""
# Local
First, local. The algorithm iterates through the local opinions. Local opinions are any opinion authored 
directly on a layer or a sublayer of a layer, without any additional composition.


# Inherits
Second, it looks for any inherit arcs in the scenegraph. An inherit arc allows opinions authored on one 
source prim in the scenegraph to affect all prims in the scenegraph that author an inherits arc to that 
source prim. In this way, for example, you can make changes to all pine trees in a forest without 
changing the source of the pine tree itself.


# Variant Sets
Third, variant sets. Variant sets, as the name implies, defines one or more scenegraph hierarchies for a 
prim (called variants), and composes one of them. In this way, for example, an object can have multiple 
geometric representations.


# References and Payloads
The next strongest opinions are references, and then payloads. References compose the contents of a 
separate layer as a scenegraph. Payloads are similar, but have the ability to load or unload the layer from 
the stage at runtime. A typical use of references and payloads would be to modularly bring assets into a 
scene (e.g. furniture in a room).


# Specializes
Finally, we have specialize arcs. A specialize arc is essentially authoring a new fallback value for a 
property; so if all the other compositional choices result in no value, the specializes value will win. This is 
commonly used with material libraries - for example, a basic Plastic material may be specialized by a 
RoughPlastic material which reduces the value on the glossiness property. Any subsequent opinion on 
the RoughPlastic material will take precedence, because specializes is the weakest composition arc.
"""

"""
                LIVERPS
Strongest   
    |           Local
    |           Inherits
    |           VariantSets
    |           Relocates
    |           References
    |           Payloads
    |           Specializes
 Weakest
"""