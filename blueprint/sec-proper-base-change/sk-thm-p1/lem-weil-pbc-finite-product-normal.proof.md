+++
kind = "proof"
of = "lem-weil-pbc-finite-product-normal"
+++
Let $I$ be the finite index set of factors and let $\mathfrak p$ be any prime ideal of $R=\prod_{i\in I}R_i$. Every prime ideal of a finite product of rings is the inverse image of a prime ideal of one factor under the projection: there are an index $i\in I$ and a prime ideal $\mathfrak q\subset R_i$ for which $\mathfrak p=\pi_i^{-1}(\mathfrak q)$. This also deals with $I=\varnothing$: the asserted existence of $i$ contradicts emptiness, so the zero product ring has no primes and the normal-ring condition is vacuous.

For the index and prime just obtained, the coordinate projection $\pi_i$ induces an isomorphism $R_{\mathfrak p}\cong(R_i)_{\mathfrak q}$ (the other factors die after localizing at $\mathfrak p$); this identifies $R_{\mathfrak p}$ with $(R_i)_{\mathfrak q}$ through the map induced by the coordinate projection. The hypothesis that $R_i$ is a normal ring means precisely that $(R_i)_{\mathfrak q}$ is a normal domain.

Being a normal domain is invariant under ring isomorphisms, so the isomorphism of step 2 makes $R_{\mathfrak p}$ a normal domain. Since $\mathfrak p$ was arbitrary, the defining condition holds for $R$.
