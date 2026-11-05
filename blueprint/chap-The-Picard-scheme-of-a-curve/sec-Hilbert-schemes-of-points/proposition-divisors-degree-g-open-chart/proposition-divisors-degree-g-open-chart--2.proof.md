+++
kind = "proof"
of = "proposition-divisors-degree-g-open-chart--2"
order = 1537004
uses = ["theorem-hilbert-schemes-points-smooth-curve", "proposition-divisors-degree-g-open-chart--1"]
+++
By Theorem [theorem-hilbert-schemes-points-smooth-curve], choose a scheme
$H$ representing $\operatorname{Hilb}^{g}_{C/k}$, smooth of relative
dimension $g$ over $k$. Apply
[proposition-divisors-degree-g-open-chart--1] to obtain the open immersion
$j:W\to H$ and the representation of $F$ by $W$.
This is the proof of
`AlgebraicGeometry.exists_representableBy_picardFunctorInvertibleDirectImage`,
which uses the wrapper
`AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage`
to discard the compatibility clause.

An open immersion is smooth of relative dimension $0$. Composing $j$
with $H\to\operatorname{Spec}k$ therefore makes $W$ smooth of relative
dimension $0+g=g$. Lean uses this composition in
`AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor`
when it covers the Picard scheme by translates of $W$.
