+++
id = "det-finite-window-reduction"
kind = "lemma"
title = "The finite window from the lower tail vanishing"
order = 2221
uses = ["det-finite-window-unbounded", "sk-cor-ambient-ind-derived"]
+++
Let $\Lambda=E$ or $\Qlb$, $C\in\Cons(X,\Lambda)$ and $K\in\Dic(X,\Lambda)$. Assume that $\Hom(C,L)=0$ for
every $L\in\Dic(X,\Lambda)$ with $H^q(L)=0$ for $q>-d_C-1$. Then the maps
$K\leftarrow\tau_{\leq0}K\to\tau_{\geq-d_C}\tau_{\leq0}K$ induce isomorphisms

$$
\Hom(C,K)\xleftarrow{\ \sim\ }\Hom(C,\tau_{\leq0}K)\xrightarrow{\ \sim\ }\Hom(C,\tau_{\geq-d_C}\tau_{\leq0}K).
$$

Applied to $K[m]$ this gives the isomorphism of [sk-lem-finite-window].
