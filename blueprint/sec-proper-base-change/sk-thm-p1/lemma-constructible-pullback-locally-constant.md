+++
id = "lemma-constructible-pullback-locally-constant"
kind = "lemma"
title = "Pullback of locally constant sheaves"
order = 1221
lean = ["AlgebraicGeometry.Scheme.Etale.overEquiv", "AlgebraicGeometry.Scheme.IsLocallyConstantSheaf.upperStar", "AlgebraicGeometry.Scheme.isConstant_over_iff_upperStar"]
uses = ["def-constructible-constant", "def-constructible-locally-constant"]
+++
For an étale $X$-scheme $U$, the site $\et X$ localised at $U$ is
equivalent to $\et U$, and the restriction of $\mathcal F\in\shv{\et X}$
to the localised site is constant if and only if the pullback of
$\mathcal F$ along $U\to X$ is a constant sheaf on $\et U$.

Let $g\colon Y\to X$ be a morphism and let $\mathcal F\in\shv{\et X}$ be
locally constant. Then $g^*\mathcal F$ is locally constant.
