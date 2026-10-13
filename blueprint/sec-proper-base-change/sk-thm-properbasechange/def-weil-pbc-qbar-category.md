+++
id = "def-weil-pbc-qbar-category"
kind = "definition"
title = "Qbar-l coefficient category"
order = 1371
uses = ["def-weil-karoubi-envelope", "def-weil-pbc-common-stage-cones", "def-weil-pbc-finite-stage-pair-category"]
+++
For $\alpha\in\Qlb$ and $f=[M,u]$ in $\mathcal P_T$, choose a finite field
$N\supset M,\Ql(\alpha)$ and define
$$
 \alpha f=[N,\alpha u_N].
$$
Define
$$
 \Dbc(T,\Qlb)=\mathcal P_T:
$$
an object is a pair $(E,K)$ with $K\in\Dbc(T,E)$ at a finite stage $E$, and
a morphism is a class $[M,u]$ of
[def-weil-pbc-finite-stage-pair-category]. The shift is that of
[def-weil-pbc-common-stage-cones] and the distinguished triangles are the
common-stage cone triangles of [def-weil-pbc-common-stage-cones]; that these
data satisfy the Verdier axioms and give an ordinary triangulated category
is [thm-weil-pbc-verdier-axioms].

No Karoubi envelope is taken in this definition. The category is idempotent
complete, and the envelope $\Kar(\mathcal P_T)$ is canonically equivalent to
it.
