+++
id = "lemma-identity-pasting--3"
kind = "lemma"
title = "Vertical pasting"
order = 319006
aliases = ["bp-r095-3"]
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
+++
Let $A$ be a Grothendieck abelian category, for instance the category of
$\Lambda$-modules, and let $K\in D^+(X_{\acute{e}t},A)$. For composable maps
$X\xrightarrow{f}Y\xrightarrow{g}Z$ and a map
$h:Z'\to Z$, let $g':Y'\to Z'$, $h_Y:Y'\to Y$ and $f':X'\to Y'$,
$h_X:X'\to X$ complete $g$, $h$ and $f$, $h_Y$ to commutative squares
(for instance $Y'=Y\times_ZZ'$ and $X'=X\times_ZZ'$). Then the base change
map for the pasted square with left map $g'f'$ and right map $gf$ is the
composite

$$
h^*R(gf)_*K
\xrightarrow{\sim}
h^*Rg_*Rf_*K
\longrightarrow
Rg'_*h_Y^*Rf_*K
\longrightarrow
Rg'_*Rf'_*h_X^*K
\xrightarrow{\sim}
R(g'f')_*h_X^*K
$$

of the canonical composition isomorphisms for derived direct image,
the base change map for $g$ at $Rf_*K$, and $Rg'_*$ applied to the
base change map for $f$ at $K$, as in [definition-derived-base-change-map].
This is an equality of natural transformations in $K$. Only
commutativity of the squares is required.
