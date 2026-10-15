+++
kind  = "proof"
of    = "prop-sf-pf-reduction"
+++
Use the pullback and tensor comparisons of
[lem-fix-operation-reduction] and the compact-support comparison
of [lem-fix-compact-support-coefficient-change]. Transpose both
routes around the reduction square for the projection transformation
of [def-sf-pf]. Each route pulls back the first factor, applies
the counit, and tensors with the reductions of the remaining factors.
Associativity of derived tensor and compatibility of that counit
with coefficient change identify these composites. Thus the square
commutes as a square of the specified maps. This argument does not
infer equality of morphisms merely from equality on geometric stalks.
Both horizontal maps are isomorphisms by [thm-sf-pf-finite];
in particular the asserted equivalence of invertibility holds.
