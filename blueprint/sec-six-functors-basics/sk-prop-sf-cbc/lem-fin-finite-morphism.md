+++
id = "lem-fin-finite-morphism"
kind = "lemma"
title = "Finite direct images of constructible sheaves"
lean = ["AlgebraicGeometry.Etale.isZero_homology_rightDerivedLowerStar_singleFunctor_of_isFinite", "AlgebraicGeometry.Etale.isConstructibleSheaf_lowerStar_of_isFinite"]
order = 1931
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-pushforward-constructible-noetherian", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "sbc-def-coefficient-conventions"]
+++
Let $f:X\to S$ be finite
with $S$ of finite type over $k$, and let $F$ be a
constructible
$\Lambda$-sheaf on $X_{{\mathrm{et}}}$. Then the direct image
$f_*F$ of [def-weil-pbc-direct-image] is constructible on
$S_{{\mathrm{et}}}$ and $R^qf_*F=0$ for every $q>0$.
