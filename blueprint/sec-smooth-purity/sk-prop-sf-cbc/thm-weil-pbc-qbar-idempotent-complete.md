+++
id = "thm-weil-pbc-qbar-idempotent-complete"
kind = "theorem"
title = "The Qbar-l category is idempotent complete"
order = 1542
uses = ["def-weil-karoubi-envelope", "def-weil-pbc-qbar-category", "lem-weil-karoubi-envelope-fully-faithful", "lem-weil-karoubi-envelope-triangulated", "prop-weil-filtered-retract-descent", "thm-weil-pbc-finite-stage-karoubian"]
+++
The category $\Dbc(T,\Qlb)=\mathcal P_T$ of
[def-weil-pbc-qbar-category] is idempotent complete, and the canonical fully
faithful functor $\Dbc(T,\Qlb)\to\Kar(\Dbc(T,\Qlb))$ is an exact
equivalence.

## Proof

By [thm-weil-pbc-finite-stage-karoubian] every finite-stage category
$\Dbc(T,E)$ is idempotent complete, so [prop-weil-filtered-retract-descent]
applies with $\mathcal P_T=\Dbc(T,\Qlb)$, as defined in
[def-weil-pbc-qbar-category]: every idempotent of $\Dbc(T,\Qlb)$ splits. The
canonical functor into the Karoubi envelope is fully faithful, and it is
essentially surjective: an object $((E,K),e)$ of the envelope is split by
the splitting of $e$ in $\mathcal P_T$ (the idempotent completeness just
proved), say by $K'\in\mathcal P_T$, $i:K'\to(E,K)$, $p:(E,K)\to K'$ with
$p\,i=\operatorname{id}$ and $i\,p=e$, and then $i$ and $p$ exhibit the
isomorphism $((E,K),e)\cong(K',\operatorname{id}_{K'})$ of the envelope (the
Karoubi-morphism conditions $p=p\circ e$ and $i=e\circ i$ follow from
$p\,i=\operatorname{id}$ and $i\,p=e$). Hence the functor is essentially
surjective, and exact because the envelope of a triangulated category is
triangulated with the canonical functor exact.
