+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--7"
order = 425015
uses = ["proposition-proper-direct-image-constructible-complexes--6", "lemma-integral-models", "lemma-change-coefficients", "lemma-change-coefficients-direct-image"]
+++
For $K\in\Dbc(X,E)$ choose an actual bounded constructible integral model
$K_0$ and an isomorphism $E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}K_0\simeq K$.
This is `AlgebraicGeometry.ProEtale.exists_boundedConstructibleExtendScalars_obj_iso`.
The scalar comparisons [lemma-change-coefficients] identify the base change map
at this scalar extension with the extension of the integral base change map,
as an isomorphism of arrows
`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToRational`.
Apply [proposition-proper-direct-image-constructible-complexes--6], extend scalars,
and transport along the chosen isomorphism. This proves invertibility at every
$K$, hence invertibility of the natural transformation.
