+++
id = "pur9-def-deformation-space"
kind = "definition"
title = "Deformation space of a section"
order = 3238
uses = ["pur9-def-section-invariant"]
+++
Let $g,s$ be as in Definition [pur9-def-section-invariant], and let $\mathcal I\subseteq\mathcal O_V$ be the ideal of $s(B)$. Put $\mathcal I^r:=\mathcal O_V$ for $r\leq0$, and let

$$
\mathcal R_s:=\bigoplus_{r\in\mathbf Z}\mathcal I^r\,t^{-r}\subseteq\mathcal O_V[t,t^{-1}],
$$

a quasi-coherent $\mathcal O_V$-algebra containing $\mathcal O_V[t]$ (the summands with $r\leq0$). The deformation space is $\mathcal D_sV:=\operatorname{Spec}_V(\mathcal R_s)$. The morphism $\widetilde g:\mathcal D_sV\to\Aaf^1_B$ is induced by $g$ and $\mathcal O_B[t]\to g_*\mathcal R_s$, $t\mapsto t$. The section $\widetilde s:\Aaf^1_B\to\mathcal D_sV$ is induced, over $s\circ p:\Aaf^1_B\to V$, by the $\mathcal O_V$-algebra map $\mathcal R_s\to(s\circ p)_*\mathcal O_{\Aaf^1_B}$ sending $f\,t^{-r}$ to $s^*(f)\,t^{-r}$ for $r\leq0$ and to $0$ for $r>0$.
