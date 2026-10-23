+++
kind = "proof"
of = "lem-weil-pbc-etale-qcqs-cofinal-finite-coverings"
uses = ["def-weil-pbc-etale-site"]
+++
The family $(T_a\to U)_a$ is jointly surjective and étale, so it generates a covering sieve of $U$ [def-weil-pbc-etale-site]. For each $u\in U$ choose $a$ and a point $t\in T_a$ over $u$, and an affine open neighbourhood $V_u\subseteq T_a$ of $t$; the composite $V_u\to T_a\to U$ is étale, hence open, so its image is an open neighbourhood of $u$. Since $U$ is quasi-compact, finitely many of these images cover $U$; this gives the finite family $(V_b\to U)_{b\in B}$ of affine étale $U$-schemes, jointly surjective, each factoring through some $T_{a(b)}\to U$ by construction.

Each $V_b$ is affine, hence quasi-compact, and $U$ is quasi-separated, so $V_b\to U$ is quasi-compact. Quasi-compact morphisms are stable under base change, so the projection $V_b\times_UV_{b'}\to V_b$ is quasi-compact; as $V_b$ is quasi-compact, so is $V_b\times_UV_{b'}$.
