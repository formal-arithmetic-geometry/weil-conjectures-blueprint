+++
id = "lemma-constructible-of-refines"
kind = "lemma"
title = "Constructibility passes to refinements"
order = 1294
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.of_refines", "AlgebraicGeometry.Scheme.Stratification.Refines.isFiniteLocallyConstantSheaf_upperStar"]
uses = ["def-constructible-constructible", "def-constructible-finite-locally-constant", "def-constructible-refines", "def-constructible-stratification", "prop-constructible-pullback"]
+++
Let $(\iota_k\colon Z_k\to X)_k$ be a stratification with all
$\iota_k^*\mathcal F$ finite locally constant, and let
$(\kappa_l\colon W_l\to X)_l$ refine it. Then all $\kappa_l^*\mathcal F$
are finite locally constant; in particular $\mathcal F$ is constructible.
