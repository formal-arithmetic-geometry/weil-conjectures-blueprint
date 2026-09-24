+++
id = "lem-weil-pbc-chow-disjoint-affine-generics"
kind = "lemma"
title = "Disjoint affine neighbourhoods of generic points"
order = 1580
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $X$ be quasi-separated, let $Z_1,\dots,Z_n$ be pairwise distinct
irreducible components of $X$, and let $\eta_i\in Z_i$ be their generic
points. Then for every $i$ there is an affine open $V_i\subseteq X$ containing
$\eta_i$ such that $V_i\cap Z_k=\emptyset$ for $k\neq i$; in particular the
$V_i$ are pairwise disjoint.
(Stacks Project, Properties, Tag
[01ZV](https://stacks.math.columbia.edu/tag/01ZV) = Lemma 28.30.1.)

## Proof

For $k\neq i$ the point $\eta_i$ does not lie in the closed set $Z_k$, since
the $Z_l$ are pairwise distinct irreducible components and $\eta_i\in Z_i$;
hence $X\setminus Z_k$ is an open neighbourhood of $\eta_i$, as is the finite
intersection

$$
 W_i:=\bigcap_{k\neq i}(X\setminus Z_k),
$$

which satisfies $W_i\cap Z_k=\emptyset$ for all $k\neq i$. The affine open
subschemes of a scheme form a basis for its topology (every scheme is locally
$\operatorname{Spec}$ of a ring, in which the distinguished opens form a
basis), so there is an affine open $V_i$ with $\eta_i\in V_i\subseteq W_i$;
this gives $V_i\cap Z_k=\emptyset$ for $k\neq i$. For $i\neq j$ the open set
$V_i$ avoids $Z_j$, whereas $V_j\ni\eta_j\in Z_j$, so $V_i\cap V_j=\emptyset$,
i.e. the $V_i$ are pairwise disjoint.
