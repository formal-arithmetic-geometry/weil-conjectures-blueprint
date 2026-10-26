+++
id = "lem-pd-geometric-curve"
kind = "lemma"
title = "The geometric curve is a smooth projective geometrically integral curve"
lean = ["AlgebraicGeometry.isSepClosed_and_pullback_sepClosure"]
order = 851
uses = ["def-pc-base-change", "def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-pd-separable-closure", "lem-pc-dim-base-change"]
+++
Let $k$ be a field and let $C$ be a
smooth projective curve over $k$
which is geometrically integral,
of genus $g$ ([def-pc-genus]). Then for a
separable closure $k_s$ of $k$ the
base change $C_{k_s}$ is a smooth projective
curve over the separably closed field $k_s$ which is geometrically integral,
of genus $g$.
