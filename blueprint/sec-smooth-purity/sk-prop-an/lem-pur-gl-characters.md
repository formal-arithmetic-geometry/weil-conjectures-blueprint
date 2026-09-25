+++
id = "lem-pur-gl-characters"
kind = "lemma"
title = "Characters of the general linear group"
order = 2061
uses = ["def-pur-conventions", "def-sc-general-linear-group", "def-sc-gm-ga", "lem-sc-gl-characters"]
+++
Let $k$ be a field and $c\geq1$. Every morphism of algebraic groups
$\mathrm{GL}_{c,k}\to\mathbb G_{m,k}$ is a power of the determinant; in
particular it is trivial on $\mathrm{SL}_{c,k}$.

## Proof

Write $k$ for the base field of [def-pur-conventions]. The
group schemes $\mathrm{GL}_{c,k}$ and $\mathbb G_{m,k}$ are those of
[def-sc-general-linear-group] and [def-sc-gm-ga], and a
morphism of algebraic groups is by definition a homomorphism of
$k$-group schemes, so the assertion is the first clause of
[lem-sc-gl-characters] of the group-schemes chapter, where it is
proved in full: after base change to an algebraic closure one restricts
to the diagonal torus, uses that homomorphisms from a split torus to
$\mathbb G_m$ are monomials, that permutation conjugation makes the
exponents equal, that every homomorphism $\mathbb G_a\to\mathbb G_m$
is trivial (so that elementary matrices are killed), and Gaussian
elimination; a morphism of finite-type $k$-schemes is then determined
by its values on rational points. The second clause follows because
$\mathrm{SL}_{c,k}$ is the closed subgroup scheme on which $\det$ is
trivial, so
$\mathrm{SL}_{c,k}\subseteq\ker(\chi)$ whenever
$\chi=\det^{r}$.
