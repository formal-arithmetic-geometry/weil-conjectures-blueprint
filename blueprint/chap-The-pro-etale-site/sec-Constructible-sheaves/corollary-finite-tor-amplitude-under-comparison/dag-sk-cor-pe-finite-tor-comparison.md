+++
id = "dag-sk-cor-pe-finite-tor-comparison"
kind = "dag-lemma"
title = "Finite Tor amplitude under comparison"
name_showing = false
order = 152506
tags = ["sheaf-dag"]
split_from = "corollary-finite-tor-amplitude-under-comparison--1"
dag_id = "sk-cor-pe-finite-tor-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.finiteTorComparisonNoetherian"]
uses = ["dag-sk-thm-pe-constructible-comparison"]
+++
For a qcqs scheme $X$ and a discrete Noetherian ring $\Lambda$, the equivalence
$\nu_X^*\colon D^b_c(X_{\Et},\Lambda)\to\Dbc(X,\Lambda)$ of
[dag-sk-thm-pe-constructible-comparison] restricts to

$$
\Dctf(X,\Lambda)\simeq D^b_{\mathrm{ctf}}(X_{\Et},\Lambda).
$$

In particular the corollary applies to every finite commutative $\ell$-primary
ring $A$, regular or not.

(SHEAF DAG node `sk-cor-pe-finite-tor-comparison`; machine-alignment layer.) Split from [corollary-finite-tor-amplitude-under-comparison--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-quasi-compact-scheme`, `def-weil-quasi-separated-morphism`, `def-weil-pbc-noetherian-ring`, `det-def-sfb-constructible-tor-amplitude`, `def-kun-tor-amplitude`.
