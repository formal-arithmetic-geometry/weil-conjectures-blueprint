+++
id = "thm-pc-picard-representable"
kind = "theorem"
title = "The Picard scheme of a curve is representable"
order = 837
uses = ["cor-pc-sigma-pic-iso", "def-pc-genus", "def-pc-pic-sigma-functor", "def-pc-picard-functor", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-pc-subfunctor", "lem-pc-f-open-subfunctor", "lem-pc-k-sheaf", "lem-pc-rational-hyp", "lem-pc-rational-points-dense", "lem-pc-sigma-k-points", "lem-pc-twist", "lem-pc-vanishing-above-dim", "lem-pc-zariski-coverings-are-fppf", "prop-pc-xk-integral", "thm-pc-criterion", "thm-pc-f-representable", "thm-pc-pic-split"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctor"]
+++
Let $k$ be a separably closed field.
Let $X$ be a scheme over $k$ which is smooth of relative dimension $1$,
proper and geometrically integral over $k$ (for instance a smooth
projective curve over $k$). Then the
Picard functor $\operatorname{Pic}_{X/k}$ is
representable, and the representing scheme
$\underline{\operatorname{Pic}}_{X/k}$ is a group scheme over $k$.
