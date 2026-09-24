+++
id = "def-nagata-global-blowup-cover-comparison"
kind = "definition"
title = "Comparison between two affine-cover constructions"
order = 308
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowup"]
uses = ["def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "lemma-nagata-global-blowup-overlap-cocycle"]
+++
Given two affine covers of $X$, choose their intersection refinement. On
every refined affine chart use the two affine-restriction isomorphisms to
define a comparison, and glue these comparisons after transporting them to
the original charts. The overlap equalities are those of
[lemma-nagata-global-blowup-overlap-cocycle].
The refinement maps are independent of the selected basic chart by the
overlap cocycle, so the glued comparison is well-defined as a morphism of
the two gluing data.
