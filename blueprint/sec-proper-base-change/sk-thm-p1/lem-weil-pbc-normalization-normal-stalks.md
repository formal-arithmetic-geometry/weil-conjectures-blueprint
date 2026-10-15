+++
id = "lem-weil-pbc-normalization-normal-stalks"
kind = "lemma"
title = "The normalization of a scheme in a normal integral scheme has integrally closed local rings"
uses = ["def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.Hom.isIntegrallyClosed_stalk_normalization"]
+++
Let $f:T\to X$ be a quasi-compact and quasi-separated morphism of schemes [def-weil-pbc-scheme-conventions] with $T$ an integral scheme `AlgebraicGeometry.IsIntegral` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Properties.lean)) all of whose local rings $\mathcal O_{T,t}$ are integrally closed domains, and let $\nu:X'\to X$ be the normalization of $X$ in $T$ as in `AlgebraicGeometry.Scheme.Hom.normalization, Scheme.Hom.toNormalization, Scheme.Hom.fromNormalization, Scheme.Hom.toNormalization_fromNormalization, Scheme.Hom.instIsIntegralHomFromNormalization, the instance IsDominant f.toNormalization (Normalization.lean:341), Scheme.Hom.normalizationObjIso, Scheme.Hom.fromNormalization_app, Scheme.Hom.normalizationObjIso_hom_val, Scheme.Hom.instIsIntegralNormalization, IsAffineHom.isAffine_preimage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Normalization.lean)). Then every local ring $\mathcal O_{X',y}$, $y\in X'$, is an integrally closed domain.
