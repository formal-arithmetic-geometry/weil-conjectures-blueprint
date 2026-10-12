+++
id = "cor-pur-affine-space-zero-section-purity"
kind = "theorem"
title = "Zero-section purity in affine space"
order = 2285
tags = ["latex:corollary"]
uses = ["cor-amb-affine-space-adjunction", "cor-pur-affine-space-purity", "def-amb-p1-trace", "def-coefficient-twists-detailed", "def-pur-affine-space-comparison", "def-pur-conventions", "def-sbc-affine-space", "def-weil-exceptional-inverse-image", "def-weil-scheme-morphism-properties", "lem-amb-cartier-kummer-map", "lem-pur-kunneth-supported", "lem-pur-support-localization-triangle", "prop-asd-smooth-base-change", "prop-pur-affine-line-orientation-base-change", "thm-pur-affine-line-orientation", "thm-pur-affine-line-purity", "thm-sf-ambient-adjoint-class"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
$A=A_{E,n}$, let $B$ be a
separated finite-type
$k$-scheme and let $z:B\hookrightarrow\mathbf A^c_B$ be the zero
section of the affine space of [def-sbc-affine-space]. The
$c$-fold exterior product of the normalized affine-line orientation of
[thm-pur-affine-line-orientation] is a canonical, base-change
compatible isomorphism

$$
\Lambda_B\xrightarrow{\ \sim\ }Rz^!\Lambda_{\mathbf A^c_B}(c)[2c],
$$

i.e. $Rz^!\Lambda\cong\Lambda_B(-c)[-2c]$; the product of the Kummer
boundaries of the coordinates $t_1,\dots,t_c$ corresponds to $1$.
Moreover this isomorphism is the inverse of the composite
$Rz^!\Lambda_{\mathbf A^c_B}(c)[2c]\xrightarrow{Rz^!(\gamma_{p_c,\Lambda_B})}
Rz^!Rp_c^!\Lambda_B\cong\Lambda_B$, where $\gamma_{p_c,\Lambda_B}$ is the
affine-space purity comparison of [def-pur-affine-space-comparison]
(an isomorphism by [cor-pur-affine-space-purity]) and the last
identification is the composition law for $p_cz=\operatorname{id}_B$:
the affine-space purity comparison, restricted along the zero section,
is normalized by the product of the Kummer boundaries of the
coordinates. Equivalently, the integration map transposed from
$\gamma_{p_c,\Lambda_B}$ sends the class of the zero section,
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$, to $1$.
