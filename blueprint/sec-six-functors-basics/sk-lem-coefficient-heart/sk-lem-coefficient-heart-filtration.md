+++
id = "det-lem-coefficient-heart-filtration"
kind = "lemma"
title = "Filtration of a constructible sheaf by extensions by zero of lisse sheaves"
uses = ["det-lem-coefficient-heart-common-stratification", "det-lem-coefficient-heart-closure"]
+++
Let $X$ be a Noetherian scheme, $\Lambda=E$ or $\Qlb$, and $F\in\Cons(X,\Lambda)$. Let
$S_1,\dots,S_m$ be a stratification adapted to $F$, ordered as in
[det-lem-coefficient-heart-common-stratification] (1), so that $V_k=S_1\cup\dots\cup S_k$ is
open, with open immersions $v_k\colon V_k\hookrightarrow X$, and let $a_k\colon S_k\hookrightarrow X$.
Put $F_k=v_{k!}v_k^*F\subseteq F$. Then
$$
0=F_0\subset F_1\subset\dots\subset F_m=F,\qquad F_k/F_{k-1}\cong a_{k!}(F|_{S_k}),
$$
and each $F|_{S_k}$ is lisse.
