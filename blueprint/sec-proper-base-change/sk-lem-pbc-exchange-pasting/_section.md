+++
id = "sk-lem-pbc-exchange-pasting"
kind = "lemma"
title = "Identity and pasting"
order = 1530
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["sk-def-exchange"]
tags = ["sketch"]
+++
Let $K\in D^+(X_{\Et},\Lambda)$. Exchange [sk-def-exchange] is the identity
for an identity square, and is compatible with horizontal and vertical pasting
of commutative squares, in particular of cartesian squares. More explicitly, if $h:Y''\to Y'$ is a second base
change, with induced maps $h':X''\to X'$ and $f'':X''\to Y''$, the exchange
map for $gh$ is the composite in $D^+(Y''_{\Et},\Lambda)$

$$
h^{-1}g^{-1}Rf_*K\xrightarrow{\ h^{-1}\Ex_{\square,K}\ }
h^{-1}Rf'_*g'^{-1}K\xrightarrow{\ \Ex_{h,g'^{-1}K}\ }
Rf''_*h'^{-1}g'^{-1}K,
$$

under the canonical composition isomorphisms.

For composable maps $X\xrightarrow{f}Y\xrightarrow{e}Z$ and a base change
$h:Z'\to Z$, put $Y'=Y\times_ZZ'$ and $X'=X\times_ZZ'$. Writing $e':Y'\to Z'$,
$f':X'\to Y'$ and $g:Y'\to Y$, $g':X'\to X$, the exchange map for $ef$ is the
composite in $D^+(Z'_{\Et},\Lambda)$, natural in $K$,

$$
h^{-1}Re_*Rf_*K\xrightarrow{\ \Ex_{e,Rf_*K}\ }
Re'_*g^{-1}Rf_*K\xrightarrow{\ Re'_*\Ex_{f,K}\ }
Re'_*Rf'_*g'^{-1}K.
$$
