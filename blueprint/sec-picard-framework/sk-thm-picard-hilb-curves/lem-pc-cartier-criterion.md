+++
id = "lem-pc-cartier-criterion"
kind = "lemma"
title = "The Cartier criterion on smooth one-dimensional fibres"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isInvertible_of_locallyQuasiFinite_of_field", "AlgebraicGeometry.Scheme.IdealSheafData.isInvertible_of_locallyQuasiFinite_of_flat", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isFinite_and_locallyOfFinitePresentation", "AlgebraicGeometry.Scheme.IdealSheafData.isInvertible_of_isFinite_of_flat", "AlgebraicGeometry.Scheme.IdealSheafData.isRelativeEffectiveCartier_of_isFinite", "AlgebraicGeometry.Scheme.IdealSheafData.isRelativeEffectiveCartier_iff_locallyQuasiFinite", "AlgebraicGeometry.Scheme.IdealSheafData.locallyOfFinitePresentation_of_locallyQuasiFinite"]
order = 810
uses = ["cor-pqf-proper-quasifinite-finite", "def-pc-finite-locally-free", "def-pc-morphism-conventions", "def-pc-relative-effective-cartier", "def-nagata-invertible-ideal", "lem-pc-recd-locally-principal", "lem-sc-cartier-divisor-points", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular", "pqf-lem-locqf-fibre-discrete", "lem-sc-point-cartier"]
+++
Let
$X\to S$ be a smooth morphism of relative dimension $1$ and let
$D\subset X$ be a closed subscheme. Consider:

1. **(1)** $D\to S$ is finite locally free;
1. **(2)** $D$ is a relative effective Cartier divisor on $X/S$;
1. **(3)** $D\to S$ is locally quasi-finite, flat and locally of finite
presentation;
1. **(4)** $D\to S$ is locally quasi-finite and flat.

Then $(1)\Rightarrow(2)\Leftrightarrow(3)\Rightarrow(4)$. If $S$ is
locally Noetherian the last arrow is an if-and-only-if; if $X\to S$ is
proper, the first arrow is an if-and-only-if.
