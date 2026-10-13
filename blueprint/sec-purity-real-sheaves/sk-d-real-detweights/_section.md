+++
id = "sk-d-real-detweights"
kind = "definition"
title = "Determinant weights and weight blocks"
order = 2975
uses = ["sk-d-real-operations", "sk-d-real-weights", "sk-p-real-rankone"]
lean = ["AlgebraicGeometry.WeilGroup.HasDetWeight"]
tags = ["sketch"]
+++
A Weil sheaf $V$ given by a representation of $W(C_0)$ on a
$\Qlb$-vector space of finite dimension $r$ has determinant weight $\gamma\in\mathbf R$
if $\det V$ is punctually $\iota$-pure of weight $r\gamma$, i.e.
$\wt_{\iota,q_x}(\det F_x\mid V)=r\gamma$ for every closed point $x$.
For a nonzero irreducible Weil sheaf $V$,
rank-one purity assigns a unique
pure weight to $\det V$, so $V$ has exactly one determinant weight

$$
\dw_\iota(V)=\frac{\wt_\iota(\det V)}{\operatorname{rank}V}.
$$

For a general sheaf, its constituent determinant weights are the numbers
$\dw_\iota(V_a)$ for its irreducible constituents.
The rank-counted list repeats $\dw_\iota(V_a)$ exactly
$r_a=\operatorname{rank}V_a$ times.
For a semisimple sheaf $\mathcal S=\bigoplus_aV_a$, its block of weight
$\gamma$ and the ranks and weight sum above that block are

$$
\mathcal S(\gamma)=\bigoplus_{\dw_\iota(V_a)=\gamma}V_a,\qquad
N_\gamma=\sum_{\dw_\iota(V_a)>\gamma}r_a,\qquad
B_\gamma=\sum_{\dw_\iota(V_a)>\gamma}r_a\dw_\iota(V_a).
$$
