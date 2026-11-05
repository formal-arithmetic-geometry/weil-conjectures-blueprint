+++
id = "proposition-pullback-multiplication-n--1"
kind = "proposition"
title = "Pullback of invertible sheaves by {$[n]$} (1)"
name_showing = false
order = 1500001
aliases = ["bp-r468-1"]
lean = []
uses = ["definition-abelian-variety"]
+++
This formula for an arbitrary invertible sheaf is bypassed by the Lean
proof, which proves the symmetric case
[proposition-pullback-multiplication-n--2] directly from the theorem of
the cube.

Let $A$ be an abelian variety over $k$ and let $\mathcal L$ be an
invertible sheaf on $A$. For every integer $n\geq0$,

$$
[n]^*\mathcal L\simeq
\mathcal L^{\otimes n(n+1)/2}\otimes
([-1]^*\mathcal L)^{\otimes n(n-1)/2}.
$$
