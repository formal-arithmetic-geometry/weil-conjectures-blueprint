+++
id = "prop-constructible-pullback"
kind = "theorem"
title = "Pullback of constructible sheaves"
order = 1165
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.upperStar", "AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.upperStar"]
tags = ["latex:proposition"]
uses = ["def-constructible-constructible", "def-constructible-finite", "def-constructible-finite-locally-constant", "def-constructible-locally-constant", "def-constructible-stratification", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-finite", "lemma-constructible-pullback-locally-constant", "lemma-constructible-pullback-stratification"]
+++
Let $g\colon Y\to X$ be a morphism and let $\mathcal F\in\shv{\et X}$ be
constructible. Then $g^*\mathcal F$ is constructible. Likewise, if
$\mathcal F$ is finite locally constant, so is $g^*\mathcal F$. In particular
constructibility is preserved by restriction to an open, to a closed
subscheme, and to any locally closed subscheme.
