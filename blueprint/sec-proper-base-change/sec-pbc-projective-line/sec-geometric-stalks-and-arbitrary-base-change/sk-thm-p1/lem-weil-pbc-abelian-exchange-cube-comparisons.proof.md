+++
kind = "proof"
of = "lem-weil-pbc-abelian-exchange-cube-comparisons"
uses = ["def-weil-pbc-derived-inverse-image", "lem-weil-pbc-inverse-image-stalk-germ", "lemma-weil-pbc-derived-exchange-coherence"]
+++
Apply the proved horizontal pasting law for the derived exchange to the original square followed by the square over jB, and to the square over jA followed by the local square over g0. The outer mates agree because their horizontal maps agree by the two cube equations. Cancel the composition isomorphisms. Insert the inverse-image/single-complex comparison by naturality of the local mate. ([lemma-weil-pbc-derived-exchange-coherence]).

Apply homology and the fibre functor. Naturality of the exact inverse-image/homology comparison and of the inverse-image stalk comparison transports the resulting equality to the two stalk comparison maps $r_1,r_2$ of the statement. This is a formal calculation, with no invertibility assumption on either mate. ([def-weil-pbc-derived-inverse-image], [lem-weil-pbc-inverse-image-stalk-germ]).
