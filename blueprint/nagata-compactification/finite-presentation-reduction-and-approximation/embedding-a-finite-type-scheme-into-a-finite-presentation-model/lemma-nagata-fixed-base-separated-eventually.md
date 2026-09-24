+++
id = "lemma-nagata-fixed-base-separated-eventually"
kind = "lemma"
title = "Eventual separatedness over a fixed base, [stacks-project]"
order = 204
lean = ["AlgebraicGeometry.Scheme.exists_isSeparated_app_of_isLimit"]
uses = ["def-nagata-fixed-base-separated-stage", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-fixed-base-separated-stage-exists", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-separated-stage-exists-absolute"]
+++
For every $\alpha\geq\alpha_{\mathrm{sep}}$, the morphism
$X_\alpha\to S$ is separated.

## Proof

The witness supplied by
[lemma-nagata-fixed-base-separated-stage-exists] contains the eventual
separatedness proof. Project that field along the index selected in
[def-nagata-fixed-base-separated-stage].
