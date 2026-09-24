+++
id = "lemma-nagata-fixed-base-separated-eventually"
kind = "lemma"
title = "Eventual separatedness over a fixed base, [stacks-project]"
order = 557
lean = ["AlgebraicGeometry.Scheme.exists_isSeparated_app_of_isLimit"]
uses = ["def-nagata-fixed-base-separated-stage", "lemma-nagata-fixed-base-separated-stage-exists"]
+++
For every $\alpha\geq\alpha_{\mathrm{sep}}$, the morphism
$X_\alpha\to S$ is separated.

## Proof

The witness supplied by
[lemma-nagata-fixed-base-separated-stage-exists] contains the eventual
separatedness proof. Project that field along the index selected in
[def-nagata-fixed-base-separated-stage].
