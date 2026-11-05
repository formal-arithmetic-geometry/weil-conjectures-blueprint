+++
id = "lemma-frobenius-fixed-scheme"
kind = "lemma"
title = "The Frobenius fixed scheme"
order = 959
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.nonempty_isLimit_fixedPointsFork", "AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.fixedPointEquiv", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isoSigmaPointFixedFieldPoints", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isFinite_hom", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isReduced", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isProper_hom"]
uses = ["definition-correspondence", "definition-frobenius-correspondences-their-operators"]
+++
For $m\geq1$, the fixed point scheme of $\Phi_X^m$ satisfies

$$
\Fix(\Phi_X^m)
\simeq\coprod_{x\in X_0(\mathbf F_{q^m})}s.
$$

In particular, the fixed scheme is finite, reduced and proper over $k$.
