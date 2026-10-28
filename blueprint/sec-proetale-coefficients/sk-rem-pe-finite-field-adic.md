+++
id = "sk-rem-pe-finite-field-adic"
kind = "remark"
title = "The first cohomology of a finite field"
order = 1099
tags = ["sketch"]
+++
For $X=\Spec\mathbb F_q$ and $\ell\nmid q$,

$$
H^1(X_{\Proet},\mathbf Z_{\ell,X})\simeq\mathbf Z_\ell,
\qquad H^1(X_{\Proet},\mathbf Q_{\ell,X})\simeq\mathbf Q_\ell.
$$

Indeed the finite-level first cohomology is
$\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbf Z},\mathbf Z/\ell^n)=\mathbf Z/\ell^n$,
and the degree-zero groups are finite, so their $\varprojlim^1$ vanishes in the
Milnor sequence for continuous cohomology ([sk-prop-pe-continuous-cohomology]).
Localization commutes with bounded-below cohomology on the qcqs scheme $X$
(Stacks Project, Tag 09A3), which gives the rational statement. For the
discrete constant sheaf, however, $H^1(X_{\Et},\mathbf Q_\ell^{\mathrm{disc}})=0$:
a continuous homomorphism from a profinite group to the discrete torsion-free
additive group has finite, hence zero, image.
