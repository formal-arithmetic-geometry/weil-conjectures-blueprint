+++
id = "lem-chow-affine-cover"
kind = "lemma"
title = "Affine cover through the generic points"
order = 614
lean = ["AlgebraicGeometry.exists_isAffineOpen_cover_genericPoints_subset", "dense_iInf_of_genericPoints_subset"]
uses = ["lem-chow-affine-through-generic-points"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme with finitely many
irreducible components $Z_1,\dots,Z_r$, with generic points $\eta_j$. Then
there is a finite affine open covering $X=U_1\cup\dots\cup U_m$ such that
$\eta_j\in U_i$ for all $i$ and $j$. For any such covering the open

$$
U:=U_1\cap\dots\cap U_m
$$

is dense in $X$.

## Proof

By [lem-chow-affine-through-generic-points] every $x\in X$ has an affine
open neighbourhood containing all the $\eta_j$; since $X$ is quasi-compact,
finitely many of them cover $X$. For the density statement note that
$U\cap Z_j$ is an open subset of $Z_j$ containing $\eta_j$, hence is dense in
the irreducible space $Z_j$; as $X=Z_1\cup\dots\cup Z_r$, the closure of $U$
contains every $Z_j$ and therefore equals $X$.
