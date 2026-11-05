+++
id = "theorem-extension-partial-section--1"
kind = "theorem"
title = "Extension of a partial section (1)"
name_showing = false
order = 1441001
aliases = ["bp-r448-1"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection"]
uses = ["definition-admissible-blow-up--1"]
+++
Let $T$ and $Y$ be qcqs, let $U\subseteq V\subseteq T$ be quasi-compact
opens with $U$ dense in $T$, and let $p:Y\to T$ be separated,
quasi-compact and locally of finite type.
Suppose that $f:U\to Y$ is a section of $p$ over $U$ and that
its image is closed in $p^{-1}(V)$. There are a $V$-admissible blow-up
$\pi:T'\to T$, an open $W\subseteq T'$ containing $\pi^{-1}(U)$,
and a map $g:W\to Y$ such that

$$
p\circ g=\pi|_W,\qquad
g|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)},
$$

and the graph of $g$ is closed in $Y\times_TT'$.

Here quasi-compactness and local finite type of $p$ mean that $p$ is
of finite type. The explicit qcqs hypothesis on $Y$ follows from $T$
being qcqs and $p$ being separated and of finite type.
