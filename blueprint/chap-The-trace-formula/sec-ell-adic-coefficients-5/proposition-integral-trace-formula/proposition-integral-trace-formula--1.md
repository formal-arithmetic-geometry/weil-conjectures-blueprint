+++
id = "proposition-integral-trace-formula--1"
kind = "proposition"
title = "Integral trace formula (1)"
name_showing = false
order = 1010001
aliases = ["bp-r308-1"]
lean = []
uses = ["definition-frobenius-correspondences-their-operators"]
+++
This integral statement is bypassed by the Lean proof of the main theorem.

Let $K\in\Dbc(X,\mathcal O_E)$ and let $\theta:\Phi_X^*K\to K$ be any
morphism, that is, a Frobenius correspondence with integral coefficients. Define its iterates $\theta_m$, the
endomorphisms $T_{c_m}(\theta_m)$ and the stalk maps
$\theta_{m,\bar y}$ by the formulas of Definition [definition-frobenius-correspondences-their-operators]. Then for every $m\geq1$ we have

$$
\operatorname{tr}_{\mathcal O_E}
\bigl(T_{c_m}(\theta_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}
\bigl(\theta_{m,\bar y}\mid K_{\bar y}\bigr),
\tag{12.1}
$$

where both sides are categorical traces of perfect complexes over
$\mathcal O_E$.

The Lean route establishes the trace formula over $\overline{\mathbf Q}_\ell$
for bounded constructible complexes with an invertible Weil structure,
allowing a twisting automorphism of finite order.
The relative formula, `AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction`,
follows by Noetherian induction from the finite étale, closed immersion and
relative affine-line cases. Its specialization to the structure morphism is
`AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula`; taking the twisting
automorphism to be the identity and comparing Weil objects with Weil complexes
gives `AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq`.
These declarations do not state the integral formula for an arbitrary
$\theta:\Phi_X^*K\to K$ displayed above.
