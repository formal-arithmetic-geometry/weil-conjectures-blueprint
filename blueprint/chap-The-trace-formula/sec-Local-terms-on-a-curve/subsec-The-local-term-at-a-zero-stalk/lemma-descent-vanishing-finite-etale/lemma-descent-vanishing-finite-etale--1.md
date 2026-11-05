+++
id = "lemma-descent-vanishing-finite-etale--1"
kind = "lemma"
title = "Finite étale trace on derived sections"
name_showing = false
order = 986001
aliases = ["bp-r301-1"]
lean = ["AlgebraicGeometry.Etale.exists_rightDerivedPullback_app_comp_eq_smul", "AlgebraicGeometry.Etale.exists_sectionsRestriction_app_comp_eq_smul"]
+++
Let $A$ be a commutative ring, let $f:W'\to W$ be a finite étale
morphism of schemes, and let $n\in\mathbf N$. Suppose that, for every
separably closed field $\Omega$ and every geometric point
$\bar w:\operatorname{Spec}(\Omega)\to W$, the geometric fibre of $f$
over $\bar w$ has $n$ points. For every $L\in D(W_{\acute{e}t},A)$, the
pullback map

$$
p:R\Gamma(W,L)\longrightarrow R\Gamma(W',f^{-1}L)
$$

admits a trace $t:R\Gamma(W',f^{-1}L)\to R\Gamma(W,L)$ in $D(A)$ such
that $t\circ p=n\,\operatorname{id}_{R\Gamma(W,L)}$.

The same assertion holds for the restriction map of derived sections
evaluated at the terminal étale objects $W\to W$ and $W'\to W'$.
There is no invertibility assumption on $n$, and $L$ need not be bounded.
