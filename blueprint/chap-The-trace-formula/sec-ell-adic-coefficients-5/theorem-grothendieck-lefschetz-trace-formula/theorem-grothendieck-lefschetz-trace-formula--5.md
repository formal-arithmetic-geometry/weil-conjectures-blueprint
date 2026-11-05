+++
id = "theorem-grothendieck-lefschetz-trace-formula--5"
kind = "theorem"
title = "Compact support: perfectness and cohomological finiteness"
order = 1017010
aliases = ["bp-r311-5"]
lean = ["AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections", "AlgebraicGeometry.WeilComplex.exists_subsingleton_compactlySupportedCohomology"]
uses = ["definition-constructible-sheaves", "definition-weil-structure"]
+++
For finite coefficients, let $k$ be separably closed, let $\Lambda$ be a finite commutative ring whose exponent is invertible in $k$, and let $a:Y\to\operatorname{Spec}k$ be locally of finite type and admit a compactification. For $M\in\Dctf(Y_{\acute{e}t},\Lambda)$, the complex $R\Gamma_c(Y_{\acute{e}t},M)$ is perfect over $\Lambda$.

For the $\Qlb$-Weil complex $K$ on $X=X_0\times_{\Fq}\overline{\Fq}$ used in the mainline trace formula, there are integers $a,b$ such that

$$
H_c^i(X,K)=0\qquad(i<a\text{ or }b<i).
$$

Each $H_c^i(X,K)$ is a finite-dimensional $\Qlb$-vector space with geometric Frobenius. These are the finite-coefficient perfectness and the cohomological finiteness statements available here; no uniform perfectness assertion for all the coefficient rings of the human statement is made by these declarations.
