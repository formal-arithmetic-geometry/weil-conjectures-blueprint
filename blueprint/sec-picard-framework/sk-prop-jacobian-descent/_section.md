+++
id = "sk-prop-jacobian-descent"
kind = "proposition"
title = "The Jacobian over a general base field, by Galois descent"
order = 741
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-picard-pic", "sk-prop-av-projective", "sk-prop-picard-degree-decomposition", "sk-prop-picard-pic-split", "sk-thm-picard-main"]
lean = ["AlgebraicGeometry.exists_jacobian_descent"]
tags = ["sketch"]
+++
Let $k_0$ be any field, $k_s$ a separable closure and $\bar k_0$ an
algebraic closure containing it, and let $C_0$ be a proper smooth
geometrically connected curve of genus $g$ over $k_0$; put
$C=C_0\times_{k_0}\bar k_0$. The Jacobian $J(C)$ and its representing
isomorphism in [sk-prop-jacobian] descend canonically to $k_0$,
compatibly with base change; write $J_0$ for this descended abelian
variety. The induced identification $J_0(\bar k_0)=\Pic^0(C)$ is
*equivariant* for the natural actions of
$\operatorname{Gal}(k_s/k_0)$: on the left through the $k_0$-structure of
$J_0$, on the right through that of $C_0$. In particular, for every $n$
and every $\ell$, restricting to $\ell^n$-torsion gives a
$\operatorname{Gal}(k_s/k_0)$-equivariant isomorphism
$J_0[\ell^n](\bar k_0)\cong\Pic^0(C)[\ell^n]$. No rational point of
$C_0$ is assumed.
