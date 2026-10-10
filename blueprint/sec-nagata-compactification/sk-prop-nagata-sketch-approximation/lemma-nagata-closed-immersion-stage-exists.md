+++
id = "lemma-nagata-closed-immersion-stage-exists"
kind = "lemma"
title = "Existence of a stage where a finite-presentation map is closed"
order = 364
lean = ["AlgebraicGeometry.Scheme.exists_isClosedImmersion_overPullbackMap"]
uses = ["lemma-nagata-filtered-colimit-finite-data"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of schemes with affine
transition maps and limit $S$. Let $g_\lambda\colon Z_\lambda\to Y_\lambda$
be a morphism of finite presentation between $S_\lambda$-schemes, with
$Y_\lambda$ quasi-compact and quasi-separated. If its base change to the
inverse limit $S$ is a closed immersion, then there is
$\mu\geq\lambda$ such that every later base change $g_\nu$ is a closed
immersion.
