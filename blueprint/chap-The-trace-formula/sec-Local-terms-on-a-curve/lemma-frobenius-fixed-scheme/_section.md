+++
id = "lemma-frobenius-fixed-scheme"
kind = "lemma"
title = "The Frobenius fixed scheme"
order = 960
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isProper_hom"]
uses = ["lemma-stability", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-composition-open-restriction-compactifications-f", "definition-correspondence", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For $m\geq1$, the fixed point scheme of $\Phi_X^m$ satisfies

$$
\Fix(\Phi_X^m)
\simeq\coprod_{x\in X_0(\mathbf F_{q^m})}s.
$$

In particular, the fixed scheme is finite, reduced and proper over $k$.
