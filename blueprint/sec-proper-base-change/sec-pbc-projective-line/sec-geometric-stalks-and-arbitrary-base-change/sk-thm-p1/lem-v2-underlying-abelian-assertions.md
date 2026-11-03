+++
id = "lem-v2-underlying-abelian-assertions"
kind = "lemma"
title = "Curve assertions are invariant under forgetting coefficient scalars"
uses = ["def-constructible-constructible", "def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves"]
lean = ["AlgebraicGeometry.IsCurve.assertions_of_underlying_abelian_iso"]
order = 1949
+++
Let $k$ be a field, $f:X\to\operatorname{Spec}k$ a scheme morphism, and $\Lambda,R$ commutative rings. Let $F$ and $G$ be constructible sheaves of $\Lambda$-modules and $R$-modules respectively on $X_{\mathrm{\acute et}}$ [def-weil-pbc-etale-sheaves], [def-constructible-constructible]. Suppose their underlying abelian sheaves are isomorphic. If the eight conditional assertions $\mathcal C(X,G)$ [def-weil-pbc-eight-curve-assertions] hold, then $\mathcal C(X,F)$ holds. No curve, reducedness, finiteness of the coefficient rings, or algebraic closedness assumption is required.
