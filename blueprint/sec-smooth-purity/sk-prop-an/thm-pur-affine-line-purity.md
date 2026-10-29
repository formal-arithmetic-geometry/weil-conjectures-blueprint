+++
id = "thm-pur-affine-line-purity"
kind = "theorem"
title = "Affine-line purity"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineLine"]
order = 3271
uses = ["cor-amb-affine-space-adjunction", "def-amb-p1-trace", "def-pur-affine-line-datum", "def-pur-affine-line-purity-comparison", "def-pur-conventions", "prop-asd-smooth-base-change", "thm-sf-ambient-adjoint-class", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting), let $Y$ be the scheme of the
affine-line datum and let
$K\in D^b_{ctf}(Y,\Lambda)$ with $\Lambda=A$. The affine-line purity
comparison $\gamma_{p,K}$ of
[def-pur-affine-line-purity-comparison] – the adjoint of the
projection-formula composite
$Rp_!Lp^*K(1)[2]\cong K\otimes^L Rp_!\Lambda_{\mathbf A^1_Y}(1)[2]\to K$
formed with the projective-line trace of [def-amb-p1-trace], which is
normalized by $t_q(c_1(\mathcal O(1)))=1$ – is an isomorphism

$$
\gamma_{p,K}:Lp^*K(1)[2]\xrightarrow{\ \sim\ }Rp^!K.
$$

It is natural in $K$ and compatible with arbitrary base change of $Y$.
