+++
id = "lem-pc-smooth-characterization"
kind = "lemma"
title = "Smoothness versus flatness"
lean = ["AlgebraicGeometry.smooth_iff_flat_and_smooth_fiber", "AlgebraicGeometry.smooth_iff_flat_locallyOfFinitePresentation_smooth_fiberToSpecResidueField"]
order = 820
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-weil-scheme-morphism-properties"]
+++
Let $f:X\to S$ be a morphism of
locally finite presentation.
Then $f$ is smooth if and only if $f$
is flat and every fibre $X_s$ is smooth over $\kappa(s)$.
