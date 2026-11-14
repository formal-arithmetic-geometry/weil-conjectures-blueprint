+++
id = "dag-sk-def-pe-wlocal"
kind = "dag-definition"
title = "The local hierarchy"
name_showing = false
order = 43504
tags = ["sheaf-dag"]
split_from = "definition-w-local-w-strictly-local--2"
dag_id = "sk-def-pe-wlocal"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["WLocalSpace", "IsWLocalRing", "IsWStrictlyLocalRing", "IsWContractibleRing"]
+++
Let $T$ be a spectral topological space `def-weil-spectral-space`, and write
$T^c=\{c\in T:\{c\}\text{ is closed in }T\}$ for its closed points.
For $x,c\in T$, saying that $x$ specializes to $c$ means
$c\in\overline{\{x\}}$. The space $T$ is *w-local* if $T^c$ is closed in $T$
and every $x\in T$ specializes to exactly one point of $T^c$.

Let $R$ be a commutative ring, and give $\operatorname{Spec}(R)$ its Zariski
topology `def-weil-affine-spectrum`. This affine scheme is quasi-compact and
quasi-separated `lem-weil-pbc-affine-scheme-qcqs`, so its underlying space is spectral
`lem-weil-pbc-qcqs-scheme-spectral`. The ring $R$ is *w-local* if
$\operatorname{Spec}(R)$ is w-local. It is *w-strictly local* if it is w-local
and, for every maximal ideal $\mathfrak m\subset R$, the localization
$R_{\mathfrak m}$ `def-weil-pbc-localization-at-prime` is strictly henselian
`def-weil-pbc-henselian-terminology`. It is *w-contractible* if it is
w-strictly local and the profinite space $\pi_0(\operatorname{Spec}(R))$
[dag-lem-pe-spectral-components-profinite] is extremally disconnected.
Here $\pi_0(X)$ denotes the quotient of $X$ by its connected components
(maximal connected subsets), with the quotient topology; *extremally disconnected*
means that the closure of every open subset is open.

(SHEAF DAG node `sk-def-pe-wlocal`; machine-alignment layer.) Split from [definition-w-local-w-strictly-local--2]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-weil-affine-spectrum`, `def-weil-pbc-localization-at-prime`, `def-weil-spectral-space`, `lem-weil-pbc-affine-scheme-qcqs`, `lem-weil-pbc-qcqs-scheme-spectral`.
