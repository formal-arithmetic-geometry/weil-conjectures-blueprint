+++
id = "lemma-filtrations-spectra"
kind = "lemma"
title = "Filtrations and spectra"
order = 1068
lean = ["LinearMap.charpoly_eq_charpoly_restrict_mul_charpoly_mapQ"]
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
