+++
id = "sk-i-geometry"
kind = "proposition"
title = "Basic affine geometry"
order = 2820
uses = ["sk-d-geometry", "sk-d-tangent"]
lean = ["iInf_ker_algHom_eq_nilradical", "exists_algHom_ker_eq_of_isMaximal", "exists_isOpen_inter_subset_of_isConstructible", "ringKrullDim_quotient_lt_of_finiteType", "IsRegularLocalRing.isDomain", "isReduced_tensorProduct_of_perfectField"]
tags = ["sketch"]
+++
Finite-type affine schemes over $k$ are Noetherian (descending chains
of closed sets stabilize). They have finitely many irreducible
components. Closed points have residue field $k$, and a function on
a reduced affine variety vanishing at every $k$-point is zero.
Images of finite-type morphisms are constructible; a dense
constructible subset contains a nonempty open subset of its closure.
A proper closed subset of an irreducible variety has strictly smaller
dimension. Regular local rings are domains, so irreducible components
of a smooth variety do not meet.
A product of reduced affine varieties over $k$ is again a reduced affine
variety; the vanishing principle above therefore applies to it, so a
regular function on such a product vanishing at all its $k$-points is
zero. This is what lets a morphism defined on a product, such as a
commutator map, be tested on rational points in each variable
separately.
