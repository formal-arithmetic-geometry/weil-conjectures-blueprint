+++
id = "sk-rem-sf-matrix"
kind = "corollary"
title = "The six operations on $\\Dctf(-,A)$"
lean = ["AlgebraicGeometry.Etale.boundedConstructible_preservation", "AlgebraicGeometry.Etale.constructibleFiniteTor_preservation", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_derivedHom_mapDerivedCategory"]
order = 2406
uses = ["sk-prop-sf-existence", "sk-prop-sf-rf-shriek-preservation"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative $\ell$-primary ring. For separated finite-type
morphisms of the standing schemes, the operations $f^*$, $Rf_*$, $Rf_!$, and
$f^!$, together with $\otimes_A^{\mathbf L}$ and $R\mathcal Hom_A$, preserve
bounded constructible complexes of finite Tor amplitude. Here $f^*$, $Rf_*$,
$\otimes_A^{\mathbf L}$ and $R\mathcal Hom_A$ are the functors on
$D((-)_{\mathrm{proét}},A)$, and $Rf_!$, $f^!$ are the functors on
$\Loc(\Dctf(-,A))$ of [sk-prop-sf-existence].
