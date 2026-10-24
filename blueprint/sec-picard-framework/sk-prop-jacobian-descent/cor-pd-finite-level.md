+++
id = "cor-pd-finite-level"
kind = "theorem"
title = "The descent datum is defined at a finite separable level"
lean = ["AlgebraicGeometry.exists_isClosedImmersion_projectiveSpace_of_isPullback", "AlgebraicGeometry.exists_intermediateField_descentDatum", "AlgebraicGeometry.exists_intermediateField_descentDatum_isClosedImmersion"]
order = 892
tags = ["latex:corollary"]
uses = ["def-pc-base-change", "def-pc-geometrically-irreducible", "def-pc-morphism-conventions", "def-pc-projective-morphism", "def-pc-smooth-projective-curve", "def-pd-descent-datum", "def-pd-separable-closure", "lem-pd-canonical-descent-datum", "lem-pd-descent-cocycle", "lem-sc-abelian-variety-projective", "thm-pd-geometric-pic0", "thm-pd-spreading-out"]
+++
Let $k$ be a field, let $C$ be a
smooth projective curve over $k$
which is geometrically integral,
and let $(J_s,\varphi)$ be the scheme with its
descent datum furnished by
[lem-pd-canonical-descent-datum] and [lem-pd-descent-cocycle]. Then
there are a finite separable extension $K/k$, a scheme $J_K$ of finite
presentation over $K$, and a descent datum
$\varphi_K$ on $J_K$ over $\Spec(K)/\Spec(k)$ such that
$J_K\times_KK_s\cong J_s$ and such that $\varphi_K$
base changes to $\varphi$; moreover $J_K$ may
be chosen projective over $K$.
