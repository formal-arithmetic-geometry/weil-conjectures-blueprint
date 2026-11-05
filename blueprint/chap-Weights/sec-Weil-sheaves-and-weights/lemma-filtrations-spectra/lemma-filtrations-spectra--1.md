+++
id = "lemma-filtrations-spectra--1"
kind = "lemma"
title = "Filtrations and spectra (1)"
name_showing = false
order = 1068001
aliases = ["bp-r328-1"]
lean = ["LinearMap.charpoly_eq_prod_charpoly_mapQ_of_le"]
+++
Let $K$ be a field, $V$ a finite-dimensional $K$-vector space, and
$u:V\to V$ a linear endomorphism. Let $(F_i)_{i\geq0}$ be subspaces
preserved by $u$, with $F_0=0$, $F_n=V$, and $F_i\subseteq F_{i+1}$
for $0\leq i<n$. Write $u_i$ for the induced endomorphism of
$\operatorname{gr}_iV=F_{i+1}/F_i$. Then

$$
\det(T-u\mid V)=\prod_{i=0}^{n-1}
\det(T-u_i\mid\operatorname{gr}_iV).
$$

Reversing these characteristic polynomials gives the identity for
$\det(1-Tu\mid V)$. Invertibility of $u$ is not required.
