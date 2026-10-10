+++
id = "lemma-nagata-immersion-into-proper"
kind = "lemma"
title = "The immersion construction is a compactification"
order = 80
lean = ["AlgebraicGeometry.HasCompactification.of_isImmersion"]
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-immersion-compactification", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-open-immersion-qc-over-separated-target"]
+++
Let $g\colon X\to Y$ be an immersion over $S$ with $Y\to S$ proper, and
assume the composite $X\to S$ is quasi-compact. Then $X\to S$ is
compactifiable: $g$ is quasi-compact, and the constructed factorization
$\mathsf C(g)$ is a compactification of $X\to S$.
