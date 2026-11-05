+++
id = "corollary-triviality-over-open-cover-base--1"
kind = "corollary"
title = "Gluing isomorphisms along a fixed slice"
name_showing = false
order = 1478001
aliases = ["bp-r460-1"]
lean = ["AlgebraicGeometry.nonempty_iso_of_forall_exists_nonempty_iso_preimageSnd"]
uses = []
+++
The pushforward formulation above is bypassed by the Lean proof, which
uses the following gluing statement.

Let $k$ be a field, let $X$ and $Y$ be proper geometrically integral
$k$-schemes, let $Z$ be a $k$-scheme, and let $x\in X(k)$.
Let $\mathcal M$ and $\mathcal N$ be invertible sheaves on
$X\times Y\times Z$. Suppose that for every
$t\in Z$ there is an open neighbourhood $U$ of $t$ such that
$$
\mathcal M|_{X\times Y\times U}\simeq
\mathcal N|_{X\times Y\times U},
$$
and that their restrictions to $\{x\}\times Y\times Z$ are isomorphic.
Then $\mathcal M\simeq\mathcal N$.
