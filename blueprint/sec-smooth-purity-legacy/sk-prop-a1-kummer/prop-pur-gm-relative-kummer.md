+++
id = "prop-pur-gm-relative-kummer"
kind = "theorem"
tags = ["latex:proposition"]
title = "The affine line and the punctured line over a base"
order = 2275
uses = ["def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "fix-prop-adjunctions", "lem-pur-a1-direct-image", "lem-pur-finite-kummer-level", "lem-weil-derived-direct-image-composition", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-strict-henselization-stalk-formula", "sbc-lem-strict-henselian-constant-cohomology", "sbc-thm-smooth-base-change", "thm-pur-kummer-affine-line", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\Lambda=A=A_{E,n}$, let $Y$ be a separated finite-type $k$-scheme,
and use the affine-line datum of [def-pur-affine-line-datum]: the
projection $p:\mathbf A^1_Y\to Y$, the zero section $s$, the open
complement $j:\mathbf G_{m,Y}\hookrightarrow\mathbf A^1_Y$, the composite
$\pi=pj:\mathbf G_{m,Y}\to Y$, the finite-level twist
$\Lambda(1)=\mu_{\ell^N}\otimes_{\mathbf Z/\ell^N}A$, and the Kummer class
$\kappa(t)\in H^1(\mathbf G_{m,Y},\Lambda(1))$ of the coordinate. Write
$R^m\pi_*=\mathcal H^m R\pi_*$ for the cohomology sheaves of
[def-weil-derived-cohomology-sheaves]. Then:

1. *(Acyclicity of the affine line.)* The units
$\Lambda_Y\to Rp_*\Lambda_{\mathbf A^1_Y}$ and
$\Lambda_Y(1)\to Rp_*\Lambda_{\mathbf A^1_Y}(1)$ are isomorphisms; so
$R^mp_*\Lambda(1)=0$ for $m>0$.
1. *(The Kummer generator.)* The unit
$\Lambda_Y(1)\to R^0\pi_*\Lambda(1)$ — equivalently, restriction along $j$
composed with the pullback $p^*$ — is an isomorphism, and the map
$$
\Lambda_Y\longrightarrow R^1\pi_*\Lambda(1),\qquad 1\longmapsto\kappa(t),
$$
sending $1$ to the image of $\kappa(t)$ under the edge map
$H^1(\mathbf G_{m,Y},\Lambda(1))=H^1(Y,R\pi_*\Lambda(1))\to
\Gamma(Y,R^1\pi_*\Lambda(1))$, is an isomorphism: $R^1\pi_*\Lambda(1)$
is free of rank one on $\kappa(t)$.
1. *(Vanishing above degree one.)* $R^m\pi_*\Lambda(1)=0$ for $m\geq2$.
1. *(Base change.)* For every morphism $g:Y'\to Y$ of separated
finite-type $k$-schemes, with base changes
$p':\mathbf A^1_{Y'}\to Y'$, $\pi':\mathbf G_{m,Y'}\to Y'$ and
$g':\mathbf G_{m,Y'}\to\mathbf G_{m,Y}$, the pullback of the Kummer class
is the Kummer class, $g'^*\kappa(t)=\kappa(t')$, and the base-change
morphisms
$$
g^*Rp_*\Lambda(1)\to Rp'_*\Lambda(1),\qquad
g^*R\pi_*\Lambda(1)\to R\pi'_*\Lambda(1)
$$
are isomorphisms.

In particular, taking $Y'=\bar y$ a geometric point, (1)–(3) are
equivalent to the corresponding statements for $\mathbf A^1$ and
$\mathbf G_m$ over an algebraically closed field, which are
[thm-pur-kummer-affine-line].
