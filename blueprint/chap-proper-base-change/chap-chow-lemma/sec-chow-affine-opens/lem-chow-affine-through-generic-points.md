+++
id = "lem-chow-affine-through-generic-points"
kind = "lemma"
title = "An affine open containing a point and all generic points"
order = 613
lean = ["AlgebraicGeometry.exists_isAffineOpen_mem_of_subset_genericPoints"]
uses = ["lem-chow-disjoint-affines"]
+++
Let $X$ be a quasi-separated scheme, let $Z_1,\dots,Z_n$ be pairwise distinct
irreducible components of $X$ with generic points $\eta_i$, and let $x\in X$.
Then there is an affine open $U\subseteq X$ containing $x$ and all the
$\eta_i$.

## Proof

After renumbering we may assume $x\in Z_i$ for $i\leq r$ and $x\notin Z_k$ for
$k>r$. Then $\bigcap_{k>r}(X\setminus Z_k)$ is an open neighbourhood of $x$,
so there is an affine open $W$ with
$x\in W\subseteq\bigcap_{k>r}(X\setminus Z_k)$; thus $W\cap Z_k=\emptyset$ for
$k>r$. For $i\leq r$ the set $W\cap Z_i$ is a nonempty open subset of the
irreducible space $Z_i$, hence contains its generic point, so $\eta_i\in W$.

By [lem-chow-disjoint-affines] applied to $Z_{r+1},\dots,Z_n$ there are
pairwise disjoint affine opens $U_k\ni\eta_k$ for $k>r$. Fix $k>r$. Since $X$
is quasi-separated, $W\cap U_k$ is a quasi-compact open of $U_k$, and it does
not contain $\eta_k$ because $\eta_k\in Z_k$ while $W\cap Z_k=\emptyset$. As
in the proof of [lem-chow-disjoint-affines], $\eta_k$ is a minimal prime
of the affine scheme $U_k$, so 00EV provides a standard affine
open $U_k'\subseteq U_k$ with $\eta_k\in U_k'$ and $U_k'\cap W=\emptyset$.

The opens $W$ and $U_k'$ for $k>r$ are pairwise disjoint and affine, so

$$
U:=W\cup\bigcup_{k>r}U_k'
$$

is affine by 01I5, and it contains $x$ and all the $\eta_i$.
