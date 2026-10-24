+++
id = "lem-pc-projective-proper"
kind = "lemma"
title = "Projective morphisms are proper"
lean = ["AlgebraicGeometry.IsHProjective.isProper", "AlgebraicGeometry.IsSmoothProjectiveCurve.isProper_baseChangeField"]
order = 826
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-pc-projective-morphism", "def-pc-smooth-projective-curve", "lem-pc-proper-base-change"]
+++
Every H-projective morphism of schemes ([def-pc-projective-morphism]), in
particular every projective morphism, is proper. In particular a smooth
projective curve over a field is proper over it, and its base changes along
field extensions are proper.
