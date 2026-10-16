+++
id = "lem-pc-genus-base-change"
kind = "lemma"
title = "The genus is invariant under base change"
lean = ["AlgebraicGeometry.Scheme.arithmeticGenus_pullback"]
order = 744
uses = ["def-pc-base-change", "def-pc-smooth-projective-curve", "def-sc-curves", "lem-pc-proper-base-change", "lem-sc-flat-base-change-coherent"]
+++
Let $k$ be a field, $X$ a
smooth projective curve over
$k$ which is geometrically irreducible with $H^0(X,\mathcal{O}_X)=k$, and let
$K/k$ be a field extension. Then
$g(X_K)=\dim_KH^1(X_K,\mathcal{O}_{X_K})=g(X)$. If $k$ is separably closed (or
more generally $H^0(X,\mathcal{O}_X)=k$), this applies in particular when
$X_K$ is a connected curve in the sense of [def-sc-curves].
