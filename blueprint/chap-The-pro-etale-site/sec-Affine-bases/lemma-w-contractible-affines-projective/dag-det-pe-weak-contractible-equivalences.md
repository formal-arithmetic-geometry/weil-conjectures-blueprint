+++
id = "dag-det-pe-weak-contractible-equivalences"
kind = "dag-lemma"
title = "Equivalent forms of weak contractibility"
name_showing = false
order = 69503
tags = ["sheaf-dag"]
split_from = "lemma-w-contractible-affines-projective--2"
dag_id = "det-pe-weak-contractible-equivalences"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proetale_weakContractible_equivalences"]
uses = ["dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-wlocal"]
+++
Let $W$ be an object of $X_{\mathrm{proét}}$ with representable sheaf
$h_W=\Hom_X(-,W)$ (`det-pe-topos-functoriality-site`). The following are equivalent:

1. every epimorphism of sheaves of sets $F\to h_W$ has a section;
2. $h_W$ is projective in $\Sh(X_{\mathrm{proét}})$: for every epimorphism $F\to G$ and every
   map $h_W\to G$ there is a lift $h_W\to F$;
3. for every epimorphism of sheaves $F\to G$ the map $F(W)\to G(W)$ is surjective.

An object satisfying these conditions is called *weakly contractible*. Every affine
$W=\operatorname{Spec}D$ with $D$ w-contractible is weakly contractible
([dag-det-pe-wcb-projective]).

(SHEAF DAG node `det-pe-weak-contractible-equivalences`; machine-alignment layer.) Split from [lemma-w-contractible-affines-projective--2]. DAG kind: statement. DAG status: split.
