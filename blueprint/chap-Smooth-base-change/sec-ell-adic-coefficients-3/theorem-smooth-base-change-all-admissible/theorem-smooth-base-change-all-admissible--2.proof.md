+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--2"
order = 700005
uses = ["lemma-change-coefficients", "lemma-reduction-derived-nakayama", "proposition-six-operations-dctf", "proposition-integral-constructibility-criterion", "theorem-smooth-base-change-all-admissible--1"]
+++
The source and target of the integral map are bounded constructible.
The residue-field instance of [lemma-change-coefficients] identifies its
first derived reduction with the finite-coefficient map at $K_1$, as an
arrow. This is
`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_derivedReduction_boundedConstructibleBaseChange`.
The hypothesis therefore makes the reduction invertible. Apply derived
Nakayama [lemma-reduction-derived-nakayama] on $Y'$, in the form
`AlgebraicGeometry.ProEtale.isIso_of_isIso_derivedReduction_map` for
morphisms of bounded constructible $\mathcal O_E$-complexes.

In the smooth square of the theorem, the hypothesis is supplied by
[theorem-smooth-base-change-all-admissible--1]. Indeed, the first reduction
of $K_0$ is of bounded constructible étale origin by
[proposition-integral-constructibility-criterion], in the form
`AlgebraicGeometry.ProEtale.boundedConstructible_derivedReduction_obj`.
The field $\mathbf F_E$ is killed by $\ell$, and $\ell$ is invertible on
$Y$ because $p\ne\ell$.
