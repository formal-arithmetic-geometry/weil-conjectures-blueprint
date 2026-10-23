+++
id = "sk-def-cd"
kind = "definition"
title = "Cohomological dimension"
order = 2119
uses = ["sk-def-pe-classical-definition", "sk-prop-sf-comparison", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
For a qcqs scheme $S$ and a qcqs morphism $g\colon X\to Y$, the
*$\ell$-cohomological dimensions* are

$$
\begin{aligned}
\operatorname{cd}_\ell(S)&=\sup\{q: H^q(S_{\Proet},F)\neq0
  \text{ for some classical $\ell$-power torsion sheaf $F$}\},\\
\operatorname{cd}_\ell(g)&=\sup\{q: R^qg_*F\neq0
  \text{ for some classical $\ell$-power torsion sheaf $F$ on }X_{\Proet}\}.
\end{aligned}
$$

For a field $K$ we write $\operatorname{cd}_\ell(K)=\operatorname{cd}_\ell(\Spec K)$.

By the cohomology comparison and the direct-image comparison these are the usual
$\ell$-cohomological dimensions computed on the étale sites, so the classical
bounds apply. If $K$ is a field with $\operatorname{cd}_\ell(K)<\infty$, then
$\operatorname{cd}_\ell(S)$ and $\operatorname{cd}_\ell(g)$ are finite for all
schemes $S$ and morphisms $g$ of finite type over $K$ (Stacks Project, Tag
0F10).
