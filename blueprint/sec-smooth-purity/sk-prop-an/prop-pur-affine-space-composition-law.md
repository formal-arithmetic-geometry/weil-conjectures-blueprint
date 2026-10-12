+++
id = "prop-pur-affine-space-composition-law"
kind = "theorem"
title = "Affine-space composition law"
order = 2281
tags = ["latex:proposition"]
uses = ["def-coefficient-twists-detailed", "def-pur-affine-space-comparison", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
$A=A_{E,n}$, and let $d,e\geq1$. Under the canonical identification
$\mathbf A^{d+e}_Y\cong\mathbf A^d_{\mathbf A^e_Y}$, the equality

$$
\gamma_{p_{d+e},K}
=
c_{p_e,p_d}^{-1}\circ
\gamma_{p_d,Rp_e^!K}\circ
Lp_d^*(\gamma_{p_e,K})(d)[2d]
$$

holds after the canonical reassociation of twists and shifts, where
$c_{g,f}:R(gf)^!\cong Rf^!Rg^!$ is the composition isomorphism for the
exceptional inverse image. The Koszul sign interchanging the two
$A(1)$-tensor factors in the product of $(d)[2d]$ and $(e)[2e]$ is
$+1$, both factors being of even degree; the two orderings of the affine
coordinates give the same composite comparison.
