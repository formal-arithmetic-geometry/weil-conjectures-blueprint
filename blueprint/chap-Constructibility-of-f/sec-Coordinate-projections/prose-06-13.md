+++
id = "prose-06-13"
kind = "hidden"
title = "Coordinate projections (1)"
order = 562
+++
To control $Rj_*F$ for an open immersion $j:X\hookrightarrow Y$ over $S$,
with $Y$ projective over $S$, we cover most of $Y$ by opens where the
induction hypothesis applies and treat the rest separately. A coordinate
function $t:Y_\alpha\to\mathbf A^1_S$ lets us view $X\cap Y_\alpha$ over
the new base $\mathbf A^1_S$. Over this base its generic fibre has one
dimension less. Hence the induction hypothesis in
Theorem [theorem-generic-constructibility-base-change-rj] gives
constructibility and base change over a dense open of $\mathbf A^1_S$.
The preimages of these opens do not cover $Y$. Take for instance
$Y=\mathbf P^1_S$ with the two standard charts. A point is missed only if
each of the coordinates $x$ and $1/x$ defined there takes an excluded
value. After shrinking $S$, the leftover set is therefore a closed subset
finite over $S$. Lemma [lemma-coordinate-projections] shows that the
same holds in general.

On the leftover finite part we cannot argue by dimension again. We do not
have to, since a finite direct image is exact and conservative. This means
that on a subset finite over $S$, the constructibility of a sheaf can be
read off from its direct image to $S$.
Lemma [lemma-detection-proper-direct-image] turns this into a
criterion. If a complex is already constructible away from such a subset,
a proper direct image to $S$ detects whether it is constructible
everywhere. In the smooth case this direct image is $R(bj)_*F$, which
Lemma [lemma-smooth-morphisms-locally-constant-sheaves] controls. For
this reason the induction passes through the smooth case first.
