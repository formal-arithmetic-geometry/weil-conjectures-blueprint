+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-epsilon-comparison"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-epsilon-comparison"
order = 1779
uses = ["def-weil-pbc-epsilon-comparison", "lemma-weil-pbc-epsilon-factorization-index-filtered-v1", "lemma-weil-pbc-epsilon-geometric-morphism-construction-v1", "lemma-weil-pbc-etale-proetale-continuous", "lemma-weil-pbc-etale-proetale-left-exact"]
+++
The construction in Definition [def-weil-pbc-epsilon-comparison] is a typed raw datum. Its theorem-valued naturality, comparison, descent, or coherence fields are isolated in this property lemma.

## Proof

The inclusion functor is continuous and left exact. The factorization-index
lemma makes the displayed Kan-extension formula a filtered colimit, and the
construction lemma supplies its sheafification, the adjunction, naturality,
and finite-limit preservation. The formulas for direct image and inverse
image are therefore independent of representatives and restrictions and
define the stated geometric morphism with all comparison fields.
