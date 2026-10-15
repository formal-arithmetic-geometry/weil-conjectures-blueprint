+++
id = "sk-def-pbc-curve-assertions"
kind = "definition"
title = "The eight curve-cohomology assertions"
order = 1143
lean = ["AlgebraicGeometry.IsCurve.Assertions"]
tags = ["sketch"]
+++
For a curve coefficient pair $(C,F)$ ($k$ algebraically closed, $C$ separated
of finite type over $k$ with $\dim C\le1$, $F$ a torsion sheaf on $C_{\Et}$),
the assertions $(C_1)$–$(C_8)$ are eight separate definitions, each a property
of $(C,F)$: vanishing above degree $2$, vanishing above degree $1$ for affine
$C$ and for $p$-primary $F$, finiteness for constructible $F$ (prime to $p$, or
$C$ proper), invariance under algebraically closed field extension (prime to
$p$, or $C$ proper), and surjectivity of $H^2$ restriction to opens. Their
conjunction is $\mathcal C(C,F)$ ([def-weil-pbc-eight-curve-assertions]).
The curve estimate proves each one first for constant sheaves, then by
dévissage for general torsion sheaves.
