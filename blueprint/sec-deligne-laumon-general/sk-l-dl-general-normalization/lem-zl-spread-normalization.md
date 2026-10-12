+++
id = "lem-zl-spread-normalization"
kind = "lemma"
title = "Spreading affine normalization to a principal open"
order = 3164
lean = ["Algebra.FiniteType.exists_finite_aeval_away"]
uses = ["def-weil-pbc-scheme-conventions", "def-zl-localized-coordinates"]
+++
Let $A$ be a domain and $B$ a finitely generated commutative
$A$-algebra. There are $0\neq s_0\in A$, $d\geq0$, and
$t_1,\ldots,t_d\in B$ with the following property: for every nonzero
multiple $s$ of $s_0$ in $A$, with $t$ also denoting the images of the
$t_i$ in $B_s$, the map $\nu_t$ is finite, i.e. $B_s$ is a finitely
generated module over $A_s[T_1,\ldots,T_d]$ via $T_i\mapsto t_i$.
If moreover $A\to B$ is injective, then
$A_s[T_1,\ldots,T_d]\to B_s$ is injective as well.
