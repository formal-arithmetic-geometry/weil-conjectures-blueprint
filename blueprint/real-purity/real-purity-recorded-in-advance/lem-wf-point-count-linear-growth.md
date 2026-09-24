+++
id = "lem-wf-point-count-linear-growth"
kind = "lemma"
title = "Linear growth of the point count on an affine curve"
order = 4167
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $U_0$ be a smooth affine curve over $k_0=\mathbf F_q$ (in the
separated finite-type
conventions of [def-weil-pbc-scheme-conventions]) and let
$k_n=\mathbf F_{q^n}$. Then there is a constant $d\ge1$ such that

$$
\#U_0(k_n)\le d\,q^n\qquad(n\ge1).
$$

## Proof

The affine curve is $\operatorname{Spec}(R)$ for the finite-type
$k_0$-algebra $R=\Gamma(U_0,\mathcal O_{U_0})$ of dimension one (in
the finite-type conventions of
[def-weil-pbc-scheme-conventions]). By
the Noether normalization theorem in dimension one (Stacks Project,
Commutative Algebra, [Tag
00OY](https://stacks.math.columbia.edu/tag/00OY): the standard statement [the same classical input as in the proof
of the cohomological-dimension bounds of the Jacobian chapter]) there is a
finite injective $k_0$-algebra map $k_0[t]\hookrightarrow R$ with
$R$ a finite $k_0[t]$-module; put $d=[R:k_0[t]]$ and let
$f:U_0\to\mathbf A^1_{k_0}$ be the corresponding finite surjective
morphism. For every $n$ and every $y\in\mathbf A^1_{k_0}(k_n)$ the
fiber of $f$ over $y$ has at most $d$ $k_n$-points (the closed
points of $\operatorname{Spec}(R\otimes_{k_0}k_n)$ above $y$ are at
most the rank $d$ of the free
$k_n[t]$-module $R\otimes_{k_0}k_n$, after the standard localization
in $y$), and $\mathbf A^1_{k_0}(k_n)$ has $q^n$ points, which
gives the estimate.

*Recorded in advance* from chapter *Boundary weights, constant twists, and real envelopes* of the source.
