+++
id = "lem-wf-l2-purity-rigidity"
kind = "lemma"
title = "The $L^2$-weight of a punctually pure lisse sheaf equals its weight"
order = 2766
uses = ["def-weil-punctual-weights", "def-wf-constant-weil-twist", "def-wf-iota-real", "def-wf-l2-norm", "def-wf-normalized-real-envelope", "lem-tw-dual-negation", "lem-wf-constant-twist-weight", "lem-wf-envelope-real", "lem-wf-l2-upper", "thm-wf-l2-dictionary"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.l2Weight_eq_of_isPunctuallyPureOfWeight"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, and let $\mathcal G$ be a nonzero lisse Weil sheaf
on $X_0$, punctually
$\iota$-pure of weight $w$. Then, in the $L^2$-weight parameter
$\|\cdot\|$ of [def-wf-l2-norm],

$$
\|\mathcal G\|=w .
$$

Thus the $L^2$-rigidity [thm-wf-l2-dictionary] does not in fact
need its hypothesis of $\iota$-reality: punctual purity of the weight
alone suffices, and in particular the rigidity applies to the
$\iota$-realizable sheaves of
[def-wf-iota-real].
