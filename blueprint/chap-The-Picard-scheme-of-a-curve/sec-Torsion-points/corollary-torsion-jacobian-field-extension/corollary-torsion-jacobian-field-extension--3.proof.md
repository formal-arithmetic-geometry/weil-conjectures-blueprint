+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension--3"
order = 1558009
uses = ["proposition-multiplication-n", "theorem-picard-scheme-jacobian-over-separably"]
+++
By [proposition-multiplication-n], $[m]:A\to A$ is finite and
surjective. Over the algebraically closed field $k$, every
$k$-point lifts along this morphism, by
`AlgebraicGeometry.exists_comp_eq_of_isFinite_of_surjective`.
This proves the surjectivity on $A(k)$.

For $\operatorname{Pic}^0(C)$, Lean obtains the Jacobian and the
group isomorphism $\varphi:\operatorname{Pic}^0(C)\simeq J(C)(k)$
from `AlgebraicGeometry.exists_jacobian`, as in
[theorem-picard-scheme-jacobian-over-separably]. Given $\cL$, take
an $m$-th root of $\varphi(\cL)$ and apply $\varphi^{-1}$.
`AlgebraicGeometry.Scheme.surjective_pow_picardZero` carries out
this transport using the divisibility clause of
`AlgebraicGeometry.abelianVariety_estimate_of_isAlgClosed`.
