+++
id = "lemma-artin-schreier-character-sheaf--6"
kind = "lemma"
title = "Frobenius trace"
order = 1220012
aliases = ["bp-r375-6"]
lean = ["AlgebraicGeometry.WeilSheaf.traceFunction_artinSchreier"]
uses = ["definition-trace-function", "lemma-artin-schreier-character-sheaf--1"]
+++
For every $a\in k_0$, every $n\geq1$, and every $x\in\Fqn$, the trace of
local geometric Frobenius on the sheaf $\mathcal L_{\psi(ax)}$ of
[lemma-artin-schreier-character-sheaf--3] is

$$
t_{\mathcal L_{\psi(ax)},n}(x)
=\psi\bigl(\operatorname{Tr}_{\Fqn/k_0}(ax)\bigr).
$$

In particular, $a=1$ gives the asserted trace function of $\mathcal L_\psi$.
