+++
id = "lem-weil-pbc-extension-by-zero-exact"
kind = "lemma"
title = "Extension by zero is exact (étale site)"
uses = ["def-weil-pbc-extension-by-zero"]
lean = ["AlgebraicGeometry.Etale.preservesFiniteLimits_openImmersionLowerShriek", "AlgebraicGeometry.Etale.openImmersionLowerShriekUpperStarAdjunction"]
order = 1733
+++
Let $\Lambda$ be a commutative ring ($\Lambda=\mathbf Z$ gives abelian sheaves), let $j:U\hookrightarrow X$ be an open immersion of schemes and let $j_!:\Mod(U_{\Et},\Lambda)\to\Mod(X_{\Et},\Lambda)$ be extension by zero on the small etale sites [def-weil-pbc-extension-by-zero]. Then $j_!$ is an exact functor of abelian categories: it is additive and carries every short exact sequence $0\to F'\to F\to F''\to0$ of sheaves of $\Lambda$-modules on $U_{\Et}$ to a short exact sequence $0\to j_!F'\to j_!F\to j_!F''\to0$ on $X_{\Et}$. Consequently, applied degreewise, $j_!$ carries complexes to complexes, quasi-isomorphisms to quasi-isomorphisms and acyclic complexes to acyclic complexes.
