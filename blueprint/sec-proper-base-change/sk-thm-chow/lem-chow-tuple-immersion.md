+++
id = "lem-chow-tuple-immersion"
kind = "lemma"
title = "Tuples of morphisms with one immersion"
order = 1055
lean = ["AlgebraicGeometry.isImmersion_left_pi_lift"]
+++
Let $S$ be a scheme, let $(Y_i)_{i\in I}$ be a family of schemes over $S$ whose
fibre product $\prod_{S}Y_i$ (the product in the category of $S$-schemes)
exists, for instance a finite family, and let $f_i\colon T\to Y_i$ be morphisms
of $S$-schemes. If some $f_k$ is an immersion, then

$$
(f_i)_{i\in I}\colon T\longrightarrow \prod_{S}Y_i
$$

is an immersion.

## Proof

Composing $(f_1,\dots,f_m)$ with the projection $\mathrm{pr}_k$ gives back
$f_k$, which is an immersion; hence $(f_1,\dots,f_m)$ is an immersion, because
if a composition $h\circ g$ is an immersion then so is $g$.

(The blueprint originally deduced this from 01KR by factoring
$(f_1,\dots,f_m)$ through $T\times_S Y_2\times_S\dots\times_S Y_m$, which also
requires the $Y_i$ to be separated over $S$. The argument above needs neither.)
