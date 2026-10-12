+++
kind = "proof"
of = "lem-pbc-a3-prime-annihilated-primary-cases"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Apply each additive geometric stalk functor to r id_F = 0. Every stalk element is killed by r, so exponent one proves r-primary torsion.

If p differs from r, r and p^n are coprime. nsmul_eq_zero_iff_of_coprime shows that each p-primary stalk element is zero.

Use sheafHom_ext_of_sheafFiber_map_algClosurePoint from the geometric-stalk conservativity module to identify the identity of F with zero. IsZero.iff_id_eq_zero concludes. ([lemma-weil-pbc-geometric-stalk-conservative]).
