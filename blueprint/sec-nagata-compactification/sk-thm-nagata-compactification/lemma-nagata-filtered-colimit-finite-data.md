+++
id = "lemma-nagata-filtered-colimit-finite-data"
kind = "lemma"
title = "Finite data and finite relations descend in a filtered colimit"
order = 30
lean = ["CommRingCat.exists_lift_forall_aeval_eq"]
uses = ["lemma-nagata-directed-finite-upper-bound"]
+++
Let $(A_i)_{i\in I}$ be a filtered diagram of commutative rings (for
instance a directed system) with colimit $A$. Given finitely many elements
$x_1,\ldots,x_n$ of $A$ and finitely many equalities $P_l(x)=Q_l(x)$ with
$P_l,Q_l\in\mathbf Z[X_1,\ldots,X_n]$, there exist one stage $i$ and lifts
$y_1,\ldots,y_n\in A_i$ of the $x_k$ such that every equality
$P_l=Q_l$ holds for the images of the $y_k$ under every transition
$A_i\to A_j$ (in particular for the $y_k$ themselves).
