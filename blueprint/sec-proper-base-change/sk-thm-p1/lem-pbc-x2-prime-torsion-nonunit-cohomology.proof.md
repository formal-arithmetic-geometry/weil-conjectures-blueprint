+++
kind = "proof"
of = "lem-pbc-x2-prime-torsion-nonunit-cohomology"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Map the identity $r\,\mathrm{id}_F=0$ to each geometric stalk, where it says that $r$ kills the stalk (stalk functors are additive). For a stalk element take an invertible annihilator n. If r divided n, the unit product would force r to be a unit, a contradiction; primality implies gcd(r,n)=1. An element killed by two coprime integers is zero, so the element vanishes. Geometric stalks faithfully detect equality, so id_F=0. Forgetting coefficients maps this identity to id=0, and inverse image preserves zero objects. The cohomology of a zero sheaf is zero in every degree, which proves the two claims. ([lemma-weil-pbc-geometric-stalk-conservative]).
