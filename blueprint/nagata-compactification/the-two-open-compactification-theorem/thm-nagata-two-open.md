+++
id = "thm-nagata-two-open"
kind = "theorem"
title = "[stacks-project]"
order = 566
lean = ["AlgebraicGeometry.HasCompactification.of_two_open_cover"]
uses = ["def-nagata-compactification", "def-nagata-global-blowup-cover-comparison", "def-nagata-two-open-compactification-candidate", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-two-open-candidate-proper", "lemma-nagata-two-open-final-modification", "prop-nagata-global-blowup-cover-independent"]
+++
The constructed factorization $\mathsf C_{12}(U/S)$ is a compactification
of $U\to S$. Consequently $U\to S$ is compactifiable.

## Proof

By [lemma-nagata-two-open-final-modification], the first map
$j_W\colon U\to W$ is an open immersion and $W\to S$ is separated and of
finite type. It is proper by
[lemma-nagata-two-open-candidate-proper]. The open immersion $j_W$ is
quasi-compact by
[lemma-nagata-open-immersion-qc-over-separated-target], applied to the
triangle $U\to W\to S$. The defining gluing maps give the factorization
equality, so all fields of [def-nagata-compactification] are present.
