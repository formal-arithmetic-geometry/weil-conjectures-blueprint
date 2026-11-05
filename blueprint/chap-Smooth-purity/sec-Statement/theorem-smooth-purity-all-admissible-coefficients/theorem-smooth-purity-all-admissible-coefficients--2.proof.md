+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients--2"
order = 730005
uses = ["theorem-smooth-purity-all-admissible-coefficients--1", "definition-derived-adic-completeness", "lemma-sp-reduction", "lemma-reduction-derived-nakayama", "theorem-bounded-below-cohomology-comparison"]
+++
Reduce the two objects modulo $\ell^n$ and read the reductions on the small étale site. The comparisons for reduction of $f^!$ and of the Tate twist identify them with the two objects in [theorem-smooth-purity-all-admissible-coefficients--1]. Hence they are isomorphic at every positive finite level.

The Tate twists have finite endomorphism sets: $X$ is noetherian, and thus has finitely many connected components. Full faithfulness of the étale reading transfers this finiteness to the morphisms between the reductions. König's lemma and derived completeness then give a morphism whose reductions are all isomorphisms (`AlgebraicGeometry.ProEtale.exists_forall_isIso_derivedReduction_map`). The first reduction detects that this morphism is an isomorphism, by derived Nakayama [lemma-reduction-derived-nakayama]. This argument chooses a compatible family of isomorphisms; it does not lift a prescribed family of finite orientations.
