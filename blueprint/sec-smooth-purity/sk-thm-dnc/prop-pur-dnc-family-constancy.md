+++
id = "prop-pur-dnc-family-constancy"
kind = "theorem"
title = "The deformation family is constant along the affine line"
order = 2305
tags = ["latex:proposition"]
uses = ["cor-pur-vector-bundle-purity", "def-pur-co-smoothness", "def-pur-conventions", "def-pur-dnc-section-family", "def-weil-derived-tensor", "lem-pur-concentrated-complex-shift", "lem-pur-dnc-section-geometry", "prop-pur-a1-invariance", "thm-pur-cohomological-smoothness"]
+++
In the purity conventions of [def-pur-conventions], in the situation of
[def-pur-dnc-section-family] with family object $F$, let
$a:\mathbf A^1_B\to B$ be the projection and let
$i_1:B\to\mathbf A^1_B$ be the section $t=1$.

1. *the family is a shift of a lisse line.* The family object
is a shift of a finite locally constant rank-one sheaf,
$$
F\simeq\mathcal L_F(d)[2d],
$$
and likewise $C(g,s)\simeq\mathcal L_1(d)[2d]$ on $B$; in
particular no descent of an object or of a morphism of a derived
category is needed below.
1. *constancy along the affine line.* There is a canonical
isomorphism
$$
\kappa:\;F\;\xrightarrow{\ \sim\ }\;a^*C(g,s).
$$
Since $i_1^*a^*C(g,s)=C(g,s)=i_1^*F$ by
[lem-pur-dnc-section-geometry](1), the family object is the
pullback of its own fibre at $t=1$: the deformation family is
constant along $\mathbf A^1_B$ over $B$.
1. *normalization and uniqueness.* $\kappa$ is the unique
isomorphism $F\to a^*C(g,s)$ which at the section $t=1$
restricts to the identity of $C(g,s)$ under the identification
$i_1^*F\simeq C(g,s)$ of
[lem-pur-dnc-section-geometry](1).
1. *locality and base change.* $\kappa$ is compatible with
etale localization on $B$ and with arbitrary base change
$B'\to B$.
