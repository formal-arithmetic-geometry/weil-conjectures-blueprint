+++
id = "sbc-thm-bounded-derived-smooth-base-change"
kind = "theorem"
title = "Bounded derived smooth base change"
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_app_of_boundedConstructible_of_smooth"]
order = 2077
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-five-lemma-transfer", "lemma-weil-pbc-hypercohomology-convergence", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-lem-finite-range-comparison", "sbc-prop-extension-by-zero-and-arbitrary-base-change", "sbc-thm-smooth-base-change"]
+++
In the square of
[sbc-thm-smooth-base-change] with $f$ smooth and $g$ quasi-compact
and quasi-separated, for every $K\in\Dbc(T_{\Et},\Lambda)$,

$$
{\operatorname{BC}}_{f,g}(K):Lf^*Rg_*K\xrightarrow{\ \sim\ }Rh_*Le^*K
$$

in $D(X_{\Et},\Lambda)$, where the derived exchange is the one of
[sbc-def-base-change-map].
