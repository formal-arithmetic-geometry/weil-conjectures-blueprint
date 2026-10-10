+++
id = "lem-weil-pbc-rectangle-derived-limit"
kind = "lemma"
title = "The rectangle passes to the derived limit"
order = 1346
uses = ["def-weil-pbc-derived-inverse-limit", "lem-weil-pbc-tower-compatibility", "prop-weil-pbc-rlim-functoriality"]
+++
Put
$$
 A_\infty=\Rlim A_\bullet,\quad
 B_\infty=\Rlim B_\bullet,\quad
 C_\infty=\Rlim C_\bullet,\quad
 D_\infty=\Rlim D_\bullet,
$$
and let $H,V,H',V'$ be the images under the triangulated functor $\Rlim$ ([prop-weil-pbc-rlim-functoriality]) of
the four compatible tower morphisms $h,v,h',v'$. Then
$$
 V'H=H'V:A_\infty\longrightarrow D_\infty.
$$
The $n$-th component of both sides is the equality $v'_nh_n=h'_nv_n$ at
level $n$.

## Proof

The triangle functor $\Rlim$ of the derived inverse limit preserves the
rectangle commutation of [lem-weil-pbc-tower-compatibility], and evaluation
at $n$ recovers the finite-level equality.
