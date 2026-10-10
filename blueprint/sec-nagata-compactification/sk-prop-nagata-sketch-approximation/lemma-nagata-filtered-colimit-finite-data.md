+++
id = "lemma-nagata-filtered-colimit-finite-data"
kind = "lemma"
title = "Finite data and finite relations descend in a filtered colimit"
order = 331
uses = ["lemma-nagata-directed-finite-upper-bound"]
+++
Let $(A_i)_{i\in I}$ be a directed system of rings with colimit $A$. Given
finitely many elements of $A$ and finitely many equalities between ring
expressions in those elements, there exists one stage $i$ and lifts of all
selected elements to $A_i$ for which all selected equalities hold. Once
they hold at $i$, they hold after every transition $A_i\to A_j$.

## Proof

Choose a representative stage for each selected element. Directedness and
[lemma-nagata-directed-finite-upper-bound] place all representatives at
one common stage. Equality of two representatives in a filtered colimit is
witnessed at a later stage. There are only finitely many equalities, so a
second finite upper bound makes them all true simultaneously. Ring
homomorphisms preserve the equalities at every later stage.
