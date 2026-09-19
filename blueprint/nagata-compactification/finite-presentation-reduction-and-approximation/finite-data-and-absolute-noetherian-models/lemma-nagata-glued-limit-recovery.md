+++
id = "lemma-nagata-glued-limit-recovery"
kind = "lemma"
title = "Recovery of the glued limit"
order = 502
uses = ["def-nagata-glued-limit-comparison", "lemma-nagata-glue-noetherian-stage", "lemma-nagata-ring-finite-type-subalgebras"]
+++
**Status.** Bypassed by the formalized route: the finite-presentation and
Noetherian descent is done in one step by
`AlgebraicGeometry.Scheme.exists_isPullback_of_finitePresentation_of_isSeparated`
and `AlgebraicGeometry.Scheme.nonempty_noetherianApproximation`, so
this stage-by-stage bookkeeping is never carried out.

The constructed comparison $\kappa_S$ is an isomorphism.

## Proof

On every selected affine chart, the inverse limit has coordinate ring the
filtered colimit of its finite-stage coordinate rings, hence the original
chart ring. These chartwise isomorphisms agree on the chosen basic
overlaps because all transition maps came from the original gluing maps.
They glue to an inverse for $\kappa_S$.
