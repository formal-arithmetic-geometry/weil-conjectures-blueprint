+++
id = "def-sfb-conjugate-pull-iso"
kind = "definition"
title = "The conjugate isomorphism in a square of adjunctions"
order = 1339
lean = ["CategoryTheory.Adjunction.pullIsoOfComapIso"]
+++
Consider four adjunctions

$$
E_1\dashv\mathrm{Res}_1\colon\mathcal A\rightleftarrows\mathcal B,\quad
E_2\dashv\mathrm{Res}_2\colon\mathcal A'\rightleftarrows\mathcal B',\quad
U_1\dashv L_1\colon\mathcal A'\rightleftarrows\mathcal A,\quad
U_2\dashv L_2\colon\mathcal B'\rightleftarrows\mathcal B
$$

(left adjoints $E_1\colon\mathcal A\to\mathcal B$, $E_2\colon\mathcal A'\to\mathcal B'$,
$U_1\colon\mathcal A'\to\mathcal A$, $U_2\colon\mathcal B'\to\mathcal B$), and a natural
isomorphism $e\colon\mathrm{Res}_2\circ L_2\cong L_1\circ\mathrm{Res}_1$ of functors
$\mathcal B\to\mathcal A'$ between the composites of right adjoints. The *conjugate* of $e$ is
the natural isomorphism

$$
E_1\circ U_1\;\cong\;U_2\circ E_2\colon\mathcal A'\longrightarrow\mathcal B
$$

corresponding to $e$ under the bijection between natural transformations of left adjoints and
of right adjoints for the composite adjunctions $E_1U_1\dashv L_1\mathrm{Res}_1$ and
$U_2E_2\dashv\mathrm{Res}_2L_2$.
