+++
id = "sbc-lem-finite-range-comparison"
kind = "lemma"
title = "Finite-range comparison"
lean = ["DerivedCategory.Plus.isIso_app_of_isGE_of_isLE", "DerivedCategory.Plus.isIso_app_of_bounded", "AlgebraicGeometry.Etale.isIso_baseChange_app_of_isGE_of_isLE"]
order = 2076
uses = ["def-weil-pbc-derived-categories", "thm-sp-truncation-e2"]
+++
If $H^q(K)=0$ outside $[a,b]$ and the comparison of the two
hypercohomology spectral sequences of
[thm-sp-truncation-e2] is an isomorphism on
every $E_2^{p,q}$, then it is an isomorphism on every abutment
$H^n\cong H^n$, and hence
${\operatorname{BC}}_{f,g}(K)$ is an isomorphism.
