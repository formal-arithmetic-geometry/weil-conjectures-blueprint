+++
id = "lemma-extreme-degrees-affine-curve--2"
kind = "lemma"
title = "Degree two and geometric coinvariants"
name_showing = false
order = 1186002
aliases = ["bp-r366-2"]
lean = ["AlgebraicGeometry.nonempty_equiv_compactlySupportedCohomology_directImage_two"]
uses = ["definition-lisse-sheaves", "definition-middle-extension", "definition-tate-twists", "definition-compactification-refinement"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open in a smooth
geometrically connected affine curve over $\Fq$, and let $F$ be a
lisse $\Qbarl$-Weil sheaf on $U_0$, with
$\ell\ne\operatorname{char}\Fq$. Write $U$ and $C$ for the base
changes to $\Fbar$, and put

$$
W=H^0(U,F^\vee)^\vee,
$$

with the dual Frobenius action. There is a Frobenius-equivariant
isomorphism

$$
H_c^2(C,j_*F)\simeq W(-1).
$$

The space $W$ is the realization of geometric coinvariants used in
Lean, denoted by `AlgebraicGeometry.WeilSheaf.geometricCoinvariants`;
the twist $(-1)$ multiplies its Frobenius by $q$.
