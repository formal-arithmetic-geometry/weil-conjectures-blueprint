+++
id = "cor-a1-middle-extension-affine-endpoints"
kind = "theorem"
title = "Middle-extension cohomology of an affine curve"
order = 3077
tags = ["latex:corollary"]
uses = ["def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "lem-a1-middle-extension-endpoints", "prop-a1-middle-extension-curve-upper"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open immersion of smooth
geometrically connected curves with $C_0$ affine (for instance
$C_0=\mathbf A^1_{k_0}$), and let $\mathcal F$ be a lisse Weil sheaf
on $U_0$ which is punctually $\iota$-pure of weight $w$. For the middle
extension $j_*\mathcal F$ of [def-wf-middle-extension] and every
integer $r$,

$$
H_c^r(C,j_*\mathcal F)\quad\text{has weights at most }w+r.
$$

More precisely, $H_c^0(C,j_*\mathcal F)=0$ and
$H_c^2(C,j_*\mathcal F)$ is $\iota$-pure of weight $w+2$; only the
degree-one bound is not an endpoint computation.

## Proof

The upper bound in every degree is
[prop-a1-middle-extension-curve-upper]. The two refinements are the
endpoint lemma [lem-a1-middle-extension-endpoints], whose hypotheses
($C_0$ a smooth geometrically connected affine curve, $j$ a dense open
immersion, $\mathcal F$ lisse and punctually $\iota$-pure of weight
$w$) are those of the statement: it gives $H_c^0(C,j_*\mathcal F)=0$
and shows that $H_c^2(C,j_*\mathcal F)$, the Tate twist of the
geometric coinvariants, is $\iota$-pure of weight $w+2$.
