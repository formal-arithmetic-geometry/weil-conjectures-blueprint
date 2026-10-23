+++
id = "lem-weil-pbc-weak-etale-integral-closure"
kind = "lemma"
title = "Integral closure after weakly etale base change"
order = 950
lean = ["Algebra.WeaklyEtale.isIntegrallyClosedIn_tensorProduct", "IsIntegrallyClosedIn.exists_weakDimensionLEOne_isEpi_exact"]
uses = ["def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-weak-etale-tor"]
+++
Let $A$ be a domain, let $K$ be a field containing $A$ and algebraic over
it, such that $A$ is integrally closed in $K$ (for instance $K$ the fraction
field of an integrally closed domain $A$), and let $B/A$ be weakly etale
[def-weil-pbc-ind-etale-algebra]. Then $B$ is integrally closed in
$B\otimes_AK$.
