+++
id = "lemma-nagata-final-density"
kind = "lemma"
title = "Density after the final common modification"
order = 497
lean = ["AlgebraicGeometry.HasCompactification.of_two_open_cover"]
uses = ["def-nagata-two-open-compactification-candidate", "lemma-nagata-two-open-density-transport"]
+++
The constructed map $U_1\cap U_2\to W$ is quasi-compact and has dense
image.

## Proof

Apply [lemma-nagata-two-open-density-transport] to the construction of
$W'_1,W'_2,W$. Its hypotheses hold because the selected compactifications
are scheme-theoretically dense and every subsequent center is supported
away from the preserved copy of $U$. The asserted quasi-compactness and
density follow.
