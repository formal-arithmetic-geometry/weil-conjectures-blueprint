+++
id = "sk-p-linear-filtration"
kind = "lemma"
title = "Filtrations and spectra"
order = 636
lean = ["LinearMap.charpoly_eq_charpoly_restrict_mul_charpoly_mapQ", "Module.End.hasEigenvalue_of_subquotient"]
uses = ["sk-p-linear-triangular", "sec-trace-formula"]
tags = ["sketch"]
+++
Let $V$ have a finite filtration preserved by an automorphism $u$.
Then

$$
\det(1-Tu\mid V)=\prod_a\det(1-Tu\mid\operatorname{gr}_aV).
$$

In particular, the eigenvalues, with algebraic multiplicity, are the
union of the eigenvalues on the graded pieces. If the eigenvalues of
$u$ on $V$ are $\alpha_1,\ldots,\alpha_d$, then those on $V^\vee$ are
$\alpha_i^{-1}$, and those on $\bigwedge^rV$ are
$\alpha_{i_1}\cdots\alpha_{i_r}$ for $i_1<\cdots<i_r$.
If $v$ on $V'$ has eigenvalues $\beta_j$, those of $u\otimes v$ are
$\alpha_i\beta_j$.

*Complement.* The factorization holds for any endomorphism $f$ of $V$ and
an $f$-stable subspace $S$, in the form
$\det(T-f\mid V)=\det(T-f\mid S)\,\det(T-f\mid V/S)$, and more generally
over a commutative ring for a finite free module $V$ and an $f$-stable
submodule $S$ with $S$ and $V/S$ finite free. If $U\subsetneq S\subseteq V$
are $f$-stable subspaces and $f$ acts on the nonzero subquotient $S/U$ as a
scalar $c$, then $c$ is an eigenvalue of $f$ on $V$. The dual eigenvalues
refer to the contragredient $u^\vee=(u^{-1})^*$; in particular $\alpha^n$ is
an eigenvalue of $u^{\otimes n}$, and in an exterior basis a diagonal map
with entries $c_1,\ldots,c_d$ has entries $c_{i_1}\cdots c_{i_r}$ with
$i_1<\cdots<i_r$.
