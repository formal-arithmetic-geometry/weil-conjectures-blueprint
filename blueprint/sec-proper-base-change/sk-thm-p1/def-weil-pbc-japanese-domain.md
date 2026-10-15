+++
id = "def-weil-pbc-japanese-domain"
kind = "definition"
title = "N-1 and N-2 (Japanese) domains"
lean = ["IsN2"]
+++
Let $R$ be an integral domain with field of fractions $K$. (1) $R$ is *N-1* if the integral closure of $R$ in $K$ `integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean)) is a finitely generated $R$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)). (2) $R$ is *N-2*, or *Japanese*, if for every finite field extension $L/K$ `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)) (i.e. $\dim_KL<\infty$) the integral closure of $R$ in $L$, where $L$ is an $R$-algebra through the composite $R\subseteq K\to L$, is a finitely generated $R$-module. Taking $L=K$ shows that an N-2 domain is N-1.
