+++
id = "lem-weil-pbc-normal-ring-integrally-closed-total"
kind = "lemma"
title = "A normal ring is integrally closed in its total ring of fractions"
lean = ["integral_totalFraction_mem_range_of_normal"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 034M (lemma-normal-ring-integrally-closed, line 8218), with its proof"
+++
Let $R$ be a commutative normal ring `IsIntegrallyClosed, IsDomain, Localization.AtPrime` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean)). Let $S$ be the set of nonzerodivisors of $R$ and $Q(R)=S^{-1}R$ its total ring of fractions `LocalizedModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)). Then every element of $Q(R)$ integral over $R$ lies in the image of the localization map $R\to Q(R)$; equivalently, $R$ is integrally closed in $Q(R)$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)).
