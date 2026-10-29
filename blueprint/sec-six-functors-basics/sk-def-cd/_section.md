+++
id = "sk-def-cd"
kind = "definition"
title = "Cohomological dimension"
order = 2229
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

Here classical sheaves are those of [sk-def-pe-classical-definition]. For a field $k'$ we write
$\operatorname{cd}_\ell(k')=\operatorname{cd}_\ell(\Spec k')$.

By [sk-prop-sf-comparison] and [sk-thm-pe-direct-image-comparison], these are the usual
$\ell$-cohomological dimensions computed on the étale sites, so the classical bounds apply. If $k'$
is a field with $\operatorname{cd}_\ell(k')<\infty$, then $\operatorname{cd}_\ell(S)$ and
$\operatorname{cd}_\ell(g)$ are finite for all schemes $S$ and morphisms $g$ of finite type over $k'$
([Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10)).
