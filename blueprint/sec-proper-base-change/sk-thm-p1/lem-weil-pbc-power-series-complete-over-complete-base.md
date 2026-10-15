+++
id = "lem-weil-pbc-power-series-complete-over-complete-base"
kind = "lemma"
title = "Power series over a complete Noetherian ring are complete for the combined ideal"
lean = ["power_series_complete_over_complete_base"]
+++
Let $\Lambda$ be a Noetherian ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) and $J\subseteq\Lambda$ an ideal such that $\Lambda$ is $J$-adically complete `IsAdicComplete` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/AdicCompletion/Basic.lean)). Let $d\ge0$, $R=\Lambda[[X_1,\ldots,X_d]]$ the formal power series ring `MvPowerSeries` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/MvPowerSeries/Basic.lean)), and $\mathfrak a=JR+(X_1,\ldots,X_d)$. Then $R$ is $\mathfrak a$-adically complete.
