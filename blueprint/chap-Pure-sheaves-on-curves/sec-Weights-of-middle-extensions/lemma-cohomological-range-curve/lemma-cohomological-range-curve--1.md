+++
id = "lemma-cohomological-range-curve--1"
kind = "lemma"
title = "Cohomological range in dimension at most one"
name_showing = false
order = 1189001
aliases = ["bp-r367-1"]
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_krullDim_le_one", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isAffine"]
uses = ["definition-weil-structure", "proposition-construction-independence-rf-shriek"]
+++
Let $k_0=\Fq$, let $k$ be an algebraic closure of $k_0$, and let
$\ell$ be a prime different from the characteristic of $k_0$.
Let $X_0$ be a separated scheme of finite type over $k_0$ with
$\dim X_0\leq1$, put $X=X_0\times_{k_0}k$, and let $F$ be a
constructible Weil $\overline{\mathbf Q}_\ell$-sheaf on $X_0$.
Then

$$
H^r_c(X,F)=0\qquad\text{for every }r\in\mathbf Z\setminus\{0,1,2\}.
$$

In particular, this holds when $X_0$ is affine and smooth of relative
dimension one over $k_0$.
