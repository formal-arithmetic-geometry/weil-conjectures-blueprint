+++
id = "det-properbasechange-modules"
kind = "lemma"
title = "Étale proper base change for module coefficients"
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_app_restrictScalars_iff", "AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology"]
order = 2012
uses = ["thm-weil-pbc-bounded-below", "det-pbc-conventions-module-cohomology", "def-weil-pbc-derived-exchange", "lemma-weil-pbc-derived-exchange-replacement", "lemma-weil-pbc-leray-acyclicity"]
+++
Let $f:X\to Y$ and $g:Y'\to Y$ be morphisms of schemes, and let $f',g'$ be
the base changes as in [def-weil-pbc-derived-exchange].

1. Let $\varphi:\Lambda\to\Lambda'$ be a morphism of commutative rings and
   write $\mathrm{res}:D^+(T_{\Et},\Lambda')\to D^+(T_{\Et},\Lambda)$ for
   restriction of scalars along $\varphi$. For every
   $K\in D^+(X_{\Et},\Lambda')$, the exchange map
   $\Ex^{\Lambda}_{\square,\mathrm{res}K}$ is an isomorphism in
   $D^+(Y'_{\Et},\Lambda)$ if and only if
   $\Ex^{\Lambda'}_{\square,K}$ is an isomorphism in
   $D^+(Y'_{\Et},\Lambda')$.
2. Let $\Lambda$ be a commutative ring and let $f$ be proper. If
   $K\in D^+(X_{\Et},\Lambda)$ has cohomology sheaves which are torsion as
   abelian sheaves, then
   $\Ex^{\Lambda}_{\square,K}:g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an isomorphism
   in $D^+(Y'_{\Et},\Lambda)$.
