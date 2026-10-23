+++
id = "lem-chow-disjoint-affines"
kind = "lemma"
title = "Disjoint affine neighbourhoods of generic points"
order = 405
lean = ["AlgebraicGeometry.exists_isAffineOpen_of_subset_genericPoints", "AlgebraicGeometry.exists_isAffineOpen_pairwise_disjoint"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $X$ be a quasi-separated scheme, let $Z_1,\dots,Z_n$ be pairwise distinct
irreducible components of $X$ and let $\eta_i\in Z_i$ be their generic points.
Then there are affine opens $U_i\subseteq X$ with $\eta_i\in U_i$ and
$U_i\cap U_j=\emptyset$ for $i\neq j$. Consequently
$U_1\cup\dots\cup U_n$ is an affine open containing all the $\eta_i$.
