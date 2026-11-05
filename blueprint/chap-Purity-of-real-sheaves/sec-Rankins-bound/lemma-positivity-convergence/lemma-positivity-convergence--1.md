+++
id = "lemma-positivity-convergence--1"
kind = "lemma"
title = "Positive products and zero-free discs"
order = 1162001
aliases = ["bp-r357-1"]
lean = ["PowerSeries.eval_ne_zero_of_lt_radius_inv", "PowerSeries.radius_tprod_le_radius"]
+++
For a power series $f$, write $\rad(f)\in[0,\infty]$ for its radius
of convergence.

Let $(f_j)_{j\in J}$ be a family in $1+t\mathbf R_{\ge0}[[t]]$,
viewed as complex power series. Suppose that the finite subproducts
converge coefficientwise in the usual topology on $\mathbf C$ to $L$.
Then, for every $j\in J$,

$$
\rad(L)\le\rad(f_j).
$$

Independently, let $K$ be a complete nontrivially normed field and
$P\in K[t]$ with $P(0)\ne0$. Then

$$
|z|<\rad(P^{-1})\quad\Longrightarrow\quad P(z)\ne0
\qquad(z\in K),
$$

where $P^{-1}$ is the formal power series inverse of $P$.
In particular, if $f_j=P_j^{-1}$ for $P_j\in\mathbf C[t]$ with
$P_j(0)=1$, then $P_j$ has no zero on $|t|<\rad(L)$.
