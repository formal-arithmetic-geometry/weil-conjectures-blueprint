+++
id = "dag-det-pe-sections-conservative"
kind = "dag-lemma"
title = "Evaluation on weakly contractible affines is conservative"
name_showing = false
order = 79502
tags = ["sheaf-dag"]
split_from = "corollary-evaluation-weakly-contractible-objects--6"
dag_id = "det-pe-sections-conservative"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.ProEt.sections_conservative"]
uses = ["dag-def-weil-pbc-small-proetale-site", "dag-sk-def-pe-weak-contractible"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{proét}}$ and let $\mathcal W$ be the
class of affine weakly contractible objects of $X_{\mathrm{proét}}$.

1. A sequence $A\xrightarrow{f}B\xrightarrow{g}C$ of $\mathcal R$-modules with $g\circ f=0$
   is exact at $B$ if and only if $A(W)\to B(W)\to C(W)$ is exact for every
   $W\in\mathcal W$.
2. A complex of $\mathcal R$-modules is acyclic if and only if its evaluation at every
   $W\in\mathcal W$ is acyclic.
3. A morphism of $\mathcal R$-modules is an isomorphism if and only if its evaluation at
   every $W\in\mathcal W$ is bijective; a morphism of complexes is a quasi-isomorphism if and
   only if its evaluation at every $W\in\mathcal W$ is a quasi-isomorphism.

(SHEAF DAG node `det-pe-sections-conservative`; machine-alignment layer.) Split from [corollary-evaluation-weakly-contractible-objects--6]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-sheaf-of-modules-category`, `sk-def-pbc-conventions`.
