+++
id = "lemma-identity-pasting--2"
kind = "lemma"
title = "Horizontal pasting"
order = 319004
aliases = ["bp-r095-2"]
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz"]
uses = ["definition-underived-base-change-map--1"]
+++
Let $A$ be a Grothendieck abelian category, for instance the category of
$\Lambda$-modules, and let $K\in D^+(X_{\acute{e}t},A)$. Let
$f:X\to Y$, $f':X'\to Y'$, $g:Y'\to Y$ and $g':X'\to X$ form a
commutative square with $fg'=gf'$. If $h:Y''\to Y'$ is a second base
change, completed by maps
$h':X''\to X'$ and $f'':X''\to Y''$ to a commutative square with
$f'h'=hf''$, the base change map for the pasted square, with bottom map
$gh$, is the composite

$$
(gh)^*Rf_*K
\xrightarrow{\sim}
h^*g^*Rf_*K
\longrightarrow
h^*Rf'_*g'^*K
\longrightarrow
Rf''_*h'^*g'^*K
\xrightarrow{\sim}
Rf''_*(g'h')^*K
$$

of the canonical composition isomorphisms, $h^*$ applied to the base
change map of the first square, and the base change map of the second
square, as in [definition-derived-base-change-map]. This is an equality
of natural transformations in $K$. Only commutativity of the squares
is required.
