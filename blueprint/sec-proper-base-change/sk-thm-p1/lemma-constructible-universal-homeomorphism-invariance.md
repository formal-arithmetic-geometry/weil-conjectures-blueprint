+++
id = "lemma-constructible-universal-homeomorphism-invariance"
kind = "lemma"
title = "Invariance under universal homeomorphisms"
order = 1168
lean = ["AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.of_upperStar", "AlgebraicGeometry.Scheme.IsFiniteSheaf.of_upperStar", "AlgebraicGeometry.Scheme.IsLocallyConstantSheaf.of_upperStar", "AlgebraicGeometry.Scheme.exists_comp_eq_of_surjective", "AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_iff", "CategoryTheory.Sheaf.isConstant_upperStar_iff"]
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-finite-locally-constant", "def-constructible-locally-constant", "lemma-constructible-pullback-finite", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $u\colon Z'\to Z$ be a universal homeomorphism. Then
$\mathcal G\in\shv{\et Z}$ is constant (locally constant) if and only if
$u^*\mathcal G$ is. If moreover $u$ is a surjective closed immersion, then
$\mathcal G$ is finite (finite locally constant) if and only if
$u^*\mathcal G$ is. More generally, if $p\colon W\to Z$ is surjective and
surjective on stalks (for instance a surjective closed immersion), then
every morphism $\operatorname{Spec}K\to Z$ with $K$ a field factors through
$p$.
