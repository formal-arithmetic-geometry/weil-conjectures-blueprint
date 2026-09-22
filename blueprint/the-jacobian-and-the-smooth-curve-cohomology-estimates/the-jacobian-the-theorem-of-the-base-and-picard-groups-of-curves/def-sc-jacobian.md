+++
id = "def-sc-jacobian"
kind = "definition"
title = "The Jacobian"
order = 4506
lean = ["AlgebraicGeometry.Curve.IsJacobian"]
uses = ["def-sc-general-curve"]
+++
Let $C$ be a geometrically integral smooth projective curve
[def-sc-general-curve] over a field $k$, of genus $g=g(C)$. A *Jacobian of
$C$* is a pair $(J,\varphi)$ consisting of an abelian variety $J$ over $k$
of dimension $g$ together with an isomorphism of group-valued functors
$$
\varphi:\operatorname{Pic}^0_{C/k}\xrightarrow{\ \sim\ }h_J,
$$
where $\operatorname{Pic}^0_{C/k}$ is the degree-zero part of the Picard
functor; that is, a Jacobian of $C$ is a representing object of
$\operatorname{Pic}^0_{C/k}$ in the category of abelian varieties of
dimension $g$ over $k$, together with the representing isomorphism. Whether
such a pair exists, and which properties it has, is not part of this
definition.

When a Jacobian $(J,\varphi)$ of $C$ is fixed, we write $J_C:=J$ and call
$J_C$ the *Jacobian* of $C$, so that $\varphi$ is the canonical
identification $\operatorname{Pic}^0_{C/k}\cong h_{J_C}$.

Unresolved dependencies: def:sc-pic0, def:sc-picard-functor, def:sc-abelian-variety
