+++
id = "lem-pc-tensor-dual-invertible"
kind = "lemma"
title = "Invertible modules: duals and tensor products"
lean = ["AlgebraicGeometry.Scheme.Modules.IsInvertible.dual", "AlgebraicGeometry.Scheme.Modules.IsInvertible.tensorObj", "AlgebraicGeometry.Scheme.Modules.isIso_dualEvaluation", "AlgebraicGeometry.Scheme.Modules.nonempty_tensorObj_dual_iso_unit", "AlgebraicGeometry.Scheme.Modules.nonempty_iso_dual_dual", "AlgebraicGeometry.Scheme.Modules.isInvertible_dual_and_isIso_dualEvaluation_and_isIso_bidual", "AlgebraicGeometry.Scheme.Modules.isInvertible_dual_and_nonempty_iso"]
order = 579
uses = ["def-pc-morphism-conventions", "def-pc-scheme", "def-sc-invertible-module"]
+++
Let $X$ be a scheme and let $\mathcal{M},\mathcal{N}$ be
invertible $\mathcal{O}_X$-modules. Then
$\mathcal{M}^\vee=\mathcal{H}om_{\mathcal{O}_X}(\mathcal{M},\mathcal{O}_X)$ is invertible, so is
$\mathcal{M}\otimes_{\mathcal{O}_X}\mathcal{N}$, the canonical evaluation map
$\mathcal{M}\otimes\mathcal{M}^\vee\to\mathcal{O}_X$ is an isomorphism, and
$\mathcal{M}\cong\mathcal{M}^{\vee\vee}$.
