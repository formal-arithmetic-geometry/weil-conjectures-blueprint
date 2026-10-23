+++
id = "lem-zl-relative-curve-punctual"
kind = "lemma"
title = "Punctual upper bound in a relative affine curve"
order = 4064
lean = ["AlgebraicGeometry.hasWeightsAtMost_higherLowerShriek_of_isAffine_fiber"]
uses = ["def-weil-punctual-weights", "lem-a1-weight-bound-constant-extension", "lem-tw-punctual-rescaling", "sk-def-sf-weil-complexes", "sk-lem-coefficient-heart", "sk-thm-sfb-shriek-base-change", "thm-a1-curve-upper", "sk-cor-wft-curve-upper", "sk-prop-sf-cbc", "sk-thm-sf-comp-composition"]
+++
Let $Y_0$ be a separated $k_0$-scheme of finite type and let
$h:U_0\to Y_0$ be a morphism of $k_0$-schemes that is smooth of
relative dimension one, separated and quasi-compact, with affine
fibres; thus every nonempty geometric fiber is a smooth affine curve.
Let $\mathcal F$ be a lisse $\Qlb$-Weil sheaf on $U_0$ (lisse in
$\Cons(U,\Qlb)$ [sk-lem-coefficient-heart], with a Weil structure
[sk-def-sf-weil-complexes]), punctually
$\iota$-pure of weight $w$, and let $i\ge0$. Then every Frobenius
eigenvalue $\alpha$ on the stalk of $R^ih_!\mathcal F$ at a closed point
$y$ of degree $m$ satisfies $|\iota(\alpha)|\le(q^m)^{(w+i)/2}$, i.e.
the punctual weight of $R^ih_!\mathcal F$ at $y$ is at most $w+i$.
