+++
id = "lemma-nagata-global-blowup-local-maps-agree"
kind = "lemma"
title = "Compatibility of the local structure maps"
order = 305
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupι_blowupMap"]
uses = ["def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "prop-nagata-affine-blowup-restrict"]
+++
On every overlap, the two local structure maps to $X$ agree after applying
the constructed overlap map $\omega_{ij}$.

## Proof

On a basic refinement, both composites are the structural map from the
blow-up of the localized ideal to $D(s)\subseteq X$; the degree-zero part of
the restriction isomorphism makes them equal. Equality on the basic cover
gives equality on the overlap.
