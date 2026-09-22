+++
id = "lem-weil-pbc-exchange-identity-pasting"
kind = "lemma"
title = "Identity and pasting equations for exchange"
order = 2043
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_id", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-cartesian-square-detailed"]
+++
The transformation $\Ex_{\square}$ of the derived exchange morphism
[def-weil-pbc-derived-exchange-detailed] is the identity for an identity
square. For horizontally or vertically pasted cartesian squares
[def-weil-pbc-cartesian-square-detailed], the exchange morphism of the outer
rectangle equals the composite of the exchange morphisms of the two inner
squares after inserting the canonical associativity isomorphisms for inverse
and derived direct images.

## Proof

Both equations are the mate versions of the identity and pasting laws for
$\theta_\square$ recorded in [def-weil-pbc-cartesian-square-detailed],
transported through the adjunction calculus for $u^{-1}\dashv Ru_*$. By
[lem-weil-pbc-derived-exchange-replacement] every displayed map is the
specified derived exchange morphism of
[def-weil-pbc-derived-exchange-detailed].
