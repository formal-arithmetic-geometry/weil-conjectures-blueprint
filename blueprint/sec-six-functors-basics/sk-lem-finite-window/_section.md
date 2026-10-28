+++
id = "sk-lem-finite-window"
kind = "lemma"
title = "Reduction to finitely many degrees"
order = 2437
uses = ["sk-def-sfb-constructible", "sk-lem-uniform-constructible-ext", "sk-cor-ambient-ind-derived"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. Let $C\in\Cons(X,\Lambda)$ ([sk-def-sfb-constructible]), with $d_C$ as in
[sk-lem-uniform-constructible-ext], and let $K\in\Dic(X,\Lambda)$ ([sk-cor-ambient-ind-derived]) and
$m\in\mathbf Z$. The truncation maps induce a natural isomorphism

$$
\Hom(C,K[m])\simeq\Hom\bigl(C,(\tau_{\geq m-d_C}\tau_{\leq m}K)[m]\bigr).
$$
