+++
id = "dag-det-pe-wcb-projective"
kind = "dag-lemma"
title = "Representables of w-contractible affines are projective"
name_showing = false
order = 69501
tags = ["sheaf-dag"]
split_from = "lemma-w-contractible-affines-projective"
dag_id = "det-pe-wcb-projective"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proetale_wContractible_projective"]
uses = ["dag-def-weil-pbc-small-proetale-site", "dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-wlocal"]
+++
Let $U=\operatorname{Spec}D$ with $D$ w-contractible be an object of $X_{\mathrm{proét}}$.

1. Every epimorphism of sheaves of sets $F\to h_U$ has a section.
2. $h_U$ is projective in $\Sh(X_{\mathrm{proét}})$: for every epimorphism $F\to G$, the map
   $F(U)\to G(U)$ is surjective.

(SHEAF DAG node `det-pe-wcb-projective`; machine-alignment layer.) Split from [lemma-w-contractible-affines-projective]. DAG kind: statement. DAG status: split.
