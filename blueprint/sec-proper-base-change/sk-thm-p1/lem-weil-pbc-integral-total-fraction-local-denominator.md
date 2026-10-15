+++
id = "lem-weil-pbc-integral-total-fraction-local-denominator"
kind = "lemma"
title = "Local denominators of integral total fractions"
lean = ["IsIntegral.exists_local_denominator_of_normal"]
+++
Let $R$ be a commutative ring, $Q(R)$ its localization at the nonzerodivisors `LocalizedModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)), $x\in Q(R)$ integral over $R$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)), and $p$ a prime with $R_p$ a normal domain `Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)) `IsIntegrallyClosed, IsDomain, Localization.AtPrime` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean)). Then there are $s\notin p$ and $a\in R$ such that $sx=a$ in $Q(R)$.
