+++
id = "lemma-nagata-fixed-base-separated-stage-exists"
kind = "lemma"
title = "Existence of a separated stage over a fixed base"
order = 393
lean = ["AlgebraicGeometry.Scheme.exists_isSeparated_app_of_isLimit"]
uses = ["lemma-nagata-separated-stage-exists-absolute"]
+++
Let $X=\varprojlim_\alpha X_\alpha$ over a base $S$, where the terms are
qcqs, the transition maps are affine, and every $X_\alpha\to S$ is
quasi-compact — which is automatic when $S$ is quasi-separated. If
$X\to S$ is separated, then there is an index $\alpha_0$ such that
$X_\alpha\to S$ is separated for every $\alpha\geq\alpha_0$.
