+++
id = "dag-def-pe-derived-complete"
kind = "dag-definition"
title = "Derived complete complexes and normalized towers"
name_showing = false
order = 208501
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "def-pe-derived-complete"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.IsDerivedComplete", "AlgebraicGeometry.ProEtale.AdicCompletion.derivedReduction", "AlgebraicGeometry.ProEtale.AdicCompletion.derivedStep", "AlgebraicGeometry.ProEtale.AdicCompletion.completionMap", "AlgebraicGeometry.ProEtale.AdicCompletion.reductionComp", "AlgebraicGeometry.ProEtale.AdicCompletion.roos_isDerivedLimit"]
uses = ["dag-sk-def-pe-derived-completion"]
+++
Let $E/\Ql$ be finite, with uniformizer $\pi_E$, let $X$ be a scheme, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and $(\mathcal O_E/\pi_E^n)_X$ be the
integral and finite coefficient sheaves of `det-def-sfb-pulled-back-coefficients`. For
$K\in D(X_{\mathrm{proét}},\mathcal O_E)$ `det-def-sfb-derived-categories` and $n\geq1$ put

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X ,
$$

the derived tensor product of `def-sfb-derived-tensor-modules`, with the transition maps
$K_{n+1}\to K_n$ induced by the reductions $(\mathcal O_E/\pi_E^{n+1})_X\to(\mathcal O_E/\pi_E^n)_X$
and the maps $K\to K_n$ induced by $\mathcal O_{E,X}\to(\mathcal O_E/\pi_E^n)_X$. The complex
$K$ is *derived complete* if the canonical map

$$
K\longrightarrow R\varprojlim_n K_n
$$

to the derived limit `def-weil-derived-limit` of the tower $(K_n)_n$ is an isomorphism; this map is the
canonical completion map of [dag-sk-def-pe-derived-completion].

The canonical transitions satisfy the *derived reduction identities* of [dag-sk-def-pe-derived-completion]

$$
K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq K_n
\qquad(n\geq1).
$$

A compatible tower $(C_n)_{n\geq1}$, with $C_n\in D(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$,
whose transitions induce isomorphisms
$C_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq C_n$
is called *normalized*.

(SHEAF DAG node `def-pe-derived-complete`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.AdicCompletion.IsNormalized`, `AlgebraicGeometry.ProEtale.AdicCompletion.derivedReduction_isNormalized`. Statement dependencies not drawn: `det-def-sfb-pulled-back-coefficients`, `det-def-sfb-derived-categories`, `def-sfb-derived-tensor-modules`, `def-weil-derived-limit`.
