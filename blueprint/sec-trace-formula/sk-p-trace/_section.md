+++
id = "sk-p-trace"
kind = "proposition"
title = "Trace on perfect complexes"
order = 2646
uses = ["sk-d-trace"]
lean = ["DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace"]
tags = ["sketch"]
+++
For a commutative ring $R$, a bounded finite-projective complex $P^\bullet$,
and a chain endomorphism $v$, the categorical trace is

$$
\tr_R(v\mid P^\bullet)=\sum_i(-1)^i\Tr_R(v^i\mid P^i).
$$
