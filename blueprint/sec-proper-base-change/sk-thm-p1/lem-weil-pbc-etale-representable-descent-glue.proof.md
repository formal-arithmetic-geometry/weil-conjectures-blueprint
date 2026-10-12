+++
kind = "proof"
of = "lem-weil-pbc-etale-representable-descent-glue"
uses = ["def-weil-pbc-etale-site"]
+++
The pullback universal property gives an isomorphism from the represented presheaf of V on the localized site to the restriction of h_P: send a point z to z followed by q; the inverse is the unique pullback lift. The projection equations prove naturality and both inverse identities. (`CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean))).

Compose e with this local isomorphism. The compatibility equation for e and invariance of q under transport show the resulting map is independent of the chosen lift to U. The generic helper amalgamates its maps over the covering sieve of objects mapping to U. Naturality and uniqueness follow from the sheaf axiom. Its restriction is the given local isomorphism, so Sheaf.isIso_of_coversTop makes it an isomorphism. Mathlib supplies subcanonicity directly: Subcanonical.of_le applied to etaleTopology_le_proetaleTopology, followed by subcanonical_of_full_of_faithful for Etale.forget T. This supplies the sheaf h_P, and the surjection U to T makes the sieve covering at every object by base change. (`CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), [def-weil-pbc-etale-site]).
