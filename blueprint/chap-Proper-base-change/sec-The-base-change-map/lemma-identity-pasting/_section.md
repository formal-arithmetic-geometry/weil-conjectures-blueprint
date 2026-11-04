+++
id = "lemma-identity-pasting"
kind = "lemma"
title = "Identity and pasting"
order = 318
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["definition-derived-base-change-map"]
+++
Let $K\in D^+(X_{\acute{e}t},\Lambda)$. The base change map is the identity for an
identity square, and is compatible with horizontal and vertical pasting
of commutative squares, in particular of cartesian squares. More
explicitly, if $h:Y''\to Y'$ is a second base change, completed by maps
$h':X''\to X'$ and $f'':X''\to Y''$ to a commutative square with
$f'h'=hf''$, the base change map for the pasted square, with bottom map
$gh$, is the composite

$$
h^*g^*Rf_*K
\longrightarrow
h^*Rf'_*g'^*K
\longrightarrow
Rf''_*h'^*g'^*K
$$

of $h^*$ applied to the base change map of (4.1) and the
base change map of the second square, under the canonical composition
isomorphisms.

For composable maps $X\xrightarrow{f}Y\xrightarrow{g}Z$ and a map
$h:Z'\to Z$, let $g':Y'\to Z'$, $h_Y:Y'\to Y$ and $f':X'\to Y'$,
$h_X:X'\to X$ complete $g$, $h$ and $f$, $h_Y$ to commutative squares
(for instance $Y'=Y\times_ZZ'$ and $X'=X\times_ZZ'$). Then the base change
map for the pasted square with left map $g'f'$ and right map $gf$ is the
composite

$$
h^*Rg_*Rf_*K
\longrightarrow
Rg'_*h_Y^*Rf_*K
\longrightarrow
Rg'_*Rf'_*h_X^*K
$$

of the base change map for $g$ at $Rf_*K$ and $Rg'_*$ applied to the
base change map for $f$ at $K$.
