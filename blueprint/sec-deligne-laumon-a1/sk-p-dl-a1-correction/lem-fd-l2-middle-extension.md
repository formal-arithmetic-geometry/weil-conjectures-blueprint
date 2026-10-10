+++
id = "lem-fd-l2-middle-extension"
kind = "lemma"
title = "The middle extension does not change the $L^2$-weight"
order = 2769
uses = ["def-weil-punctual-weights", "def-wf-l2-norm", "def-wf-middle-extension", "lem-wf-boundary-semicontinuity", "lem-wf-l2-purity-rigidity"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.l2Weight_directImage"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion
with finite complement $S_0$, and let $\mathcal M$ be a nonzero lisse
Weil sheaf of rank $r$ on $U_0$, punctually
$\iota$-pure of weight $w$. Write $\|f_{\mathcal M}\|_m^2$ for
the sum of squares of the trace function of $\mathcal M$ over
$U_0(k_m)$ as in [def-wf-l2-norm], and
$\|f_{j_*\mathcal M}\|_m^2$ for the same sum for the
middle extension over
$\mathbf A^1_{k_0}(k_m)$. Then the two parameters that these sums
define through the ratio of [def-wf-l2-norm] coincide, and equal
$w$:

$$
\|j_*\mathcal M\|=\|\mathcal M\|=w .
$$
