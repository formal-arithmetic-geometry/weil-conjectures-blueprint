+++
id = "lem-zl-relative-curve-punctual"
kind = "lemma"
title = "Punctual upper bound in a relative affine curve"
order = 2839
lean = ["AlgebraicGeometry.hasWeightsAtMost_higherLowerShriek_of_isAffine_fiber"]
uses = ["def-weil-pbc-qbar-category", "def-weil-punctual-weights", "lem-a1-weight-bound-constant-extension", "lem-tw-punctual-rescaling", "thm-a1-curve-upper", "thm-cbc-qbar"]
+++
Let $Y_0$ be a separated $k_0$-scheme of finite type and let
$h:U_0\to Y_0$ be a morphism of $k_0$-schemes that is smooth of
relative dimension one, separated and quasi-compact, with affine
fibres; thus every nonempty geometric fiber is a smooth affine curve.
Let $\mathcal F$ be a lisse Weil sheaf on $U_0$, punctually
$\iota$-pure of weight $w$, and let $i\ge0$. Then every Frobenius
eigenvalue $\alpha$ on the stalk of $R^ih_!\mathcal F$ at a closed point
$y$ of degree $m$ satisfies $|\iota(\alpha)|\le(q^m)^{(w+i)/2}$, i.e.
the punctual weight of $R^ih_!\mathcal F$ at $y$ is at most $w+i$.

## Proof

Compact-support base change [thm-cbc-qbar], applied to the
cartesian square formed by the fiber $U_y\to U_0$ and the point
$y\to Y_0$, identifies the stalk of $R^ih_!\mathcal F$ at a
geometric point over $y$ with
$H_c^i(U_{\bar y},\mathcal F|_{U_{\bar y}})$. The restricted sheaf has
weight $w$ relative to $q^m$ by the rescaling lemma
[lem-tw-punctual-rescaling]. After a finite extension of
$\kappa(y)$, all geometric components of the affine fiber are
defined and geometrically connected. Apply the curve estimate
[thm-a1-curve-upper] (the upper bound on a smooth geometrically
connected curve, with no condition at infinity) to each component.
The direct sum has the same bound, and
[lem-a1-weight-bound-constant-extension] reflects it back to
$\kappa(y)$. This obtains the displayed bound.
