+++
id = "lemma-nagata-global-blowup-local-maps-agree"
kind = "lemma"
title = "Compatibility of the local structure maps"
order = 305
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupι_blowupMap"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-diagonal-base-change", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-restrict", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
On every overlap, the two local structure maps to $X$ agree after applying
the constructed overlap map $\omega_{ij}$.

## Proof

On a basic refinement, both composites are the structural map from the
blow-up of the localized ideal to $D(s)\subseteq X$; the degree-zero part of
the restriction isomorphism makes them equal. Equality on the basic cover
gives equality on the overlap.
