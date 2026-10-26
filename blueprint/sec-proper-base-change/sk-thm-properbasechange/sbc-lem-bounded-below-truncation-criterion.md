+++
id = "sbc-lem-bounded-below-truncation-criterion"
kind = "lemma"
title = "Bounded-below truncation criterion"
lean = ["DerivedCategory.Plus.isIso_homologyFunctor_map_map_truncLE\u03b9_app", "AlgebraicGeometry.Etale.isIso_homologyFunctor_map_rightDerivedFunctorPlus_map_truncLE\u03b9_app", "AlgebraicGeometry.Etale.isIso_homologyFunctor_map_baseChangeSource_map_truncLE\u03b9_app", "AlgebraicGeometry.Etale.isIso_homologyFunctor_map_baseChangeTarget_map_truncLE\u03b9_app"]
order = 1988
uses = ["thm-sp-truncation-e2", "sbc-def-derived-categories-with-allowable-torsion"]
+++
Let $K\in D^+_{\mathcal P\text{-tor}}(T_{\Et})$. For fixed $n$, only
$H^q(K)$ with $q\leq n$ can contribute to $H^n(Rg_*K)$. Hence

$$
H^n(Rg_*\tau_{\leq n}K)\xrightarrow{\ \sim\ }H^n(Rg_*K),
$$

and the analogous statement holds after pullback and for $h_*$.
