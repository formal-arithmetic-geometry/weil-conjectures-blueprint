+++
id = "def-pc-invertible-in-degree-zero"
kind = "definition"
title = "Objects placed in degree $0$"
lean = ["AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFreeInDegree", "AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeInDegree_zero_one_iff"]
order = 778
uses = ["def-pc-derived-category", "def-pc-finite-locally-free", "def-sc-invertible-module"]
+++
Let $X$ be a scheme and let $(\mathcal{M}^q)_{q\ge0}$ be a family of
$\mathcal{O}_X$-modules, typically the cohomology sheaves
$\mathcal{M}^q=H^q(M)$ of an object $M\in D(\mathcal{O}_X)$ (or of a complex)
concentrated in non-negative degrees. For integers $i,r\ge0$, the family is
that of a *finite locally free rank $r$ module placed in degree $i$* if
$\mathcal{M}^q=0$ for $q\neq i$ and $\mathcal{M}^i$ is finite locally free of rank
$r$ ([def-pc-finite-locally-free]). The case $i=0$, $r=1$ is an
*invertible $\mathcal{O}_X$-module placed in degree $0$*: $\mathcal{M}^q=0$ for
$q\neq0$ and $\mathcal{M}^0$ is an invertible $\mathcal{O}_X$-module.

For $M\in D(\mathcal{O}_X)$ with $\mathcal{M}^q=H^q(M)$ this says exactly that
$M\cong E[-i]$ with $E=\mathcal{M}^i$ finite locally free of rank $r$ (a complex
whose cohomology is concentrated in degree $i$ is quasi-isomorphic to that
cohomology placed in degree $i$); in particular $M\cong\mathcal{N}[0]$ with
$\mathcal{N}$ invertible in the case $i=0$, $r=1$.
