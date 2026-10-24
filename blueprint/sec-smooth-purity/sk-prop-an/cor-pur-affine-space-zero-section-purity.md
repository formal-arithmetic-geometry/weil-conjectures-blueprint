+++
id = "cor-pur-affine-space-zero-section-purity"
kind = "theorem"
title = "Zero-section purity in affine space"
order = 2935
tags = ["latex:corollary"]
uses = ["cor-amb-affine-space-adjunction", "cor-pur-affine-space-purity", "def-amb-p1-trace", "def-coefficient-twists-detailed", "def-pur-affine-space-comparison", "def-pur-conventions", "def-sbc-affine-space", "def-weil-exceptional-inverse-image", "def-weil-scheme-morphism-properties", "lem-amb-cartier-kummer-map", "lem-pur-divisor-class", "lem-pur-kunneth-supported", "lem-pur-support-localization-triangle", "prop-asd-smooth-base-change", "prop-pur-affine-line-orientation-base-change", "thm-pur-affine-line-orientation", "thm-pur-affine-line-purity", "thm-sf-ambient-adjoint-class"]
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
Moreover this isomorphism is $(-1)^c$ times the inverse of the composite
$Rz^!\Lambda_{\mathbf A^c_B}(c)[2c]\xrightarrow{Rz^!(\gamma_{p_c,\Lambda_B})}
Rz^!Rp_c^!\Lambda_B\cong\Lambda_B$, where $\gamma_{p_c,\Lambda_B}$ is the
affine-space purity comparison of [def-pur-affine-space-comparison]
(an isomorphism by [cor-pur-affine-space-purity]) and the last
identification is the composition law for $p_cz=\operatorname{id}_B$:
the affine-space purity comparison, restricted along the zero section,
carries the product of the Kummer boundaries of the coordinates to
$(-1)^c$. Equivalently, the integration map transposed from
$\gamma_{p_c,\Lambda_B}$ sends the class of the zero section,
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$, to $(-1)^c$, and
it sends the product $c_{D_1}\cup\cdots\cup c_{D_c}$ of the Cartier
classes of [lem-amb-cartier-kummer-map] of the coordinate hyperplanes
$D_i=V(t_i)$ to $1$. The sign is that of [lem-pur-divisor-class](b):
$\partial\kappa(t_i)=-c_{D_i}$, and the projective-line trace of
[def-amb-p1-trace] is normalized by $t_q(c_1(\mathcal O(1)))=1$.
