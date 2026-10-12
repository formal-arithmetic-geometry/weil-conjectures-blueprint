+++
id = "sk-p-real-sections"
kind = "proposition"
title = "Global sections as invariants"
order = 2931
uses = ["sec-algebraic-groups-lie-algebras", "sk-d-real-operations", "sk-d-real-weil", "sk-i-real-sheaves"]
lean = ["AlgebraicGeometry.WeilGroup.globalSections_eq_invariants", "AlgebraicGeometry.WeilGroup.globalSections"]
tags = ["sketch"]
+++
Keep the notation of [sk-i-real-sheaves]. Let $U_0\subseteq C_0$ be a
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
