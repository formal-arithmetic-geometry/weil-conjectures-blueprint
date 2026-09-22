+++
id = "lem-fin-closed-immersion"
kind = "theorem"
title = "Closed immersions preserve constructibility"
order = 5165
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.Etale.IsConstructible.pushforward_of_isClosedImmersion"]
uses = ["lem-fin-finite-morphism"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion with $X$ of finite type
over $k$, and let $G$ be a constructible $\Lambda$-sheaf on $Z_{\Et}$. Then
$i_*G$ is constructible on $X_{\Et}$ and $R^qi_*G=0$ for $q>0$.

## Proof

A closed immersion is affine and induced locally by a surjective ring
homomorphism, so $i_*\mathcal O_Z$ is a finite $\mathcal O_X$-algebra: the
source is a finite module over the target locally, which is the finiteness
condition. Hence $i$ is finite and [lem-fin-finite-morphism] applies.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes
