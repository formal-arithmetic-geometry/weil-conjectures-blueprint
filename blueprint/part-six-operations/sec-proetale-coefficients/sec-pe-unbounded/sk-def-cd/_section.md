+++
id = "sk-def-cd"
kind = "definition"
title = "Cohomological dimension"
lean = ["AlgebraicGeometry.ProEtale.cohomologicalDimension"]
order = 105
uses = ["sk-def-pe-classical-definition", "sk-prop-sf-comparison", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
For a qcqs scheme $S$ and a qcqs morphism $g:X\to Y$, the
*$\ell$-cohomological dimensions* are

$$
\begin{aligned}
\operatorname{cd}_\ell(S)&=\sup\{q: H^q(S_{\mathrm{pro}\acute{e}t},F)\neq0
\text{ for some classical $\ell$-power torsion sheaf $F$}\},\\
\operatorname{cd}_\ell(g)&=\sup\{q: R^qg_*F\neq0
\text{ for some classical $\ell$-power torsion sheaf $F$ on }X_{\mathrm{pro}\acute{e}t}\}.
\end{aligned}
$$

For a field $k'$ we write $\operatorname{cd}_\ell(k')=\operatorname{cd}_\ell(\operatorname{Spec}k')$.
