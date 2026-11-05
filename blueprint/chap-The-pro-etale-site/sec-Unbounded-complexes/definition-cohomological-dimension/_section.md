+++
id = "definition-cohomological-dimension"
kind = "definition"
title = "Cohomological dimension"
order = 157
lean = ["AlgebraicGeometry.ProEtale.cohomologicalDimension", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension"]
uses = ["lemma-stability"]
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
