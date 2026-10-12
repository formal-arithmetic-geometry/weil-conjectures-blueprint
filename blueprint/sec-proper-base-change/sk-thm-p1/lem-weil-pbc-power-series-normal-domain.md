+++
id = "lem-weil-pbc-power-series-normal-domain"
kind = "lemma"
title = "A power series ring over a Noetherian normal domain is a Noetherian normal domain"
lean = ["PowerSeries.noetherian_normal_domain"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 0BI0 (lemma-power-series-over-Noetherian-normal-domain), lines 8149-8174, statement and proof (Laurent series over the fraction field, Lemma almost-integral)"
+++
Let $R$ be a Noetherian `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) normal domain `IsIntegrallyClosed, IsDomain, Localization.AtPrime` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean)), and let $R[[x]]$ be the ring of formal power series in one variable $x$ over $R$ `MvPowerSeries` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/MvPowerSeries/Basic.lean)) (the case $n=1$). Then $R[[x]]$ is a Noetherian normal domain: it is Noetherian, an integral domain, and every element of its fraction field which is a root of a monic polynomial with coefficients in $R[[x]]$ lies in $R[[x]]$.
