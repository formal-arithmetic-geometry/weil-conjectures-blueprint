+++
id = "sbc-thm-bounded-below-derived-smooth-base-change"
kind = "theorem"
title = "Bounded-below derived smooth base change"
lean = ["DerivedCategory.Plus.isIso_app_of_forall_homology", "AlgebraicGeometry.Etale.isIso_baseChange_app_of_smooth"]
order = 1495
uses = ["lem-weil-pbc-derived-stalk-conservative", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-def-derived-categories-with-allowable-torsion", "sbc-lem-bounded-below-truncation-criterion", "sbc-thm-bounded-allowable-torsion", "sbc-thm-smooth-base-change"]
+++
In the square of
[sbc-thm-smooth-base-change] with $f$ smooth, $g$ quasi-compact
and quasi-separated, and $\mathcal P$ the set of primes invertible on
$S$: for $K\in D^+_{\mathcal P\text{-tor}}(T_{\Et})$,

$$
{\operatorname{BC}}_{f,g}(K):Lf^*Rg_*K\xrightarrow{\ \sim\ }Rh_*Le^*K
$$

in $D^+_{\mathcal P\text{-tor}}(S_{\Et})$.
