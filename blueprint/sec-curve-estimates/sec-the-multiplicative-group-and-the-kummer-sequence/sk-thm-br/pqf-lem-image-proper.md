+++
id = "pqf-lem-image-proper"
kind = "lemma"
title = "Image of a proper morphism into a separated finite-type target"
lean = ["AlgebraicGeometry.isProper_image\u03b9_comp"]
order = 1445
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-proper-base-change", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-to-separated", "lem-weil-pbc-surjective-nonempty-fibres", "pqf-lem-proper-closed-map"]
+++
Let $p:X\to S$ be
proper, let $Y\to S$ be
separated and of finite
type, and let $f:X\to Y$ be an $S$-morphism. Then the
scheme-theoretic image $Z=f(X)$ of $f$ (the closed subscheme of $Y$
whose quasi-coherent ideal is the kernel of
$\mathcal O_Y\to f_*\mathcal O_X$; it is closed in $Y$ because $p$ is
a closed map, by [lem-weil-pbc-proper-closed-image]) is proper over $S$, the induced morphism $X\to Z$ is proper and
surjective, and the composite $X\to Z\to S$ is $p$.
