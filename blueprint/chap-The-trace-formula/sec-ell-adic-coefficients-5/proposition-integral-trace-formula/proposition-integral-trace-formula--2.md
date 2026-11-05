+++
id = "proposition-integral-trace-formula--2"
kind = "proposition"
title = "Integral trace formula (2)"
name_showing = false
order = 1010002
aliases = ["bp-r308-2"]
lean = []
uses = ["definition-frobenius-correspondences-their-operators", "theorem-trace-formula-frobenius-correspondence"]
+++
This reduction statement is bypassed by the Lean proof of the main theorem.

Let $K\in\Dbc(X,\mathcal O_E)$ and let $\theta:\Phi_X^*K\to K$ be a
Frobenius correspondence, with operators as in
Definition [definition-frobenius-correspondences-their-operators]. Put
$K_n=K\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n$ for $n\geq1$,
and let $\bar\theta_n:\Phi_X^*K_n\to K_n$ be the reduction of $\theta$.
For every $m\geq1$ and $y\in X_0(\mathbf F_{q^m})$, the reductions modulo
$\pi_E^n$ of the categorical traces
of $T_{c_m}(\theta_m)$ on $\RGammac(X_{\mathrm{pro}\acute{e}t},K)$ and of
$\theta_{m,\bar y}$ on $K_{\bar y}$ are the corresponding traces for
$(K_n,\bar\theta_n)$ in
Theorem [theorem-trace-formula-frobenius-correspondence].

On the Lean route, integral reduction occurs in the local calculation on a
smooth curve with model Frobenius: the fibre at a Frobenius fixed point of an
integral supported restriction, for
$\mathcal O_E$-complexes $M,N$ with $M_{\bar x}=0$, has reductions modulo every
$\ell^n$ factoring through vanishing classical supported restrictions. It is
a morphism of perfect complexes, so the Krull intersection argument makes it
zero. This is
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointIntegralSupportedRestriction_hom_eq_zero`,
using `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.exists_reduction_pointIntegralSupportedRestriction`.
It proves vanishing of a supported restriction map and does not identify the
reductions of the global or stalk traces asserted here.
