+++
id = "sk-cor-nagata-sketch-fp"
kind = "section"
title = "Nagata for finite presentation"
order = 375
uses = ["sk-lem-nagata-sketch-closure", "sk-prop-nagata-sketch-approximation", "sk-thm-nagata-sketch-noetherian"]
+++
*Corollary (sketch).*

If $S$ is qcqs, every separated finitely presented $X\to S$
admits a compactification.

## Proof

Descend to a separated finite-presentation model over a Noetherian
$S_\lambda$, compactify it by [sk-thm-nagata-sketch-noetherian],
and base change the resulting factorization to $S$.

Uses: [sk-lem-nagata-sketch-closure], [sk-prop-nagata-sketch-approximation], [sk-thm-nagata-sketch-noetherian]
