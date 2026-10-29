+++
id = "cor-cbc-derived-extension-zero-base-change"
kind = "theorem"
title = "Derived extension-by-zero base change"
lean = ["AlgebraicGeometry.Etale.isIso_derivedPlusFormalism_baseChange"]
order = 2560
tags = ["latex:corollary"]
uses = ["def-cbc-open-immersion-square", "def-weil-pbc-derived-categories", "def-weil-pbc-extension-by-zero", "lem-cbc-extension-zero-base-change"]
+++
Let $\square$ be an
open-immersion square and let
$\Lambda$ be a finite commutative ring. For every
$K\in D^+(U_{\Et},\Lambda)$ the map of
[lem-cbc-extension-zero-base-change] is an isomorphism

$$
g^{-1}j_!K\xrightarrow{\ \sim\ }j'_!g_U^{-1}K
$$

in $D^+(X'_{\Et},\Lambda)$, and the isomorphism is natural in $K$,
is the identity for $g=\operatorname{id}$, and is compatible with
pasting of open-immersion squares.
