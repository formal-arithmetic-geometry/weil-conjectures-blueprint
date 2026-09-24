+++
id = "constructible-sheaves-formalized"
kind = "section"
title = "Constructible sheaves on the étale site (formalized account)"
order = 1455
uses = ["lemma-openclosed-stalk-upperstar", "lemma-openclosed-vanishing-lowerstar", "prop-openclosed-lowerstar-fully-faithful", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
The Lean development's account of constructible étale sheaves: nearly all of
it is formalized. The detailed route of this blueprint does not cite it; it
works with its own statements, [def-weil-pbc-constructible-complexes],
[lem-weil-pbc-constructible-serre] and the finiteness lemmas of
[direct-image-finiteness]. Where a statement here is the same as one there,
its Lean names were moved onto the detailed statement and the copy was
removed: $j_!$ preserves constructibility is now
[lem-fin-extension-by-zero]. The rest stay here because they differ from the
detailed statements: the detailed $i_*$ lemma [lem-fin-closed-immersion] also
asserts $R^qi_*=0$, the detailed weak-Serre lemma includes extensions, which
are not formalized, and the detailed definition of constructibility also
asserts that $D^b_c$ is triangulated, which the formalization proves only
from closure under extensions as a hypothesis.

This section sets up the constructible sheaves on the small étale site of
a scheme: the definitions, their stability under pullback, pushforward along
a closed immersion and extension by zero along an open immersion, the
open–closed dévissage, and the closure under kernels, cokernels and
extensions. Everything is classical; the references are
[SGA4] and the Stacks Project (Tags `03RW`–`03RZ`,
`05BE`, `095K`, `09YJ`). The statements are arranged
in the order in which they are formalised, and the proofs are written at
the level of detail of the Stacks Project.
