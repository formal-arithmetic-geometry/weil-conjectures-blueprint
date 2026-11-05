+++
kind = "proof"
of = "proposition-jacobian-over-ground-field--5"
order = 1562011
uses = ["proposition-jacobian-over-ground-field--4", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Base change along $\operatorname{Spec}(\sigma)$ gives $\gamma:C\to C$,
and invariance of degree under this cartesian square shows that
$\gamma^*$ preserves $\operatorname{Pic}^0(C)$. Naturality of the map
from the degree-zero Picard presheaf to its sheafification identifies
this pullback with the action on $F(\operatorname{Spec}\bar k)$.
This is the equivariance clause of
`AlgebraicGeometry.exists_picardZero_equiv_picardFunctorDegree`.

The representing bijection $r$ is natural as well. Applying its
injectivity to the two sides of the desired equality, and using the
description of $e$ in [proposition-jacobian-over-ground-field--4],
proves the formula. Lean states it for every $k$-algebra automorphism
of $\bar k$.
