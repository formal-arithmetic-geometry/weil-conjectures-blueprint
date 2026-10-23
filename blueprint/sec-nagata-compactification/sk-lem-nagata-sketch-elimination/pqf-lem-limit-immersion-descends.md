+++
id = "pqf-lem-limit-immersion-descends"
kind = "lemma"
title = "Closed immersions spread out from a filtered limit"
lean = ["AlgebraicGeometry.Scheme.exists_isClosedImmersion_comp_\u03c0"]
order = 305
uses = ["def-weil-pbc-scheme-conventions", "pqf-lem-affine-local-target"]
+++
Let $S$ be a scheme, let $X=\varprojlim_{i\in I}X_i$ be a filtered
limit of schemes with affine transition morphisms, and let $0\in I$ be an
index such that $X_0$ is quasi-compact and comes with a morphism
$X_0\to S$. Let $Y\to X$ be a closed immersion such that the composite
$Y\to X\to X_0\to S$ is locally of finite type. Then there is an index
$j\ge0$ such that the composite $Y\to X\to X_i$ is a closed immersion for
every $i\ge j$.
