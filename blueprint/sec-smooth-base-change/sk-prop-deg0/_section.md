+++
id = "sk-prop-deg0"
kind = "proposition"
title = "Degree-zero flat base change"
order = 1437
uses = ["sk-def-bc"]
lean = ["AlgebraicGeometry.Etale.baseChangeProperty_zero", "AlgebraicGeometry.Etale.baseChangeProperty_zero_of_smooth"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring. For a Cartesian square as in
[sk-def-bc] (so $g$ is quasi-compact and quasi-separated) in which
$f:X\to S$ is flat and locally of finite presentation with geometrically
reduced fibres (in particular for $f$ smooth), the degree-zero
base-change map

$$
f^{-1}g_*\mathcal F\longrightarrow h_*e^{-1}\mathcal F
$$

is an isomorphism, for *every* sheaf $\mathcal F$ of $\Lambda$-modules on
$T_{\Et}$ — no torsion hypothesis is needed in degree zero. Hence
$\mathrm{BC}(f,\Lambda,0)$ holds for such $f$, in particular for smooth $f$.
