+++
id = "lem-pc-euler-characteristic-well-defined"
kind = "lemma"
title = "Well-definedness of the Euler characteristic"
order = 741
uses = ["def-pc-morphism-conventions", "lem-pc-coherent-hi", "lem-pc-curve-coherent-finiteness"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ and $\mathcal{F}$ a coherent
$\mathcal{O}_X$-module. Then the set
$\{i:H^i(X,\mathcal{F})\neq0\}$ is finite and each $H^i(X,\mathcal{F})$ is a finite
dimensional $k$-vector space; hence
$\chi(X,\mathcal{F})=\sum_i(-1)^i\dim_kH^i(X,\mathcal{F})$ is well defined.
