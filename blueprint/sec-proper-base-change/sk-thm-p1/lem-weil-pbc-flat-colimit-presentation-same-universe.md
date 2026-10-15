+++
id = "lem-weil-pbc-flat-colimit-presentation-same-universe"
kind = "lemma"
title = "Flatness from a same-universe filtered colimit presentation"
lean = ["ModuleCat.flat_of_colimitPresentation"]
+++
Let R be a commutative ring in Type w, J a small filtered category in Type w, M an object of ModuleCat.{w} R, and P a colimit presentation of M indexed by J. If every P.diag.obj j is flat over R `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)), then M is flat over R. A colimit presentation is a diagram with a cocone of vertex M whose cocone is a colimit `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)).
