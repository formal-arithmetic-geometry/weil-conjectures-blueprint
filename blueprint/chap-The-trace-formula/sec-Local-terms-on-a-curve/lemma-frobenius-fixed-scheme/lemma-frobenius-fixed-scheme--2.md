+++
id = "lemma-frobenius-fixed-scheme--2"
kind = "lemma"
title = "Finiteness"
order = 960004
aliases = ["bp-r292-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.IsModelFrobenius.finite_fixedPoint", "AlgebraicGeometry.ProEtale.CondensedRing.instIsFiniteHomSchemeSigmaPointOfFinite", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isFinite_hom"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-correspondence--2", "definition-correspondence--3", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5"]
+++
Let $X_0$ be of finite type over $k_0=\Fq$, let $k$ be an algebraically
closed extension of $k_0$, and let $\Phi_X$ be the model Frobenius on
$X=X_0\times_{k_0}k$. For $m\geq1$, the set $I_m$ of $k$-rational
points fixed by $\Phi_X^m$ is finite.

For any finite set $I$, the structure morphism
$\coprod_{i\in I}\Spec k\to\Spec k$ is finite. In particular, the
coproduct model of $\Fix(\Phi_X^m)$ is finite over $k$.
