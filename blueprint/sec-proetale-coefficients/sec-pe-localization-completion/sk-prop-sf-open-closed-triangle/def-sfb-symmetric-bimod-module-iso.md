+++
id = "def-sfb-symmetric-bimod-module-iso"
kind = "definition"
title = "Symmetric bimodules come from module objects"
order = 1147
uses = ["lem-sfb-modobj-symmetric-bimodules"]
lean = ["Bimod.IsSymmetric.iso"]
+++
Let $\mathcal C$ be a braided monoidal category and $\mathcal R$ a commutative monoid
object. Let $P$ be a symmetric $\mathcal R$-$\mathcal R$-bimodule in the sense of
[lem-sfb-modobj-symmetric-bimodules], and let $M$ be the $\mathcal R$-module object
obtained by forgetting the right action of $P$. Then the identity of the underlying
object is an isomorphism of bimodules from the bimodule attached to $M$ in
[lem-sfb-modobj-symmetric-bimodules] to $P$. Hence every symmetric bimodule is
isomorphic to the bimodule attached to a module object.
