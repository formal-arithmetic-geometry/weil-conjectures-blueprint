+++
id = "prop-constructible-truncations"
kind = "theorem"
title = "Construction of constructible truncations"
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.boundedAdicConstructible_truncLE", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedAdicConstructible_truncGE", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedAdicConstructible_mapDerivedCategory_upperStar", "AlgebraicGeometry.ProEtale.nonempty_truncLE_comp_mapDerivedCategory_upperStar_iso", "AlgebraicGeometry.ProEtale.nonempty_truncGE_comp_mapDerivedCategory_upperStar_iso", "AlgebraicGeometry.ProEtale.nonempty_mapDerivedCategory_upperStar_comp_homologyFunctor_iso"]
order = 3435
tags = ["latex:proposition"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "def-weil-t-structure", "det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "sk-prop-sfb-finite-extension-compatibility"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$. Fix a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
choose a finite extension $E/\Ql$ contained in $\Qlb$. Let $Y$ be a
finite-type $k$-scheme, where
finite type is the scheme
condition used throughout. Let
$\Lambda\in\{E,\Qlb\}$, regarded as a condensed ring, and let
$\Dbc(Y,\Lambda)\subseteq D(Y_{\mathrm{pro\acute et}},\Lambda)$ be the full
subcategory of bounded complexes with constructible cohomology sheaves
([det-def-sfb-bounded-constructible]). The symbols $\mathcal H^r$ denote the
cohomology sheaves of a
derived complex. Let $m,i\in\mathbf Z$.
The standard truncations of $D(Y_{\mathrm{pro\acute et}},\Lambda)$ restrict to
truncation functors

$$
\tau^{\leq m},\tau^{\geq m}:\Dbc(Y,\Lambda)
\longrightarrow \Dbc(Y,\Lambda),
$$

and these truncations, their natural maps, and the
distinguished truncation triangles satisfy the axioms of a
bounded t-structure on $\Dbc(Y,\Lambda)$, whose heart is the abelian category of
constructible $\Lambda_Y$-modules. For
$K\in \Dbc(Y,\Lambda)$, its cohomology functors satisfy

$$
\mathcal H^i(K)=\bigl(\tau^{\geq i}\tau^{\leq i}K\bigr)[i].
$$

The truncations commute with extension of scalars along $E_Y\to E'_Y$ for
finite $E'/E$ and along $E_Y\to\Qlb_Y$. For every scheme automorphism
$h:Y\xrightarrow{\sim}Y$, the
derived pullback $Lh^*$
commutes with the truncations and with $\mathcal H^i$.
