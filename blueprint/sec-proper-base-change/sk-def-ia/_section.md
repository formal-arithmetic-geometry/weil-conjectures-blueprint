+++
id = "sk-def-ia"
kind = "definition"
title = "Injective acyclicity"
order = 1657
lean = ["AlgebraicGeometry.Etale.HasInjectiveAcyclicity"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc"]
tags = ["sketch"]
+++
For a ring $\Lambda$, write $\mathrm{IA}_\Lambda(f)$ if for every cartesian
square as in [sk-def-exchange] and every injective sheaf $I$ of
$\Lambda$-modules on $X_{\Et}$ which is torsion [sk-def-pbc], one has

$$
R^qf'_*g'^{-1}I=0\qquad(q>0).
$$

The pullback $g'^{-1}I$ of an injective sheaf is in general not injective.
Injective acyclicity asks only that it be $f'_*$-acyclic. By
[sk-thm-acyclicity] this is enough to compute $Rf'_*$ of the pullback of an
injective resolution term by term.
