+++
id = "lem-wf-l2-upper"
kind = "lemma"
title = "The $L^2$-weight is at most the weight"
order = 3098
uses = ["def-weil-punctual-weights", "def-wf-l2-norm", "lem-wf-point-count-linear-growth"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.l2Weight_le_of_hasWeightsAtMost"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, and let $\mathcal F$ be a lisse Weil sheaf of rank $r$
on $X_0$, punctually $\iota$-mixed of weights at most $w$.
Then

$$
\|\mathcal F\|\le w.
$$
