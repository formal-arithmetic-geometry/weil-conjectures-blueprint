+++
id = "lem-zl-geometric-constituents-any-base"
kind = "lemma"
title = "Geometric constituents after a constant extension on any base"
order = 4287
lean = ["Representation.exists_filtration_isIrreducible_restrict"]
uses = ["def-wf-fundamental-representation", "def-wf-weil-group", "lem-mg-normal-restriction-semisimple", "lem-wf-finite-index-restriction-semisimple", "lem-wf-schur-scalar", "lem-wf-weil-group-constant-extension"]
+++
Let $k$ be an algebraically closed field, let $\rho:W\to\operatorname{GL}_k(V)$
be a finite-dimensional representation of a group $W$, let
$\Pi\subseteq W$ be a normal subgroup and $F\in W$. Then there are
$m\geq1$ and a finite chain of subspaces
$0=U_0\subsetneq U_1\subsetneq\cdots\subsetneq U_n=V$, each stable under
$\Pi$ and under $\rho(F^m)$, such that every successive quotient
$U_{i+1}/U_i$ is irreducible under $\Pi$.
