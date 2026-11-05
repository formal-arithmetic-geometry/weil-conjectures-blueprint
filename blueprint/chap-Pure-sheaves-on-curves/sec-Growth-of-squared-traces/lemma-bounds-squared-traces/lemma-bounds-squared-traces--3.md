+++
id = "lemma-bounds-squared-traces--3"
kind = "lemma"
title = "Bounds for squared traces (3)"
name_showing = false
order = 1202004
aliases = ["bp-r371-3"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_boundaryEnergy_le"]
uses = ["definition-weights", "definition-trace-function", "definition-growth-squared-traces"]
+++
The bound for arbitrary complexes with finite support is bypassed by
Lean; the boundary estimate used in its place is the following.

Let $j:U_0\hookrightarrow\Aone_{k_0}$ be a quasi-compact dense open
immersion, and let $M$ be a lisse Weil sheaf on $U_0$, punctually of
weights $\le a$. Put

$$
E_n=\sum_{y\in\Aone(k_n),\;y\notin U_0(k_n)}
|\iota t_{j_*M,n}(y)|^2.
$$

There is a constant $C\in\mathbf R$ such that $E_n\le Cq^{na}$ for
every $n\in\mathbf N$.
