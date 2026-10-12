+++
id = "sk-def-smooth"
kind = "definition"
title = "Smooth and allowed coefficients"
order = 1413
lean = ["AlgebraicGeometry.Scheme.IsTorsionSheafOfInvertibleOrder"]
tags = ["sketch"]
+++
A morphism is *smooth* if it is flat, locally of finite
presentation and its geometric fibres are smooth varieties. A sheaf
of $\Lambda$-modules on $T_{\Et}$, for a scheme $T$ and a commutative
ring $\Lambda$, has *allowed torsion* with respect to a base scheme $S$ if
all its geometric stalks are torsion of orders invertible on $S$.
"Invertible on $S$" is read globally: each element of each geometric
stalk is killed by some positive integer invertible on all of $S$
(a unit of $\Gamma(S,\mathcal O_S)$), with no common annihilator
required.

For every $d$ the projection $\Aaf^d_S\to S$ is smooth. The global
reading is stronger than invertibility of the orders near the support:
on $S=\Spec\Z$ the sheaf $j_!(\Z/2)$, $j:D(2)\hookrightarrow S$, has the
latter property but not the former. A sheaf $\mathcal F$ with allowed
torsion is the filtered union $\mathcal F=\varinjlim_d\mathcal F[d]$ of
its $d$-torsion subsheaves over the integers $d$ invertible on $S$.
