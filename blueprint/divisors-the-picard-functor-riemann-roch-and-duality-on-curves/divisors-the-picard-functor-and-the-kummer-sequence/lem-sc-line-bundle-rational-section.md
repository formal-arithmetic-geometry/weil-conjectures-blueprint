+++
id = "lem-sc-line-bundle-rational-section"
kind = "lemma"
title = "Rational sections of line bundles"
order = 3614
lean = ["AlgebraicGeometry.Curve.exists_rational_section", "AlgebraicGeometry.Curve.divisorSheaf_div_iso"]
uses = ["def-sc-divisor"]
+++
Let $C$ be an integral curve over $k$ and $\mathcal L$ an invertible
module. Then $\mathcal L\otimes_{\mathcal O_C}k(C)\cong k(C)$; in
particular $\mathcal L$ has a nonzero rational section
$s\in(\mathcal L\otimes k(C))\setminus\{0\}$, and for such an $s$ the map
$$
 \mathcal O_C(\operatorname{div}s)\longrightarrow\mathcal L,
 \qquad f\longmapsto fs,
$$
is an isomorphism.

## Proof

At the generic point $\eta$, $\mathcal L_\eta$ is a free
$\mathcal O_{C,\eta}=k(C)$-module of rank one, so
$\mathcal L\otimes k(C)\cong k(C)$ and a nonzero element $s$ exists.
Writing $D=\operatorname{div}(s)$ for the divisor of zeros and poles of
$s$, the submodule $\mathcal O_C(D)\subseteq k(C)$ of [def-sc-divisor] is
exactly the set of $f\in k(C)$ with $fs\in\mathcal L$, and $f\mapsto fs$ is
an isomorphism $\mathcal O_C(D)\to\mathcal L$: locally, on an open $U$ with
$\mathcal L|_U\cong\mathcal O_U$, it is multiplication by the element $s$
of $k(C)$, and $\mathcal O_C(D)|_U=s^{-1}\mathcal O_U$ by the definition of
$D=\operatorname{div}(s)$.

Unresolved dependencies: def:sc-curves, def:sc-function-field
