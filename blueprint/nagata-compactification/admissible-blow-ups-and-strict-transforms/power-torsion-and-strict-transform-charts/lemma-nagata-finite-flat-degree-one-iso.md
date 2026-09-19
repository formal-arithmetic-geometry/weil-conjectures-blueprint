+++
id = "lemma-nagata-finite-flat-degree-one-iso"
kind = "lemma"
title = "Finite flat degree one is an isomorphism"
order = 372
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

A finite flat morphism of finite presentation whose finite locally free
degree is one is an isomorphism.

## Proof

Work affine locally, with corresponding finite locally free algebra $B$ over
$A$. On every residue field $\kappa(\mathfrak p)$ the fibre
$B\otimes_A\kappa(\mathfrak p)$ has dimension one. Its unit is nonzero
(otherwise the fibre algebra would be zero), hence it is a basis. Nakayama's
lemma therefore shows that $1\in B$ generates $B$ as an $A$-module in a
neighbourhood of every prime. The map $A\to B$, $a\mapsto a\,1$, is
consequently a surjective map between locally free rank-one modules and is
an isomorphism. These local algebra isomorphisms are compatible on
overlaps, so the original finite flat morphism is an isomorphism.
