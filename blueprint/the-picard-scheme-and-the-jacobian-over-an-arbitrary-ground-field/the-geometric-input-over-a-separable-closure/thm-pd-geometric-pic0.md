+++
id = "thm-pd-geometric-pic0"
kind = "theorem"
title = "The degree-zero Picard functor over a separable closure"
order = 4711
lean = ["AlgebraicGeometry.Curve.picardFunctorZero_isRepresentable_of_sepClosure"]
uses = ["def-pd-degree-morphism", "def-pd-separable-closure", "lem-pd-geometric-curve"]
+++
Let $k$ be a field, let $C$ be a smooth projective curve over $k$ which is
geometrically integral, of genus $g$, and let $k_s$ be a separable closure
[def-pd-separable-closure] of $k$. Then the degree-zero part
[def-pd-degree-morphism] $\operatorname{Pic}^0_{C_{k_s}/k_s}$ is
representable, and the representing object $J_s$ is an abelian variety over
$k_s$ of dimension $g$; moreover
$J_s(k_s)=\operatorname{Pic}^0(C_{k_s})$ under the canonical identification.

## Proof

By [lem-pd-geometric-curve] the curve $C_{k_s}$ is a smooth projective curve
over the separably closed field $k_s$ which is geometrically integral of
genus $g$. The Jacobian existence theorem therefore produces an abelian
variety $J_s$ over $k_s$ of dimension $g$, whose defining property is the
isomorphism $\operatorname{Pic}^0_{C_{k_s}/k_s}\cong h_{J_s}$, and it
identifies $J_s(k_s)$ with the group $\operatorname{Pic}^0(C_{k_s})$. That
theorem formulates its functor as the degree-zero part of the Picard functor,
which is the subfunctor introduced in [def-pd-degree-morphism]; hence $J_s$
represents $\operatorname{Pic}^0_{C_{k_s}/k_s}$ in the sense used here. The
theorem of the base supplies the same conclusion independently, together with
smoothness, properness and the dimension, which is what makes $J_s$ an
abelian variety.

Unresolved dependencies: def:pc-smooth-projective-curve, def:pc-geometrically-irreducible, def:pc-genus, def:sc-abelian-variety, def:sc-pic0, thm:sc-jacobian-representability, thm:sc-theorem-of-the-base, def:sc-jacobian
