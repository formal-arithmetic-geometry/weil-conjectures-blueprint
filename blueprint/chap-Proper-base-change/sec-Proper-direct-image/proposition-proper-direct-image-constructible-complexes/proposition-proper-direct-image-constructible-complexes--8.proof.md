+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--8"
order = 425017
uses = ["proposition-proper-direct-image-constructible-complexes--6", "lemma-integral-models", "lemma-change-coefficients", "lemma-change-coefficients-direct-image"]
+++
Every bounded constructible $\overline{\mathbf Q}_\ell$-complex has an integral
model over some finite $E\subset\overline{\mathbf Q}_\ell$. The composite
coefficient comparisons for $\mathcal O_E\to E\to\overline{\mathbf Q}_\ell$
identify its base change map with the scalar extension of the integral map
[lemma-change-coefficients]. The latter is invertible by
[proposition-proper-direct-image-constructible-complexes--6].

Lean packages this argument in
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_padicAlgCl_of_integral`,
using `AlgebraicGeometry.ProEtale.exists_padicAlgCl_iso_integralModel`.
It applies integral base change to each model directly; a separate application
of the $E$-coefficient base change theorem is unnecessary.
