+++
id = "lem-weil-pbc-finite-fibre-cokernel-tensor"
kind = "lemma"
title = "Residue-field tensor of the affine section-map cokernel vanishes"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.subsingleton_fibreTensor_sectionCokernel"]
source = "literature/stacks-project/etale.tex, Lemma 04DG proof, Nakayama and spreading-out sentences (lines 734-743)"
+++
Let $f:X\to S$ be a finite morphism of schemes [def-pc-scheme] `AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Finite.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Integral.lean)), $U\subseteq S$ an affine open, and $s\in U$. Set $A=\Gamma(U,\mathcal O_S)$, $B=\Gamma(f^{-1}U,\mathcal O_X)$, and let $\varphi:A\to B$ be the section map. Let $\mathfrak p\in\operatorname{Spec}A$ correspond to $s$ `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)). If $X_s\to\operatorname{Spec}\kappa(s)$ is a closed immersion `AlgebraicGeometry.Scheme.Hom.fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Fiber.lean)) `AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean)) `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)), then $\kappa(\mathfrak p)\otimes_A (B/\operatorname{im}\varphi)=0$, where the image is taken as an $A$-submodule.
