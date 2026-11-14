+++
id = "dag-det-pe-finite-tor-comparison-noetherian"
kind = "dag-lemma"
title = "Tor amplitude under comparison for Noetherian coefficients"
name_showing = false
order = 152501
tags = ["sheaf-dag"]
split_from = "corollary-finite-tor-amplitude-under-comparison--1"
dag_id = "det-pe-finite-tor-comparison-noetherian"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.finiteTorComparisonNoetherian"]
uses = ["dag-sk-thm-pe-constructible-comparison"]
+++
Let $X$ be quasi-compact and quasi-separated, $\Lambda$ a discrete Noetherian
ring and $K\in D^b_c(X_{\Et},\Lambda)$. For integers $a\leq b$, $K$ has Tor
amplitude in $[a,b]$ (that is, $K\otimes^{\mathrm L}_\Lambda N$ has cohomology
only in degrees $[a,b]$ for every $\Lambda$-module sheaf $N$ on $X_{\Et}$) if and
only if $\nu_X^*K$ has Tor amplitude in $[a,b]$ on $X_{\Proet}$. Consequently
$\nu_X^*$ restricts to an equivalence
$D^b_{\mathrm{ctf}}(X_{\Et},\Lambda)\simeq\Dctf(X,\Lambda)$.

(SHEAF DAG node `det-pe-finite-tor-comparison-noetherian`; machine-alignment layer.) Split from [corollary-finite-tor-amplitude-under-comparison--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-pbc-quasi-compact-scheme`, `def-weil-quasi-separated-morphism`, `def-weil-pbc-noetherian-ring`, `det-pe-classical-sheaves-modules`, `det-def-sfb-constructible-tor-amplitude`, `def-kun-derived-tensor`, `def-weil-proetale-tor-amplitude`.
