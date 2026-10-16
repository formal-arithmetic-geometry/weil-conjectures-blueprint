+++
id = "lem-finrepair-finite-surjection-cancellation"
kind = "lemma"
title = "Constructibility descends through a finite surjection"
lean = ["AlgebraicGeometry.Etale.HasConstructibleDirectImages.of_comp_of_isFinite"]
order = 1948
uses = ["def-finrepair-property-c", "def-weil-pbc-scheme-conventions", "lem-fin-finite-morphism", "lem-weil-pbc-grothendieck-spectral-sequence", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative", "thm-constructible-serre", "thm-sp-if-e1"]
+++
Let $f:X\to S$ be a morphism between schemes of finite type over $k$,
and let $\pi:Y\to X$ be finite and surjective, in the sense of
[def-weil-pbc-scheme-conventions]. If $\mathcal C(f\pi)$ holds,
then $\mathcal C(f)$ holds, with $\mathcal C$ as in
[def-finrepair-property-c].
