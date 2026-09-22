+++
id = "lem-finrepair-constant-finite-comparison"
kind = "lemma"
title = "Constant coefficients under a finite normalization comparison"
order = 5201
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_constant_of_finiteComparison"]
uses = ["sbc-def-coefficient-conventions", "lem-fin-finite-morphism", "lem-fin-closed-immersion"]
+++
Let $f:X\to S$ be proper between finite-type $k$-schemes and let
$\nu:Y\to X$ be finite and surjective. Suppose $\nu$ is an isomorphism
outside a reduced closed subscheme $i:Z\hookrightarrow X$ for which $f|_Z$
is finite. Put $v=f\nu$, and let $M$ be a finite module over the ring of
[sbc-def-coefficient-conventions]. If all $R^qv_*\underline M$ are
constructible, then so are all $R^qf_*\underline M$. Moreover the natural
map
$$
R^qf_*\underline M\longrightarrow R^qv_*\underline M
$$
is an isomorphism for every $q\geq2$.

## Proof

The unit $\underline M_X\to\nu_*\underline M_Y$ is injective by the diagonal
description of the finite stalk formula; the fibre of the surjective finite
$\nu$ is nonempty at every geometric point. Let $Q$ be its cokernel. Both
sheaves in this monomorphism are constructible by [lem-fin-finite-morphism],
so $Q$ is constructible. Outside $Z$ the unit is an isomorphism; hence $Q$
restricts to zero there, and its canonical map $Q\to i_*i^*Q$ is an
isomorphism on all geometric stalks.

Closed-immersion exactness in [lem-fin-closed-immersion] and the composition
spectral sequence give $R^qf_*Q=R^q(f|_Z)_*i^*Q$. Since $f|_Z$ is finite,
[lem-fin-finite-morphism] makes $H=f_*Q$ constructible and makes these
higher direct images zero for $q>0$. The same finite exactness and
composition spectral sequence identify $R^qf_*\nu_*\underline M_Y$ with
$R^qv_*\underline M_Y$.

The long exact sequence of
$0\to\underline M_X\to\nu_*\underline M_Y\to Q\to0$ therefore gives
$$
f_*\underline M_X=\ker\bigl(v_*\underline M_Y\to H\bigr)
$$
and
$$
0\to\operatorname{coker}\bigl(v_*\underline M_Y\to H\bigr)
\to R^1f_*\underline M_X\to R^1v_*\underline M_Y\to0.
$$
All sheaves used to take the indicated kernel and cokernel are
constructible, and the rightmost term in the short exact sequence is
constructible by hypothesis. The weak-Serre property proves
constructibility in degrees zero and one. In every degree $q\geq2$, the
adjacent terms $R^{q-1}f_*Q$ and $R^qf_*Q$ are zero, so the same long exact
sequence gives the claimed isomorphism.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-grothendieck-spectral-sequence, lem:weil-pbc-geometric-stalk-conservative, lem:weil-pbc-constructible-serre
