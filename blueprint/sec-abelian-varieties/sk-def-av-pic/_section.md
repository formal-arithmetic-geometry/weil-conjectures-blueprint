+++
id = "sk-def-av-pic"
kind = "definition"
title = "$\\Pic$, degree, $\\Pic^0$"
lean = ["AlgebraicGeometry.Scheme.Pic", "AlgebraicGeometry.Scheme.Hom.picZero"]
order = 534
uses = ["sec-nagata-compactification", "sk-def-curve"]
tags = ["sketch"]
+++
Let $C$ be a scheme over a field $k$. We write $\Pic(C)$ for the set of
invertible $\cO_C$-modules up to isomorphism (for $C$ a smooth projective
geometrically integral curve this is the group $H^1(C_{\Et},\gm)$). The
*degree* of a class is $\deg\cL:=\chi(C,\cL)-\chi(C,\cO_C)$, and
$\Pic^0(C):=\{\cL\in\Pic(C):\deg\cL=0\}$. For a field extension $K/k$ we
write $C_K=C\times_kK$ and $\Pic^0(C_K)$ for the degree-zero part over $K$.
