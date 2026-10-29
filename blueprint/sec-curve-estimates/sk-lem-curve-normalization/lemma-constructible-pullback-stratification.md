+++
id = "lemma-constructible-pullback-stratification"
kind = "lemma"
title = "Pullback of a stratification"
order = 1587
lean = ["AlgebraicGeometry.Scheme.Stratification.pullback"]
uses = ["def-constructible-stratification"]
+++
Let $g\colon Y\to X$ be a morphism and let $(\iota_k\colon Z_k\to X)_{k<n}$
be a stratification of $X$. Then the base changes
$(\iota'_k\colon Z_k\times_XY\to Y)_{k<n}$ form a stratification of $Y$,
with strata $g^{-1}(X_k)$.
