+++
id = "dag-def-weil-integral-reduction-tower"
kind = "dag-definition"
title = "Derived reduction tower over pulled-back integral coefficients"
name_showing = false
order = 208502
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "def-weil-integral-reduction-tower"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.integralQuotient", "AlgebraicGeometry.ProEtale.integralQuotientRingObj", "AlgebraicGeometry.ProEtale.integralReductionRingMap", "AlgebraicGeometry.ProEtale.integralReductionCoefficientMap"]
+++
Let $E/\mathbf Q_\ell$ be a finite extension, with valuation ring $\mathcal O_E$ and uniformizer $\pi_E$, and let $X$ be a scheme. Put
$$
R=\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E},\qquad
B_n=(\mathcal O_E/\pi_E^n)_X=p_X^*\underline{\mathcal O_E/\pi_E^n}\quad(n\geq1)
$$
as in `det-def-sfb-pulled-back-coefficients`. Write $a_n:R\to B_n$ and $\rho_n:B_{n+1}\to B_n$ for the pulled-back quotient maps. Regard $B_n$ as an $R$-module object via $a_n$ `det-def-sfb-module-objects`, and set
$$
\mathcal D=D(\Mod_R(\Sh(X_{\mathrm{pro\acute et}},\Ab)))=D(X_{\mathrm{pro\acute et}},\mathcal O_E)
$$
with the unbounded convention of `det-def-sfb-derived-categories`. For an $R$-module object $M$, write $M[0]$ for its complex concentrated in degree zero, viewed in $\mathcal D$.

For $K\in\mathcal D$, let $T_K=K\otimes_R^{\mathbf L}-:\mathcal D\to\mathcal D$ be the derived tensor functor `def-sfb-derived-tensor-modules`, and let $r_K:K\otimes_R^{\mathbf L}R[0]\xrightarrow{\sim}K$ be its right unit constraint. Define
$$
K_n=T_K(B_n[0]),\qquad
 t_n=T_K(\rho_n[0]):K_{n+1}\longrightarrow K_n,\qquad
 c_n=T_K(a_n[0])\circ r_K^{-1}:K\longrightarrow K_n.
$$
The *derived reduction tower* of $K$ is the inverse system $(K_n,t_n)_{n\geq1}$ in $\mathcal D$ `def-weil-inverse-system`, with its compatible maps $c_n$ from $K$: $t_n\circ c_{n+1}=c_n$ for every $n\geq1$. For $m>n$ its map $K_m\to K_n$ is $t_n\circ\cdots\circ t_{m-1}$, and for $m=n$ it is the identity.

(SHEAF DAG node `def-weil-integral-reduction-tower`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: definition. Placed through `def-pe-derived-complete` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.integralReductionTransitionRingMap`, `AlgebraicGeometry.ProEtale.integralReductionCoefficientTransition`, `AlgebraicGeometry.ProEtale.integralReductionModule`, `AlgebraicGeometry.ProEtale.integralReductionTensor`, `AlgebraicGeometry.ProEtale.integralReductionLevel`, `AlgebraicGeometry.ProEtale.integralReductionModuleTransition_exists`, `AlgebraicGeometry.ProEtale.integralReductionModuleTransition`, `AlgebraicGeometry.ProEtale.integralReductionModuleTransition_hom`, `AlgebraicGeometry.ProEtale.integralReductionTransition`, `AlgebraicGeometry.ProEtale.integralReductionAugmentation`, `AlgebraicGeometry.ProEtale.integralReductionTower`, `AlgebraicGeometry.ProEtale.integralReductionAugmentation_compatibility`. Statement dependencies not drawn: `det-def-sfb-pulled-back-coefficients`, `det-def-sfb-module-objects`, `det-def-sfb-derived-categories`, `def-sfb-derived-tensor-modules`, `def-weil-inverse-system`.
