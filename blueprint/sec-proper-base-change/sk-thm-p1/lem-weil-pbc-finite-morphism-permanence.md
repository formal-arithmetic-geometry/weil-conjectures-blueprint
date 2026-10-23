+++
id = "lem-weil-pbc-finite-morphism-permanence"
kind = "lemma"
title = "Base change, affineness and properness for finite morphisms"
uses = ["def-weil-finite-integral-morphism", "def-pc-base-change", "def-pc-scheme", "def-weil-proper-morphism"]
lean = ["AlgebraicGeometry.IsFinite", "AlgebraicGeometry.HasAffineProperty.affineAnd_isStableUnderBaseChange", "RingHom.finite_isStableUnderBaseChange", "AlgebraicGeometry.isAffine_of_isAffineHom", "AlgebraicGeometry.IsFinite.iff_isProper_and_isAffineHom", "AlgebraicGeometry.IsProper.stableUnderComposition"]
order = 1786
tags = ["mathlib", "stacks-01WL"]
+++
Let $f:X\to Y$ be a finite morphism of schemes [def-weil-finite-integral-morphism]. (a) For every morphism $g:Y'\to Y$, the projection $f':X\times_YY'\to Y'$ from the fibre product [def-pc-base-change] is finite. (b) If $Y$ is affine [def-pc-scheme], then $X$ is affine. (c) If $h:Y\to S$ is proper [def-weil-proper-morphism], then $h\circ f:X\to S$ is proper; in particular, if $Y$ is proper over a field $k$, so is $X$ (with structure morphism $h\circ f$).
