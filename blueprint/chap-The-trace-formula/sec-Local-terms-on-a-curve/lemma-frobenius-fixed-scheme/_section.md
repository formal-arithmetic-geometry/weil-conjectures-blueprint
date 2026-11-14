+++
id = "lemma-frobenius-fixed-scheme"
kind = "lemma"
title = "The Frobenius fixed scheme"
order = 960
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isProper_hom"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-correspondence", "definition-frobenius-correspondences-their-operators"]
+++
For $m\geq1$, the fixed point scheme of $\Phi_X^m$ satisfies

$$
\Fix(\Phi_X^m)
\simeq\coprod_{x\in X_0(\mathbf F_{q^m})}s.
$$

In particular, the fixed scheme is finite, reduced and proper over $k$.
