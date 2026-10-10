+++
id = "sk-thm-intfactors"
kind = "theorem"
title = "Integral Frobenius factors"
order = 2901
lean = ["AlgebraicGeometry.IsWeilFactorization.unique", "TraceDatum.exists_isWeilFactorization"]
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-prop-rootpurity", "sk-prop-separation", "sk-thm-rationality"]
tags = ["sketch"]
+++
For every $0\le i\le2d$ there is a unique polynomial $P_i(T)\in\Z[T]$ with
$P_i(0)=1$ such that for *every* prime $\ell\ne p$

$$
P_i^{(\ell)}(T)=\det\bigl(1-TF_{i,\ell}\mid H^{i}(X,\Ql)\bigr),
$$

and then

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}},
$$

a factorization that is independent of $\ell$.
