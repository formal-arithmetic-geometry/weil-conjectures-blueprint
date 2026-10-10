+++
kind  = "proof"
of    = "thm-weil-pbc-qbar-idempotent-complete"
+++
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
