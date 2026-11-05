+++
id = "remark-non-noetherian-compactifications"
kind = "remark"
title = "Non-Noetherian compactifications"
name_showing = false
order = 1414
lean = ["AlgebraicGeometry.Compactification.denseRefinement", "AlgebraicGeometry.Compactification.isDense_denseRefinement"]
uses = ["definition-compactification-refinement", "proposition-extension-zero-restriction-closed-subscheme", "lemma-schematic-closure-uniqueness", "theorem-nagata-s-compactification-theorem"]
+++
The same proof works for qcqs $\overline X$ whenever
$\overline X\setminus Z$ is quasi-compact. For a non-Noetherian
compactification this can fail, and then
Proposition [proposition-extension-zero-restriction-closed-subscheme] does not apply to pushforward along
the closed immersion on the pro-étale site. The schematic closure and dense
refinements exist in the generality of Theorem [theorem-nagata-s-compactification-theorem].
