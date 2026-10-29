+++
id = "lem-pc-vanishing-above-dim"
kind = "lemma"
title = "Vanishing above the dimension of a curve"
lean = ["AlgebraicGeometry.Scheme.Modules.subsingleton_H_of_two_le"]
order = 816
uses = ["def-pc-curve", "def-pc-dimension", "def-pc-smooth-projective-curve", "def-sc-function-field", "lem-pc-affine-morphism-hi", "lem-sc-morphism-from-function", "lem-sc-p1-hi-vanishing", "lem-sc-smooth-regular", "pqf-lem-leray"]
+++
Let $k$ be a field and let $X$ be a scheme over $k$ which is smooth of
relative dimension $1$ and proper over $k$ (for instance a
curve over $k$ which is smooth and
projective). For every
quasi-coherent $\mathcal{O}_X$-module $\mathcal{F}$ one has

$$
H^i(X,\mathcal{F})=0\qquad\text{for all }i\ge2 .
$$
