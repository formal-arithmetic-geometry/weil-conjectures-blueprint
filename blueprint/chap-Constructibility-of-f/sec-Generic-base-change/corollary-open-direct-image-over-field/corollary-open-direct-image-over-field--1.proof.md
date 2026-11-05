+++
kind = "proof"
of = "corollary-open-direct-image-over-field--1"
order = 585003
uses = ["theorem-generic-constructibility-base-change-rj"]
+++
Apply the finite-coefficient form of
Theorem [theorem-generic-constructibility-base-change-rj] over
$S=\operatorname{Spec}k$. Its nonempty open is all of $S$, so $Rj_*F$ is
bounded constructible for every constructible étale $A$-sheaf $F$.
This is the sheaf case
`AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion_of_field`.

For a bounded constructible complex $L$, induct on the length of its
cohomological range. The truncation triangle with last nonzero cohomology
$H^b(L)[-b]$ reduces the assertion to a shorter complex and a shifted
constructible sheaf. The functor $Rj_*$ preserves distinguished triangles
and shifts, and bounded constructibility is stable under both. This is
`AlgebraicGeometry.Etale.boundedConstructible_obj_of_forall_singleFunctor`
applied to $Rj_*$.
