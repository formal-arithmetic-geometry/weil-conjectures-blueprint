+++
id = "p-real-sections"
kind = "theorem"
title = "Global sections as invariants"
order = 2750
uses = ["def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-weil-fundamental-representation", "lem-wf-weil-group-constant-extension", "lem-wf-weil-group-exact-sequence", "rem-ptr-wf-weil-group-1"]
tags = ["latex:proposition"]
+++
Keep the notation of [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation]. Let $U_0\subseteq C_0$ be a
nonempty open subscheme, $U=U_0\times_{\Fq}k$ its base change and $\pi_1(U)$
its geometric fundamental group; restriction gives the Weil group $W(U_0)$
with geometric subgroup $\pi_1(U)$. For a subgroup $I$ write
$V^{I}=\{v\in V:gv=v\text{ for all }g\in I\}$ for the invariants, as in
[sk-d-real-operations], and let $H^0$ denote ordinary etale global
sections. Then

$$
H^0\bigl(U,\mathcal F|_{U}\bigr)=V^{\pi_1(U)},
$$

compatibly with the residual action of $F=\rho(\gamma)$ on both sides.

## Proof

Apply [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation] on the connected $U$. A global section of
$\mathcal F|_{U}$ is a morphism from the constant rank-one sheaf, hence under
the equivalence a map of $\pi_1(U)$-representations from the trivial line to
$V$. Such a map is determined by the image of $1$, which must be fixed by
every element; conversely every fixed vector defines one. This gives
$H^0(U,\mathcal F|_{U})=V^{\pi_1(U)}$. The subgroup $\pi_1(U)$ is normal in
$W(U_0)$, so the degree-one lift normalizes its action and therefore preserves
the invariants; the identification is equivariant for the residual $F$.

Uses: [sk-d-real-operations], [def-wf-weil-group], [lem-wf-weil-group-constant-extension], [lem-wf-weil-group-exact-sequence], [rem-ptr-wf-weil-group-1], [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation]
