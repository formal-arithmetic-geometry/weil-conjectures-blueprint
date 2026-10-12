+++
kind = "proof"
of = "lem-v2-underlying-abelian-assertions"
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-geometric-stalks", "def-weil-pbc-primary-torsion", "lem-weil-pbc-cohomology-pullback-functorial"]
+++
Commutation of the stalk functor with forgetting modules follows from preservation of filtered colimits (Mathlib Point.sheafFiberCompIso). Compose the two commutation isomorphisms and the given abelian isomorphism to obtain a stalk additive equivalence. It preserves nsmul, hence primary and invertible-order torsion. ([def-weil-pbc-geometric-stalks], [def-weil-pbc-primary-torsion]).

Apply the functor Sheaf.H to the isomorphism, obtaining inverse equivalences in every degree. Transfer subsingleton and finite groups for C1-C5. Constructibility of both sheaves is assumed. ([def-weil-pbc-eight-curve-assertions]).

Naturality of Etale.cohomologyMap with coefficient morphisms conjugates each comparison by the equivalences on the source and pullback. Prove injectivity and surjectivity by composing those equivalences, giving C6-C8. ([lem-weil-pbc-cohomology-pullback-functorial], [def-weil-pbc-eight-curve-assertions]).
