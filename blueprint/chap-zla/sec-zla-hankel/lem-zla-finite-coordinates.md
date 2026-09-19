+++
id = "lem-zla-finite-coordinates"
kind = "lemma"
title = "Finite coordinates detect independent sequences"
order = 1002
+++
Let $v_1,\ldots,v_r\in K^{\mathbf N}$ be linearly independent. There exist
indices $n_1,\ldots,n_r\in\mathbf N$ such that

$$
\det\left(v_j(n_i)\right)_{1\leq i,j\leq r}\neq0.
$$

## Proof

Induct on $r$ by finite Gaussian elimination: given indices that work for
$v_1,\ldots,v_{r-1}$, subtract from $v_r$ the unique combination of
$v_1,\ldots,v_{r-1}$ agreeing with it at those indices; the residual sequence
is nonzero by independence, so it does not vanish at some further coordinate
$n_r$, and expanding the determinant along the last row gives a nonzero
value.
