+++
id = "sk-prop-injectivity"
kind = "proposition"
title = "Injectivity of the critical map"
order = 1423
uses = ["sk-def-bc"]
lean = ["AlgebraicGeometry.Etale.mono_baseChangeHomologyMap", "AlgebraicGeometry.Etale.mono_cokernelMap", "AlgebraicGeometry.Etale.mono_cokernelDesc"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring, let $q\ge1$ and assume
$\mathrm{BC}(f,\Lambda,q-1)$ of [sk-def-bc] holds. Then for every square
as there (with $g$ quasi-compact and quasi-separated) and every sheaf
$\mathcal F$ of $\Lambda$-modules on $T_{\Et}$:

1. the base-change map
$f^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is *injective*;
1. if $\mathcal F\subseteq\mathcal G$ with $\mathcal G$ a sheaf of
$\Lambda$-modules, the cokernel for $\mathcal F$ is contained in the cokernel for
$\mathcal G$;
1. if moreover $\mathcal G$ is an injective sheaf of
$\Lambda$-modules, that cokernel is contained in
$R^qh_*e^{-1}\mathcal G$.

Consequently a failure of $\mathrm{BC}(f,\Lambda,q)$ is witnessed by a nonzero
element of the cokernel in the stalk at a geometric point of $X$.
