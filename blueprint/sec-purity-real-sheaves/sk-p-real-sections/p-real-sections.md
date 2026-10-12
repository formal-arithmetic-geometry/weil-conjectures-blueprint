+++
id = "p-real-sections"
kind = "theorem"
title = "Global sections as invariants"
order = 2934
uses = ["def-real-weil-representation-operations", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-weil-group-exact-sequence", "prop-wf-weil-sheaf-representation-equivalence"]
tags = ["latex:proposition"]
+++
Keep the notation of [prop-wf-weil-sheaf-representation-equivalence]. Let $U_0\subseteq C_0$ be a
nonempty open subscheme, $U=U_0\times_{\Fq}k$ its base change and $\pi_1(U)$
its geometric fundamental group; restriction gives the Weil group $W(U_0)$
of [def-wf-weil-group]
with geometric subgroup $\pi_1(U)$. For a subgroup $I$ write
$V^{I}=\{v\in V:gv=v\text{ for all }g\in I\}$ for the invariants of
[def-real-weil-representation-operations], and let
$H^0$ denote ordinary etale global
sections. Then

$$
H^0\bigl(U,\mathcal F|_{U}\bigr)=V^{\pi_1(U)},
$$

compatibly with the residual action of $F=\rho(\gamma)$ on both sides, where
$\rho$ is the Weil fundamental representation of
[def-wf-fundamental-representation].
