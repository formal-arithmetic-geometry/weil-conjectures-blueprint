+++
kind = "proof"
of = "theorem-verdier-biduality--2"
order = 844005
uses = ["theorem-verdier-biduality--1", "proposition-unbounded-comparison-finite-coefficients", "corollary-finite-tor-amplitude-under-comparison", "proposition-six-operations-change-coefficients", "lemma-reduction-derived-nakayama"]
+++
Set $R=(-)\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\ell$. The étale reading of $RK$ has constructible cohomology and finite Tor amplitude, and the étale reading of $R\omega_X$ is the étale dualizing complex. Apply [theorem-verdier-biduality--1] to these finite coefficients.

The étale reading is fully faithful on the reductions in question and commutes with internal Hom into the reduced dualizing complex. Hence duality is bijective on morphisms between these reductions. The self-adjunction of internal Hom then makes their double-dual maps invertible. This is `AlgebraicGeometry.ProEtale.CondensedRing.isIso_toIhomIhom_integersModPowReductionAmbient_of_etale`.

Reduction commutes with internal Hom and with the symmetry and evaluation maps, by the coefficient comparisons in [proposition-six-operations-change-coefficients]. It therefore identifies invertibility of $R\delta_K$ with that of the double-dual map of $RK$. Derived Nakayama, [lemma-reduction-derived-nakayama], now detects invertibility of $\delta_K$. Lean applies `AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierBiduality_of_isIso_toIhomIhom_reduction` with $n=1$; it does not require a compatible family of biduality isomorphisms for all $n$.
