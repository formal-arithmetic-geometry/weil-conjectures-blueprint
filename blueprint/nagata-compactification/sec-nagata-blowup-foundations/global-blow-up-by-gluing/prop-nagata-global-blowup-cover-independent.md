+++
id = "prop-nagata-global-blowup-cover-independent"
kind = "theorem"
title = "Independence of the affine cover"
order = 310
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowup"]
tags = ["latex:proposition"]
uses = ["def-nagata-global-blowup-cover-comparison", "lemma-nagata-global-blowup-overlap-cocycle", "prop-nagata-global-blowup-affine-restrict"]
+++
The constructed comparison is the unique isomorphism over $X$ restricting
to the identity comparison on every common affine refinement.

## Proof

By [prop-nagata-global-blowup-affine-restrict], the comparison is an
isomorphism on every member of the common refinement. The overlap cocycle
makes these local isomorphisms compatible, so they glue; the glued inverse
is obtained from the local inverses. Uniqueness follows because morphisms
of schemes are determined on an affine open cover.
