+++
id = "lem-weil-pbc-chow-noetherian"
kind = "lemma"
title = "Chow's lemma over a Noetherian base"
uses = ["def-nagata-projective-space-base-change", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.ChowModification.nonempty_data"]
+++
Let $S$ be a Noetherian scheme and $f:X\to S$ a separated morphism of finite type `AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)), [def-weil-finite-type-morphism]. Then there exist an integer $n\ge0$, a scheme $X'$, a morphism $\pi:X'\to X$ which is proper `AlgebraicGeometry.IsProper` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Proper.lean)) and surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)), and an immersion $X'\to\mathbf P^n_S$ `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) into $\mathbf P^n_S=S\times_{\operatorname{Spec}\mathbf Z}\mathbf P^n_{\mathbf Z}$ [def-nagata-projective-space-base-change] such that the composite $X'\to\mathbf P^n_S\to S$ equals $f\circ\pi$; moreover these can be chosen so that there is a dense open subscheme $U\subseteq X$ with $\pi^{-1}(U)\to U$ an isomorphism.
