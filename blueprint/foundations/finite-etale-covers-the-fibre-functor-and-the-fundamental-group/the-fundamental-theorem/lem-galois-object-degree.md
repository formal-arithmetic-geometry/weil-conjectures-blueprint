+++
id = "lem-galois-object-degree"
kind = "lemma"
title = "Galois covers and the degree"
order = 1966
uses = ["def-galois-fibre-functor", "def-galois-object", "lem-fet-galois-category", "lem-galois-axioms"]
+++
Let $Y$ be connected with a geometric point $\bar y$ and let
$P\to Y$ be a finite etale cover. Then $P$ is a
Galois cover if and only if $P$ is
connected over $Y$ and
$\#\operatorname{Aut}_Y(P)=\#P_{\bar y}$.

## Proof

By [lem-fet-galois-category] the pair
$(\mathrm{F\acute Et}(Y),F_{\bar y})$ is a Galois category, and
$F_{\bar y}(P)=P_{\bar y}$ by [def-galois-fibre-functor], so
that $\#P_{\bar y}$ is the degree of $P$ over $Y$. For connected
$P$ and a chosen $p\in P_{\bar y}$ the map
$\operatorname{Aut}_Y(P)\to P_{\bar y}$, $g\mapsto g\cdot p$, is
injective by [lem-galois-axioms](6), so
$\#\operatorname{Aut}_Y(P)\le\#P_{\bar y}$; the action of
[def-galois-object] is simply transitive exactly when it is
transitive and this inequality is an equality.
