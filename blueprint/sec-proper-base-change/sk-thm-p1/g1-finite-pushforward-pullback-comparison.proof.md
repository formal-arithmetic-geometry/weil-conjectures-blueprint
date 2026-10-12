+++
kind = "proof"
of = "g1-finite-pushforward-pullback-comparison"
uses = ["lem-weil-pbc-cohomology-pullback-functorial", "lem-weil-pbc-edge-map-base-change", "lemma-weil-pbc-finite-exchange"]
+++
Finite exchange is invertible. Apply bijective_edgeMap_baseChange for the two vertical comparison bijections and cohomology_edgeMap_baseChange for the commuting square. ([lemma-weil-pbc-finite-exchange], [lem-weil-pbc-edge-map-base-change]).

For bijections l and r satisfying v ∘ l = r ∘ w, bijectivity of w is equivalent to that of v. Surjectivity is equivalent too: lift through l in one direction and cancel the injective r in the other. ([lem-weil-pbc-edge-map-base-change]).

The equivalence counit identifies the converted underlying abelian sheaves with the originals. Naturality of cohomology pullback gives commuting squares whose other maps are the cohomology bijections of these isomorphisms; apply the same elementary argument. ([lem-weil-pbc-cohomology-pullback-functorial]).
