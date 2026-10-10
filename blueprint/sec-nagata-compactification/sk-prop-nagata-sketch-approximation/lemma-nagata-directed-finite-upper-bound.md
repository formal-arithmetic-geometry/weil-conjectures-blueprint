+++
id = "lemma-nagata-directed-finite-upper-bound"
kind = "lemma"
title = "Property of the selected finite upper bound"
order = 329
uses = ["def-nagata-directed-finite-upper-bound"]
+++
Every $i\in F$ satisfies $i\leq u(F)$.

## Proof

Induct on $F$. The empty case is vacuous. At an insertion step, the
selected $d(u(F),i)$ bounds both $u(F)$ and $i$; transitivity and the
induction hypothesis prove the assertion for all old and new elements.
