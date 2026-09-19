+++
id = "lemma-nagata-relative-proj-current-api"
kind = "lemma"
title = "Relative Proj is realized by the current gluing API"
order = 552
uses = ["lemma-nagata-relative-proj-exists", "lemma-nagata-relative-proj-invertible-tensor-powers", "prop-nagata-relative-proj-functoriality", "thm-nagata-global-blowup-projective"]
+++
**Status.** Bypassed by the formalized route: this lemma is the record of
the replacement itself. The relative-Proj interface above is realized by
`AlgebraicGeometry.Scheme.Cover.RelativeGluingData` together with the
affine Proj chart API, and no relative-Proj declaration of its own was
formalized.

The relative Proj interface used in this blueprint can be implemented from
the current Mathlib scheme APIs. The affine pieces are the standard Proj
charts, the chosen affine cover is the standard-open cover, and the relative
gluing datum is a relative gluing datum over that locally directed affine
cover. Consequently the relative Proj construction, its restriction maps,
the tensor-power comparison of
[lemma-nagata-relative-proj-invertible-tensor-powers], and the finite
projective embedding of
[thm-nagata-global-blowup-projective] require only the local
coefficientwise localization and finite-coordinate lemmas already stated
above; no additional relative-Proj primitive is assumed.

## Proof

The affine chart identification is
`AlgebraicGeometry.Proj.basicOpenIsoSpec`, with the chart morphism
supplied by `AlgebraicGeometry.Proj.away$\iota$`. The
standard opens cover each affine Proj by
`AlgebraicGeometry.Proj.affineOpenCover` and
`AlgebraicGeometry.Proj.iSup_basicOpen_eq_top`. On a locally
directed affine cover of the base, package the chart restrictions and the
coefficientwise localization isomorphisms as
`AlgebraicGeometry.Scheme.Cover.RelativeGluingData`; its
`glued`, `toBase`, and
`isPullback_natTrans__toBase` fields provide the glued scheme,
structure map, and restriction pullbacks. The overlap equations are exactly
the cocycle lemma used by
[lemma-nagata-relative-proj-exists]; the tensor-power and finite
coordinate maps therefore glue by the same restriction uniqueness argument.
