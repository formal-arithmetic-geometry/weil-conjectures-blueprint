+++
id = "prose-07-09"
kind = "hidden"
title = "Complements finite over the base and coordinate projections"
order = 340
+++
The two lemmas of this subsection supply the geometry of the induction
in Theorem [sk-thm-geo-generic-open]. Consider $Rj_*F$ for an open
immersion $j:X\hookrightarrow Y$ over $S$, with $Y$ projective over $S$.
Composing with a coordinate function $t:Y_\alpha\to\mathbf A^1_S$, we may
view $X\cap Y_\alpha$ over the new base $\mathbf A^1_S$, where its generic
fibre has one dimension less, and the induction hypothesis gives
constructibility and base change over a dense open of $\mathbf A^1_S$. These
opens do not cover $Y$. For $Y=\mathbf P^1_S$ with the two standard charts,
a point is missed only if each of the coordinates $x$ and $1/x$ that is
defined there takes an excluded value, so after shrinking $S$ what is left is a closed subset
finite over $S$, and
Lemma [sk-lem-geo-coordinates] shows that this is the general picture
after shrinking $S$.

On the leftover finite part we cannot argue by dimension again, but we do
not have to. On a subset finite over $S$, constructibility of a sheaf
can be read off from its direct image to $S$, since a finite direct
image is exact and conservative. Hence if a complex is already
constructible away from such a subset, a proper direct image to $S$
detects whether it is constructible everywhere
(Lemma [sk-lem-geo-finite-boundary]). In the smooth case this direct image
is $R(bj)_*F$, which Lemma [sk-lem-geo-smooth-generic] controls. This is
the reason the induction passes through the smooth case first.
