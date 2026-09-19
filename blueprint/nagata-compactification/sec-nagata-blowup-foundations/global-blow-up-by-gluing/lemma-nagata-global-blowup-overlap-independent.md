+++
id = "lemma-nagata-global-blowup-overlap-independent"
kind = "lemma"
title = "Independence of the basic refinement"
order = 225
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-global-blowup-overlap-basic"]
+++
On the intersection of two chosen basic refinements, the two overlap
constructed maps $\omega_{ij,s}$ agree.

## Proof

Refine once more to a basic open contained in both. There the two maps are
the same composite of restriction isomorphisms, by
[lemma-nagata-affine-blowup-restrict-cocycle]. Since these refinements
cover the source overlap, equality of morphisms follows by locality on the
source.
