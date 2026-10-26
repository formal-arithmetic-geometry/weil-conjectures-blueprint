+++
id = "prop-constructible-generic-constancy"
kind = "theorem"
title = "Generic constancy"
order = 1498
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.exists_dense_open", "AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.of_openCover", "Topology.Stratification.dense_iUnion_interior_stratum"]
tags = ["latex:proposition"]
uses = ["def-constructible-constructible", "def-constructible-finite-locally-constant", "def-constructible-stratification", "prop-constructible-pullback"]
+++
Let $X$ be a scheme and let $\mathcal F\in\shv{\et X}$ be constructible.
Then there is a dense open $U\subseteq X$ such that $\mathcal F|_U$ is
finite locally constant. (No Noetherian hypothesis on $X$ is needed.)
Moreover, for every finite stratification of a topological space the
union of the interiors of the strata is dense, and a sheaf
$\mathcal G\in\shv{\et X}$ whose pullbacks to the members of an open cover
of $X$ are finite locally constant is finite locally constant.
