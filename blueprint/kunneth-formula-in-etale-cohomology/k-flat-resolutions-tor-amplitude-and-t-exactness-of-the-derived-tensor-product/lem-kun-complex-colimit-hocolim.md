+++
id = "lem-kun-complex-colimit-hocolim"
kind = "lemma"
title = "Sequential colimits represent homotopy colimits"
order = 6084
lean = ["CategoryTheory.Triangulated.hocolim_eq_colim_of_complexes"]
uses = ["def-kun-truncations"]
+++
For a sequence of complexes of étale sheaves on a site, the canonical
morphism from its homotopy colimit to its termwise colimit is a
quasi-isomorphism.

## Proof

Write $A=\bigoplus_nE_n$ and $u=1-\text{shift}:A\to A$. Termwise, $u$ is
injective: if $u(x)=0$ then $x_0=0$, then $x_1=x_0=0$, and inductively
$x_n=0$ for all $n$. Hence the short exact sequence of complexes
$0\to A\xrightarrow{u}A\to\operatorname{coker}(u)\to0$ gives a distinguished
triangle with third term $\operatorname{coker}(u)$, and in degree $i$ the
cokernel of $1-\text{shift}$ on $\bigoplus_nE_n^i$ is exactly the colimit
$\varinjlim_nE_n^i$; thus $\operatorname{coker}(u)$ is the termwise colimit
of the sequence. Since the homotopy colimit of [def-kun-truncations] is the
third term of the displayed triangle, it is canonically isomorphic to the
termwise colimit in the derived category.

Unresolved dependencies: def:weil-pbc-etale-sheaves, def:weil-pbc-derived-categories, lem:sp-long-exact-of-triangle
