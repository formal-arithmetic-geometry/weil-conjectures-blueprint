+++
id = "sk-thm-curveestimate"
kind = "section"
title = "Curve estimate"
order = 1022
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-curve", "sk-def-kummer", "sk-def-pic", "sk-prop-cd", "sk-prop-h1", "sk-prop-h2", "sk-prop-jacobian", "sk-thm-av-final"]
lean = ["AlgebraicGeometry.curve_cohomology_constant"]
+++
*Theorem (sketch).*

Let $C$ be smooth proper connected of genus $g$ over algebraically
closed $k$, and let $n$ be prime to $\operatorname{char}k$. After
choosing a primitive $n$-th root of unity (the identification
$\mu_n\cong\Z/n$ of étale sheaves), the constant-sheaf cohomology
of $C$ is

$$
H^0(C,\Z/n)=\Z/n,\qquad
H^1(C,\Z/n)=(\Z/n)^{2g},\qquad
H^2(C,\Z/n)=\Z/n,
$$

and $H^q(C,\Z/n)=0$ for $q\ge3$.

Uses: [sk-def-curve], [sk-def-kummer], [sk-def-pic], [sk-prop-cd], [sk-prop-h1], [sk-prop-h2], [sk-prop-jacobian], [sk-thm-av-final]
