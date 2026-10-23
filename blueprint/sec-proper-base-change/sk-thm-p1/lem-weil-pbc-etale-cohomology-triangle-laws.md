+++
id = "lem-weil-pbc-etale-cohomology-triangle-laws"
kind = "lemma"
title = "Triangle laws for fixed-base etale cohomology pullback"
uses = ["def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.cohomologyTriangleMap", "AlgebraicGeometry.Etale.cohomologyTriangleMap_laws", "AlgebraicGeometry.Etale.cohomologyTriangleMap_restriction"]
order = 1853
+++
Let $S$ be a scheme, $G$ an abelian sheaf on $S_{\Et}$ and $q\ge0$, with cohomology as in [def-weil-pbc-etale-cohomology]. To every commuting triangle $X\xrightarrow{f}Y\xrightarrow{a}S$ with $b=a\circ f$ assign the homomorphism $H^q(Y,a^{-1}G)\to H^q(X,b^{-1}G)$ obtained by the cohomological pullback $f^*$ [def-weil-pbc-cohomology-pullback] followed by the map induced by the inverse-image composition isomorphism $f^{-1}a^{-1}G\cong b^{-1}G$ [lem-weil-pbc-inverse-image-composition]. Then: (1) the identity triangle ($f=\mathrm{id}_Y$) induces the identity homomorphism; (2) for $X\xrightarrow{f}Y\xrightarrow{g}Z$ over $S$, the map of the composite triangle is the composite of the two triangle maps; (3) the triangle map sends the pullback $a^*x\in H^q(Y,a^{-1}G)$ of a class $x\in H^q(S,G)$ to its pullback $b^*x\in H^q(X,b^{-1}G)$.
