+++
id = "det-prop-h1"
kind = "proposition"
title = "$H^1$ via Kummer"
order = 1402
uses = ["def-sc-kummer-sequence", "det-def-pic"]
lean = ["AlgebraicGeometry.Scheme.exists_exact_sheafH_rootsOfUnitySheaf_one", "AlgebraicGeometry.Scheme.nonempty_addEquiv_sheafH_rootsOfUnitySheaf_one", "AlgebraicGeometry.nonempty_addEquiv_sheafH_rootsOfUnitySheaf_one_of_isProper", "IsAlgClosed.exists_pow_eq_of_finite"]
+++
For a scheme $C$ (for instance a curve as in [def-sc-curves]) and every
$n\ge1$ invertible on $C$ (for a curve over $k$: $n$ prime to
$\operatorname{char}k$), with $\mu_n$ as in [def-sc-kummer-sequence] and
$\Pic(C)=H^1(C_{\Et},\mathbb G_m)$ as in [det-def-pic], there is a
canonical short exact sequence

$$
0\to\mathcal O_C(C)^\times/\mathcal O_C(C)^{\times n}\to H^1(C,\mu_n)
\to\Pic(C)[n]\to0 .
$$

In particular $H^1(C,\mu_n)\cong\Pic(C)[n]$ whenever
$\mathcal O_C(C)^\times$ is $n$-divisible, e.g. when $C$ is proper over
the algebraically closed field $k$: then $\mathcal O_C(C)$ is a finite $k$-algebra, whose unit group is a
product of copies of $k^\times$ and of a unipotent group $1+\mathfrak n$
($\mathfrak n$ nilpotent), both $n$-divisible since $k$ is algebraically
closed and $n$ is invertible in $k$.
