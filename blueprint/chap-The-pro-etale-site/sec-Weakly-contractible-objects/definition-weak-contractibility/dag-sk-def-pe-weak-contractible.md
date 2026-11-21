+++
id = "dag-sk-def-pe-weak-contractible"
kind = "dag-definition"
title = "Weak contractibility"
name_showing = false
order = 75501
tags = ["sheaf-dag"]
split_from = "definition-weak-contractibility--1"
dag_id = "sk-def-pe-weak-contractible"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.GrothendieckTopology.IsWeaklyContractible"]
+++
An object $W$ of $X_{\mathrm{proét}}$ is *weakly contractible* if every epimorphism of
sheaves of sets $F\to h_W$ admits a section, where $h_W$ is the representable sheaf
associated to $W$. Equivalently, $h_W$ is projective in $\Sh(X_{\mathrm{proét}})$, or every
epimorphism $F\to G$ induces a surjection $F(W)\to G(W)$.

For the equivalence, pull an epimorphism $F\to G$ back along a section $h_W\to G$; the
resulting epimorphism onto $h_W$ splits. Conversely, surjectivity on sections lifts
$\mathrm{id}_{h_W}$ along any epimorphism onto $h_W$. This is the categorical definition of
Bhatt–Scholze, §3.2. The splitting condition concerns a cover as a whole: a disconnected
$W$ need not lift into a single member of a covering family.

(SHEAF DAG node `sk-def-pe-weak-contractible`; machine-alignment layer.) Split from [definition-weak-contractibility--1]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `sk-def-pe-site`.
