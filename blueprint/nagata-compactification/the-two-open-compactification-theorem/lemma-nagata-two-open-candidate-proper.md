+++
id = "lemma-nagata-two-open-candidate-proper"
kind = "lemma"
title = "Properness of the two-open candidate"
order = 499
lean = ["AlgebraicGeometry.HasCompactification.of_two_open_cover"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-two-open-compactification-candidate", "lemma-nagata-dense-source-valuative", "lemma-nagata-final-density", "lemma-nagata-two-open-final-modification", "lemma-nagata-two-open-valuative-lifting", "prop-nagata-global-blowup-cover-independent"]
+++
The constructed structural morphism $W\to S$ is proper.

## Proof

The morphism $U_1\cap U_2\to W$ is quasi-compact and dense by
[lemma-nagata-final-density], and its valuation diagrams admit unique
lifts by [lemma-nagata-two-open-valuative-lifting]. The dense-source
valuative criterion makes $W\to S$ universally closed. It is separated
and of finite type by
[lemma-nagata-two-open-final-modification]; hence it is proper.
