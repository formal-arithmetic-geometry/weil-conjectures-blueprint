+++
kind = "proof"
of = "lem-pbc-x2-prime-torsion-nonunit-cohomology"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Map the prime annihilation identity to each geometric stalk using sheafFiber_map_smul. For a stalk element take an invertible annihilator n. If r divided n, the unit product would force r to be a unit, a contradiction; primality implies gcd(r,n)=1. The Mathlib lemma nsmul_eq_zero_iff_of_coprime therefore forces the element to be zero. Geometric stalks faithfully detect equality, so id_F=0. Forgetting coefficients maps this identity to id=0, and inverse image preserves zero objects. subsingleton_H_of_isZero proves the two claims. ([lemma-weil-pbc-geometric-stalk-conservative]).
