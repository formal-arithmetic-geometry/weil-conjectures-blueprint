+++
id = "lem-zl-quasi-finite"
kind = "lemma"
title = "Quasi-finite morphisms: exactness and upper-weight bound"
order = 3156
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite"]
uses = ["def-weil-complex-weights", "def-weil-extension-by-zero", "def-weil-pbc-qbar-category", "lem-zl-finite-pushforward", "lemma-weil-pbc-finite-direct-image-exact", "prop-functor-package", "thm-pqf-zmt-factorization"]
+++
Let $g:Z_0\to Y_0$ be a separated, quasi-finite morphism of finite type
of $k_0$-schemes, with $Y_0$ quasi-separated of finite type over $k_0$.
Let $\mathcal F$ be a constructible $\Qlb$-Weil sheaf on $Z_0$ and
$w\in\mathbf R$.

1. $R^ig_!\mathcal F=0$ for every $i>0$.
1. If $\mathcal F$ is $\iota$-mixed of weights at most $w$, then so is
   $g_!\mathcal F=R^0g_!\mathcal F$.
1. If every local Frobenius eigenvalue of $\mathcal F$ at every closed
   point has weight at most $w$, then the same holds for
   $g_!\mathcal F$.
