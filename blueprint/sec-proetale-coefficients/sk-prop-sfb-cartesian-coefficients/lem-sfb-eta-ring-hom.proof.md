+++
kind  = "proof"
of    = "lem-sfb-eta-ring-hom"
uses = ["lem-sfb-finite-monoidal-adjunction"]
+++
The adjunction $f^*\dashv f_*$ is monoidal
([lem-sfb-finite-monoidal-adjunction]). So its unit is a monoidal natural
transformation, and its component $\Lambda_Y\to f_*f^*\Lambda_Y$ is a morphism
of ring objects. By [lem-sfb-alpha-ring-hom], $\alpha_f$ is a morphism of
ring objects, and the lax monoidal $f_*$ sends it to a morphism of ring
objects. A composite of morphisms of ring objects is one.
