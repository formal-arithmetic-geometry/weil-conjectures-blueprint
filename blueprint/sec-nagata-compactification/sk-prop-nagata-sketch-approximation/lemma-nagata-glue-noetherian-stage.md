+++
id = "lemma-nagata-glue-noetherian-stage"
kind = "lemma"
title = "Properties of the finite-type stages"
order = 341
uses = ["def-nagata-noetherian-inverse-system", "lemma-nagata-affine-gluing-identities-eventually", "lemma-nagata-valid-refinements-directed"]
+++
Every $S_\lambda$ is of finite type over $\mathbf Z$, and every transition
morphism $t_{\mu\lambda}$ is affine.

## Proof

The gluing axioms hold at each valid stage, so the schemes are defined.
Each one is covered by finitely many spectra of finitely generated
$\mathbf Z$-algebras, proving finite type. On the chosen charts each
transition is affine by construction; the indexing refinement makes those
charts cover every inverse image, proving global affineness.
