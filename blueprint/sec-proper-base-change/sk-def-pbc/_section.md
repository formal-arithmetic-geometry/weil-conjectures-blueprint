+++
id = "sk-def-pbc"
kind = "definition"
title = "The PBC property"
order = 1047
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange"]
uses = ["sk-def-conv", "sk-def-exchange"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring. For a morphism of schemes $f:X\to Y$,
write $\mathrm{PBC}_\Lambda(f)$ if for every cartesian square of
[sk-def-exchange] (every base change $g:Y'\to Y$ of $f$) and every object
$K\in\Dplus(X_{\Et},\Lambda)$ all of whose cohomology sheaves are torsion, the
exchange morphism $\Ex_{\square,K}$ is an isomorphism in
$\Dplus(Y'_{\Et},\Lambda)$. No hypothesis is imposed on $f$ or $g$. Here a
sheaf $F$ of $\Lambda$-modules on $X_{\Et}$ is *torsion* if its stalk at every
geometric point of $X$ is a torsion abelian group (torsion refers to the
underlying abelian group, not to the $\Lambda$-module structure); equivalently,
the canonical map $\varinjlim_nF[n]\to F$, $F[n]=\ker(n:F\to F)$, is an
isomorphism. This is weaker than asking that each group $F(U)$ be torsion.
