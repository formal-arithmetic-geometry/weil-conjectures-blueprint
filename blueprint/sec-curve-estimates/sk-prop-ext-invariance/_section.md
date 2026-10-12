+++
id = "sk-prop-ext-invariance"
kind = "proposition"
title = "Invariance under extension of algebraically closed fields"
order = 1035
uses = ["sk-def-av-jacobian", "sk-def-curve", "sk-def-kummer", "sk-def-pic", "sk-prop-cd-affine", "sk-prop-jacobian", "sk-prop-kummer-exact", "sk-thm-av-final", "sk-thm-curveestimate"]
tags = ["sketch"]
+++
Let $k\subseteq k'$ be an extension of algebraically closed fields,
let $C$ be a *smooth* separated curve over $k$ in the sense of
[sk-def-curve], and let $n\ge1$ be prime to $\operatorname{char}k$.
Then for every $q\ge0$ the *pullback map* along
$C_{k'}\to C$

$$
\rho^q_{k'/k}(C):\ H^q(C_{\Et},\Z/n\Z)\longrightarrow
H^q\bigl((C_{k'})_{\Et},\Z/n\Z\bigr)
$$

is an isomorphism. In particular the curve estimate of
[sk-thm-curveestimate] is compatible with algebraically closed
extension of the base field: the isomorphisms recorded there over
$k$ and over $k'$ are matched by $\rho^q$, not merely abstractly
isomorphic.
