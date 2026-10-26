+++
id = "lem-sc-isogeny-degree"
kind = "lemma"
title = "The degree of an isogeny"
lean = ["AlgebraicGeometry.IsIsogeny.finrank_eq", "AlgebraicGeometry.IsIsogeny.isFinite", "AlgebraicGeometry.IsIsogeny.flat", "AlgebraicGeometry.IsIsogeny.isFiniteLocallyFreeOfDegree"]
order = 531
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-isogeny", "lem-sc-finite-constant-length-flat", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $f:A\to B$ be an isogeny of
abelian varieties over a field
$k$, with kernel $K=\ker f$ ([def-sc-group-scheme]), and
let $d:=\dim_k\mathcal O(K)$, the order of $K$, i.e. the
degree of $f$ in the sense of [def-sc-isogeny]. Then $f$
is finite and flat and $f_*\mathcal O_A$ is a locally free
$\mathcal O_B$-module of rank $d$: the degree of the finite
flat morphism $f$ is $d$.
