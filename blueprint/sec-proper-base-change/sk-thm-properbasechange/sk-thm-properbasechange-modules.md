+++
id = "det-properbasechange-modules"
kind = "lemma"
title = "Étale proper base change for module coefficients"
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology"]
uses = ["thm-weil-pbc-bounded-below", "det-pbc-conventions-module-cohomology", "def-weil-pbc-derived-exchange", "lemma-weil-pbc-derived-exchange-replacement", "lemma-weil-pbc-leray-acyclicity"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be proper, let
$g:Y'\to Y$ be arbitrary, and let $f',g'$ be the base changes as in
[def-weil-pbc-derived-exchange]. Write
$\mathrm{For}:D^+(T_{\Et},\Lambda)\to D^+(T_{\Et},\mathbf Z)$ for the
forgetful functor. For every $K\in D^+(X_{\Et},\Lambda)$ there is a
canonical identification

$$
\mathrm{For}\bigl(\Ex^{\Lambda}_{\square,K}\bigr)=\Ex^{\mathbf Z}_{\square,\mathrm{For}K}
$$

under the isomorphisms $\mathrm{For}\,g^{-1}=g^{-1}\mathrm{For}$,
$\mathrm{For}\,Rf_*\cong Rf_*\mathrm{For}$ (and likewise for $f',g'$) of
[det-pbc-conventions-module-cohomology]. Consequently, if the cohomology
sheaves of $\mathrm{For}K$ are torsion, then
$\Ex^{\Lambda}_{\square,K}:g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an isomorphism in
$D^+(Y'_{\Et},\Lambda)$.
