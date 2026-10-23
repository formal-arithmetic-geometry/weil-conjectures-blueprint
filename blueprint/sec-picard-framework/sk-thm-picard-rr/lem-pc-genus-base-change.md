+++
id = "lem-pc-genus-base-change"
kind = "lemma"
title = "The genus is invariant under base change"
lean = ["AlgebraicGeometry.Scheme.arithmeticGenus_pullback"]
order = 734
uses = ["def-pc-base-change", "def-pc-smooth-projective-curve", "lem-pc-flat-base-change-cohom"]
+++
Let $k$ be a field, $X$ a quasi-compact and quasi-separated scheme over
$k$ (for instance a proper one) and $K/k$ a field extension. Then

$$
\dim_KH^1(X_K,\mathcal{O}_{X_K})=\dim_kH^1(X,\mathcal{O}_X).
$$

In particular, for a smooth projective curve
$X$ over $k$ the genus is invariant under base change:
$g(X_K)=g(X)$.
