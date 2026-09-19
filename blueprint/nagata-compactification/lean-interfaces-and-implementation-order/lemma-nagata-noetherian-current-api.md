+++
id = "lemma-nagata-noetherian-current-api"
kind = "lemma"
title = "Noetherian approximation is covered by the current limit APIs"
order = 553
uses = ["lemma-nagata-closed-immersion-stage-exists", "lemma-nagata-finite-presentation-descends", "lemma-nagata-relative-gluing-datum-descends", "prop-nagata-noetherian-inverse-system"]
+++
**Status.** Bypassed by the formalized route: this lemma is the record of
the replacement itself. The stagewise approximation above is subsumed by
`AlgebraicGeometry.Scheme.nonempty_noetherianApproximation` and
`AlgebraicGeometry.Scheme.exists_isPullback_of_finitePresentation_of_isSeparated`.

The inverse-system and finite-stage constructions in this blueprint use only
the verified Mathlib APIs for cofiltered limits with affine transition maps
and for relative gluing. In particular,
[prop-nagata-noetherian-inverse-system] supplies the selected system,
[lemma-nagata-relative-gluing-datum-descends] and
[lemma-nagata-finite-presentation-descends] supply the finite-stage model,
and [lemma-nagata-closed-immersion-stage-exists] supplies the common
closed stage. The remaining stage arguments are finite affine coefficient
calculations, so they are local wrapper lemmas rather than missing
scheme-limit infrastructure.

## Proof

For the inverse system in
[prop-nagata-noetherian-inverse-system], use
`AlgebraicGeometry.Scheme.OpenCover.exists_of_isCofiltered_of_finite`,
`AlgebraicGeometry.isLimitOpensCone`, and
`AlgebraicGeometry.isAffineHom__app`; these identify finite
affine covers of the limit and preserve affine transition maps. The
finite-presentation descent map is the instance
`AlgebraicGeometry.Scheme.preservesColimit_yoneda` together with
`AlgebraicGeometry.Scheme.exists__app_comp_eq_of_locallyOfFinitePresentation`.
The relative chart datum from
[lemma-nagata-relative-gluing-datum-descends] is packaged by
`AlgebraicGeometry.Scheme.Cover.RelativeGluingData`, whose
`glued`, `toBase`, and
`isPullback_natTrans__toBase` fields supply the global
scheme and its base-change charts. The proof of
[lemma-nagata-closed-immersion-stage-exists] then contributes only the
finite list of generators and relations needed to choose one common stage.
