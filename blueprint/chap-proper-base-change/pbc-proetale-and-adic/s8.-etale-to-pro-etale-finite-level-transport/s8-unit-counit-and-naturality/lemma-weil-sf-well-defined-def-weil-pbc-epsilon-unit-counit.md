+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-epsilon-unit-counit"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-epsilon-unit-counit"
order = 1793
uses = ["def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-adjunction-equations-v1", "lemma-weil-pbc-epsilon-counit-representative-descent-v1", "lemma-weil-pbc-epsilon-geometric-morphism-construction-v1"]
+++
The construction in Definition [def-weil-pbc-epsilon-unit-counit] is a typed raw datum. Its theorem-valued naturality, comparison, descent, or coherence fields are isolated in this property lemma.

## Proof

The geometric-morphism construction supplies the adjunction. Representative
descent makes the displayed counit formula a sheaf morphism, while the unit
formula is the identity-factorization component of the same adjunction. The
final lemma proves naturality, restriction compatibility, and both triangle
identities, so every theorem-valued field of the raw unit–counit datum is
well-defined.
