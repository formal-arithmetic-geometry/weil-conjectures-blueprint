+++
id = "theorem-extension-partial-section"
kind = "theorem"
title = "Extension of a partial section"
order = 1438
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection"]
uses = ["lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "definition-admissible-blow-up", "lemma-making-open-schematically-dense", "lemma-products-composites-u-admissible-blow", "proposition-relative-form-zariski-s-main"]
+++
Let $T$ be qcqs, let $U\subseteq V\subseteq T$ be quasi-compact opens
with $U$ dense in $T$, and let $p:Y\to T$ be separated and of finite
type. Suppose that $f:U\to Y$ is a section of $p$ over $U$ and that
its image is closed in $p^{-1}(V)$. There are a $V$-admissible blow-up
$\pi:T'\to T$, an open $W\subseteq T'$ containing $\pi^{-1}(U)$,
and a map $g:W\to Y$ such that

$$
p\circ g=\pi|_W,\qquad
g|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)},
$$

and the graph of $g$ is closed in $Y\times_TT'$.
