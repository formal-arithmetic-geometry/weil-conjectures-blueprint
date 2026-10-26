+++
id = "sk-thm-sf-verdier-exchange"
kind = "corollary"
title = "Verdier exchange formulas"
order = 3284
uses = ["sk-prop-sf-open-closed-triangle", "sk-lem-sf-mate", "sk-thm-sf-comp-composition", "sk-thm-sf-tensor-hom", "sk-def-ops", "sk-thm-pd-verdier-duality"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex"]
tags = ["sketch"]
+++
Here $\mathbb D_X$, $\mathbb D_Y$ and $\omega_X$, $\omega_Y$ are the Verdier duals and the
dualizing complexes of [sk-def-ops].

For a morphism $f:X\to Y$ there are natural isomorphisms of functors
$\Dctf(X,\Lambda)^{\mathrm{op}}\to\Dctf(Y,\Lambda)$ (first row) and
$\Dctf(Y,\Lambda)^{\mathrm{op}}\to\Dctf(X,\Lambda)$ (second row)

$$\begin{aligned}
 \mathbb D_YRf_!&\simeq Rf_*\mathbb D_X,&
 \mathbb D_YRf_*&\simeq Rf_!\mathbb D_X,\\
 \mathbb D_Xf^*&\simeq f^!\mathbb D_Y,&
 \mathbb D_Xf^!&\simeq f^*\mathbb D_Y.
\end{aligned}$$

In particular, for an open $j:U\hookrightarrow X$ and a closed
$i:Z\hookrightarrow X$,

$$
 \mathbb D_Xj_!\simeq Rj_*\mathbb D_U,\qquad
 \mathbb D_XRj_*\simeq j_!\mathbb D_U,\qquad
 i^*\mathbb D_X\simeq\mathbb D_Zi^!.
$$

They respect evaluation, composition and coefficient comparison.

*Complement.* For $f$ separated of finite type between finite-type $k$-schemes, with $Rf^!$
and $\omega_X=Ra_X^!\Lambda$, $\omega_Y=Ra_Y^!\Lambda$ formed with the constructible
exceptional adjoint of [det-def-sf-operations](vi), one has $Rf^!\omega_Y\cong\omega_X$. The
first isomorphism $\mathbb D_Y(Rf_!M)\xrightarrow{\sim}Rf_*\mathbb D_X(M)$,
$M\in\Dctf(X,\Lambda)$, is the tensor–Hom isomorphism of [sk-thm-sf-tensor-hom] at
$N=\omega_Y$ followed by $Rf_*\cHom_X(M,-)$ of this isomorphism. It is an isomorphism in the
ambient category $D^+(Y,\Lambda)$, natural in $M$ and compatible with finite reduction, scalar
extension and shifts.
