+++
id = "lem-weil-pbc-integrally-closed-reduced-finite-domain-decomposition"
kind = "lemma"
title = "Integral closedness lifts the finite minimal-prime decomposition to domain factors"
lean = ["exists_finite_domain_factors_of_integrallyClosed_totalFractions"]
source = "literature/stacks-project/algebra.tex, Algebra, Tag 030C (lemma-characterize-reduced-ring-normal), proof, second and third paragraphs; https://stacks.math.columbia.edu/tag/030C"
+++
Let $R$ be a reduced commutative ring with finitely many minimal prime ideals. Suppose $R$ is integrally closed `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)) in its total ring of fractions $Q(R)$ `LocalizedModule` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)). Then for some integer $n\ge 0$ there are commutative integral domains $A_i$ for $i\in\operatorname{Fin}(n)$ and a ring isomorphism $R\simeq\prod_i A_i$. No integral closedness of the factors is asserted.
