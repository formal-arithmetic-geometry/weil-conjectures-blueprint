+++
id = "lem-weil-pbc-local-rings-ind-zariski"
kind = "lemma"
title = "Local-ring identifications with w-local target"
order = 952
lean = ["Algebra.BijectiveOnStalks.indZariski_of_isWLocal", "RingHom.BijectiveOnStalks.indZariski_of_isWLocal"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-w-local", "lem-weil-pbc-w-local-partition"]
+++
Suppose $A\to B$ identifies every local ring: for every prime $q\subset B$,
the map $A_{q\cap A}\to B_q$ is an isomorphism. If $\operatorname{Spec}A$ and
$\operatorname{Spec}B$ are w-local [def-weil-pbc-w-local] and every maximal
ideal of $B$ contracts to a maximal ideal of $A$, then $B/A$ is ind-Zariski
[def-weil-pbc-ind-etale-algebra].
