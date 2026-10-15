+++
id = "lem-sfb-point-upper-star-braided"
kind = "lemma"
title = "$p^*$ is braided"
order = 1546
uses = ["def-sfb-point-adjunction", "lem-sfb-point-upper-star-tensor", "lem-sfb-point-upper-star-unit"]
lean = ["AlgebraicGeometry.ProEtale.laxBraided_pointUpperStar"]
+++
By [lem-sfb-point-upper-star-unit] and [lem-sfb-point-upper-star-tensor],
$p^*$ is strong monoidal. It is moreover braided: under the tensor comparison
isomorphisms, $p^*$ of the symmetry $F\otimes G\cong G\otimes F$ is the
symmetry $p^*F\otimes p^*G\cong p^*G\otimes p^*F$.
