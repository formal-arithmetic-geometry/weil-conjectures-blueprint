+++
id = "sk-prop-h1"
kind = "proposition"
title = "$H^1$ via Kummer"
order = 1001
uses = ["sk-def-kummer", "sk-def-pic", "sk-prop-kummer-exact"]
lean = ["AlgebraicGeometry.Scheme.exists_exact_sheafH_rootsOfUnitySheaf_one"]
tags = ["sketch"]
+++
For $C$ as in [sk-def-curve] and every $n\ge1$ prime to
$\operatorname{char}k$ there is a canonical short exact sequence

$$
0\to\mathcal O_C(C)^\times/\mathcal O_C(C)^{\times n}\to H^1(C,\mu_n)
\to\Pic(C)[n]\to0 .
$$

In particular $H^1(C,\mu_n)\cong\Pic(C)[n]$ whenever
$\mathcal O_C(C)^\times$ is $n$-divisible, e.g. when $C$ is proper:
then $\mathcal O_C(C)$ is a finite $k$-algebra, whose unit group is a
product of copies of $k^\times$ and of a unipotent group $1+\mathfrak n$
($\mathfrak n$ nilpotent), both $n$-divisible since $k$ is algebraically
closed and $n$ is invertible in $k$.
