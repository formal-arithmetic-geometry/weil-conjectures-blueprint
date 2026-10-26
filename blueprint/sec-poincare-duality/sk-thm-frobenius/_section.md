+++
id = "sk-thm-frobenius"
kind = "theorem"
title = "Equivariance and reciprocal eigenvalues"
lean = ["AlgebraicGeometry.Etale.TateOrientation.isWeilPairing_poincarePairing", "AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing_frobeniusOperator", "AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing_frobeniusOperator_eq", "AlgebraicGeometry.Etale.TateOrientation.isWeilPairing_untwistedPoincarePairing", "AlgebraicGeometry.Etale.isWeilPairing_poincarePairing"]
order = 3412
uses = ["sk-def-pairing", "sk-def-sf-orientation", "sk-def-sf-weil-complexes", "sk-thm-derived-duality", "sk-thm-sf-identification"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth and separated of pure dimension $d$, let
$X=X_0\times\overline{\mathbf F}_q$, and let $(K,\phi_K)$ be a Weil complex on
$X$ with $K$ locally perfect, in the sense of Definition
[sk-def-sf-weil-complexes] (geometric Frobenius). Write
$K^\vee=\cHom_X(K,\Lambda_X)$, and let $\beta_K$ be the derived Poincaré pairing
of [sk-thm-sf-identification]. Equip the dual with the contragredient Weil
structure

$$
\operatorname{Fr}_X^*K^\vee
\simeq(\operatorname{Fr}_X^*K)^\vee
\xrightarrow{\ (\phi_K^{-1})^\vee\ }K^\vee.
$$

The derived Poincaré pairing is a morphism of Weil complexes for every
admissible $\Lambda$. Write $F$ for the endomorphisms of cohomology induced by
the Weil structures. The induced pairings on cohomology obey

$$
\langle Fx,Fy\rangle=\langle x,y\rangle
\quad\text{with the second factor twisted by }(d),
$$

or, in the untwisted form with values in $\Lambda(-d)$,

$$
\langle Fx,Fy\rangle^{\mathrm{untw}}
=q^d\langle x,y\rangle^{\mathrm{untw}}.
$$

For field coefficients the eigenvalues on $H^{2d-i}(X,K^\vee)$ are $q^d/\alpha$,
with multiplicities, where $\alpha$ ranges over the eigenvalues on
$H_c^i(X,K)$.
