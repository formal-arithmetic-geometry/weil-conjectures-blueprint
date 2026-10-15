+++
id = "sk-lem-finite-window"
kind = "lemma"
title = "Reduction to finitely many degrees"
order = 1526
uses = ["sk-cor-ind-heart-ii", "sk-cor-ambient-ind-derived", "sk-lem-uniform-constructible-ext"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. Let $C\in\Cons(X,\Lambda)$, with $d_C$ as in
[sk-lem-uniform-constructible-ext], $K\in\Dic(X,\Lambda)$ ([sk-cor-ambient-ind-derived]) and
$m\in\mathbf Z$. The truncation maps induce a natural isomorphism

$$
\Hom(C,K[m])\cong\Hom\bigl(C,(\tau_{\geq m-d_C}\tau_{\leq m}K)[m]\bigr).
$$

Because of the uniform bound $d_C$, maps out of a constructible sheaf $C$ into an unbounded complex see
only finitely many of its cohomology sheaves.
