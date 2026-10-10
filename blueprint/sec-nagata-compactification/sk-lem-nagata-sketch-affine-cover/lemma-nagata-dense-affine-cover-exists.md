+++
id = "lemma-nagata-dense-affine-cover-exists"
kind = "lemma"
title = "Existence of a finite affine cover with dense total intersection"
order = 318
lean = ["AlgebraicGeometry.exists_isAffineOpen_cover_genericPoints_subset", "AlgebraicGeometry.exists_isAffineOpen_iSup_eq_top_and_genericPoints_subset_iInter", "dense_iInf_of_genericPoints_subset"]
uses = ["def-weil-pbc-scheme-conventions", "lem-chow-affine-through-generic-points", "lemma-nagata-affine-neighbourhood-generic-points"]
+++
Let $X$ be a quasi-compact scheme with finitely many irreducible
components $Z_1,\dots,Z_r$, with generic points $\eta_j$. Then there is a
finite affine open covering $X=U_1\cup\dots\cup U_m$ such that
$\eta_j\in U_i$ for all $i$ and $j$; in particular the total intersection

$$
U:=U_1\cap\dots\cap U_m
$$

is dense in $X$. More generally, in any scheme the intersection of finitely
many open subsets each of which contains the generic points of all
irreducible components is dense.

## Proof

**Step 1: an affine open through $x$ and all generic points.** Let
$x\in X$. A generic point $\eta_j$ lies in no irreducible component other
than $Z_j$: if $\eta_j\in Z_k$ then $Z_j=\overline{\{\eta_j\}}\subseteq Z_k$,
so $j=k$. The union $B$ of the finitely many components not containing $x$
is closed and misses $x$, so there is an affine open $W\ni x$ with
$W\cap B=\emptyset$. Every point of $W$ lies on some component, which then
contains $x$; hence $W$, and therefore its closure $\overline W$, lies in
the union of the components through $x$. If $x\in Z_j$, then $W\cap Z_j$ is
a nonempty open subset of the irreducible space $Z_j$, so it contains
$\eta_j$.

Now let $\eta_k$ be the generic point of a component with $x\notin Z_k$.
Then $\eta_k\notin\overline W$ (it lies on no component through $x$) and
$\eta_k$ lies on no component other than $Z_k$, so
$\overline W\cup\bigcup_{l\neq k}Z_l$ is a closed set missing $\eta_k$, and
there is an affine open $V_k\ni\eta_k$ disjoint from it. Every point of
$V_k$ lies on some component, which can only be $Z_k$; thus $V_k\subseteq
Z_k\setminus\bigcup_{l\neq k}Z_l$. Consequently the $V_k$ are pairwise
disjoint, and each is disjoint from $W$. A finite disjoint union of affine
opens is affine (Stacks, Tag
[01I5](https://stacks.math.columbia.edu/tag/01I5)), so
$U_x:=W\cup\bigcup_{x\notin Z_k}V_k$ is an affine open containing $x$ and
all the $\eta_j$.

**Step 2: the cover.** Since $X$ is quasi-compact, finitely many of the
$U_x$ cover $X$; call them $U_1,\dots,U_m$. Each contains every $\eta_j$.

**Step 3: density.** Let $U$ be a finite intersection of open subsets each
containing the generic points of all irreducible components (in an
arbitrary scheme), so $U$ is open and contains all these generic points.
Every point $y$ lies on some irreducible component $Z$, with generic point
$\eta\in U$; then $U\cap Z$ is a nonempty open subset of the irreducible
space $Z$, hence dense in $Z$, so $y\in\overline{U\cap Z}\subseteq
\overline U$. Thus $U$ is dense. Applied to $U_1,\dots,U_m$ this gives the
density of $U_1\cap\dots\cap U_m$.

When $X$ is moreover quasi-separated, Step 1 is also
[lem-chow-affine-through-generic-points] applied to all the $\eta_j$.
