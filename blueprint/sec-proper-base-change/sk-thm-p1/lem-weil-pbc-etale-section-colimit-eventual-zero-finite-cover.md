+++
id = "lem-weil-pbc-etale-section-colimit-eventual-zero-finite-cover"
kind = "lemma"
title = "Finite-cover filtered equalization for etale sections"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.etale_section_colimit_eventual_zero_of_finite_cover"]
order = 1848
+++
Let $X$ be a scheme, $\Lambda$ a commutative ring, $I$ a small filtered category and $i\mapsto G_i$ a functor from $I$ to sheaves of $\Lambda$-modules on the small étale site $X_{\Et}$ [def-weil-pbc-etale-site]. Let $U$ be an object of $X_{\Et}$, $i\in I$, $s\in G_i(U)$, and let $(q_k:V_k\to U)_{k\in K}$ be a finite family of morphisms of $X_{\Et}$ such that
- (local eventual vanishing) for every $k$ there is a morphism $u:i\to j$ of $I$ with $G(u)(s|_{V_k})=0$ in $G_j(V_k)$, and
- (separatedness) for every $j\in I$, a section $t\in G_j(U)$ with $t|_{V_k}=0$ for all $k$ is zero.

Then there is a morphism $u:i\to j$ of $I$ with $G(u)(s)=0$ in $G_j(U)$.
