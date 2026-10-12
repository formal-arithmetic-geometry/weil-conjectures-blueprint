+++
kind = "proof"
of = "lem-weil-pbc-fpqc-descend-flat"
+++
Apply the source repository theorem `Scheme.of_isPullback_of_ofArrows_mem_fpqcTopology` with the property `Flat`. The property is stable under base change by the Mathlib instance, and its descent instance along surjective flat quasi-compact morphisms is supplied by `WeilConjectures.Mathlib.AlgebraicGeometry.Morphisms.FlatDescent`. Instantiate the pullback legs with `pullback.fst` and `pullback.snd`, use `IsPullback.of_hasPullback`, and convert precoverage membership to topology membership with `Precoverage.generate_mem_toGrothendieck`. (`AlgebraicGeometry.Flat.isStableUnderBaseChange` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Flat.lean)), `AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean))).
