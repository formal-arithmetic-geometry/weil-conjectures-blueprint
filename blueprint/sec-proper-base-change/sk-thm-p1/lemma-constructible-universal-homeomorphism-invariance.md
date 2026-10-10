+++
id = "lemma-constructible-universal-homeomorphism-invariance"
kind = "lemma"
title = "Invariance under universal homeomorphisms"
order = 1168
lean = ["AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.of_upperStar", "AlgebraicGeometry.Scheme.IsFiniteSheaf.of_upperStar", "AlgebraicGeometry.Scheme.IsLocallyConstantSheaf.of_upperStar", "AlgebraicGeometry.Scheme.exists_comp_eq_of_surjective", "AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_iff", "CategoryTheory.Sheaf.isConstant_upperStar_iff"]
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-finite-locally-constant", "def-constructible-locally-constant", "def-kun-separably-closed", "lem-weil-pbc-closed-immersion-from-composite", "lemma-constructible-pullback-constant", "lemma-constructible-pullback-finite", "lemma-constructible-pullback-locally-constant", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-openclosed-stalk-upperstar", "prop-constructible-pullback", "prop-weil-pbc-universal-homeomorphism-topos", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $u\colon Z'\to Z$ be a universal homeomorphism. Then
$\mathcal G\in\shv{\et Z}$ is constant (locally constant) if and only if
$u^*\mathcal G$ is. If moreover $u$ is a surjective closed immersion, then
$\mathcal G$ is finite (finite locally constant) if and only if
$u^*\mathcal G$ is. More generally, if $p\colon W\to Z$ is surjective and
surjective on stalks (for instance a surjective closed immersion), then
every morphism $\operatorname{Spec}K\to Z$ with $K$ a field factors through
$p$.
