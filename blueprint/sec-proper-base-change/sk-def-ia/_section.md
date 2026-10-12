+++
id = "sk-def-ia"
kind = "definition"
title = "Injective acyclicity"
order = 1081
lean = ["AlgebraicGeometry.Etale.HasInjectiveAcyclicity"]
uses = ["sk-def-conv", "sk-def-exchange"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring. For a morphism of schemes $f:X\to Y$,
write $\mathrm{IA}_\Lambda(f)$ if for every base change $g:Y'\to Y$ — with
$f':X'\to Y'$ and $g':X'\to X$ the two other sides of the cartesian square of
[sk-def-exchange], so that $X'=X\times_YY'$, $f'$ is the base change of $f$
and $g'$ the base change of $g$ — every injective sheaf $I$ of
$\Lambda$-modules on $X_{\Et}$ which is torsion (every geometric stalk is a
torsion abelian group) satisfies

$$
R^qf'_*\,g'^{-1}I=0\qquad(q>0),
$$

where $R^qf'_*G$ is the $q$-th cohomology sheaf of $Rf'_*$ applied to $G$
placed in degree $0$. No hypothesis is imposed on $f$.
