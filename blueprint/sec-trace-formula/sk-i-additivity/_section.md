+++
id = "sk-i-additivity"
kind = "proposition"
title = "Localization trace additivity"
order = 2655
uses = ["sk-d-curve-pieces", "sk-d-integral", "sk-d-local-term", "sk-d-trace-class"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.traceClass_graph_eq_traceClass_add_traceClass"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field, $X$ quasi-compact and compactifiable over
$s$, and let $(K,\varphi)$ be a Weil complex on $X$ in the sense of [sk-d-weil],
with $K\in D^b_{ctf}(X,A)$ and arbitrary (not necessarily invertible) Frobenius
coefficient morphism $\varphi$; fix $m\ge0$. Let $i:Z\to X$ be a closed immersion
and $j:U\to X$ the complementary open immersion, with endomorphisms
$\Phi_Z$ of $Z$ and $\Phi_U$ of $U$ such that $\Phi_mi=i\Phi_Z$ and the square
$\Phi_mj=j\Phi_U$ is Cartesian. Let $K^Z=Ri_*i^*K$ and $K^U=Rj_!j^*K$, assumed in
$D^b_{ctf}(X,A)$, carry the coefficient morphisms $u^Z$, $u^U$ induced by
$\varphi_m$ as in [sk-d-curve-pieces]. Then the trace classes of the graph
correspondences $(1,\Phi_m)$ satisfy

$$
\Tr_{(1,\Phi_m)}(\varphi_m)=\Tr_{(1,\Phi_m)}(u^Z)+\Tr_{(1,\Phi_m)}(u^U)
$$

as maps $A_F\to\omega_F$ on the fixed scheme $F=\Fix(1,\Phi_m)$.
