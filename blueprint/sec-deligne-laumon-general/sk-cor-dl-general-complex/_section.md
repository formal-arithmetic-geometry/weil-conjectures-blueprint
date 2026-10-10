+++
id = "sk-cor-dl-general-complex"
kind = "section"
title = "The derived direct-image bound"
order = 2850
lean = ["AlgebraicGeometry.LAdicWeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek"]
uses = ["sk-d-dl-general-weights", "sk-thm-dl-general-sheaf"]
+++
*Corollary (sketch).*

Let $f_0:X_0\to Y_0$ be a separated finite-type morphism of
$k_0$-schemes, with $Y_0$ separated of finite type over $k_0$.
If $K_0$ is a bounded constructible Weil complex on $X_0$ that is
$\iota$-mixed of weights at most $w$, then $Rf_{0!}K_0$ is $\iota$-mixed
of weights at most $w$.

## Proof

In the finite hypercohomology spectral sequence

$$
R^af_{0!}\mathcal H^b(K_0)
\ \Longrightarrow\ \mathcal H^{a+b}(Rf_{0!}K_0),
$$

the term on the left has weights at most $w+b+a$.
Subquotients and extensions give the bound $w+n$ in total degree $n$,
which is precisely the derived convention.
