+++
id = "lemma-constructible-immersion-independence"
kind = "lemma"
title = "Independence of the scheme structure"
order = 1232
lean = ["AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.upperStar_of_range_subset", "AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_iff_of_range_eq"]
uses = ["def-constructible-finite-locally-constant", "lemma-constructible-pullback-stratification"]
+++
Let $\mathcal F\in\shv{\et X}$, let $b\colon Z'\to X$ be an immersion and
let $a\colon Z\to X$ be a morphism whose image is contained in the image
of $b$. If $b^*\mathcal F$ is finite locally constant, then so is
$a^*\mathcal F$. In particular, if $a$ and $b$ are immersions with the same
image, then $a^*\mathcal F$ is finite locally constant if and only if
$b^*\mathcal F$ is.
