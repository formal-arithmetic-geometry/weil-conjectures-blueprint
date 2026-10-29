+++
id = "lem-weil-pbc-disjoint-etale-sections-product"
kind = "lemma"
title = "Sections of a sheaf over a disjoint etale cover"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.Etale.isIso_piLift_of_disjoint"]
order = 1824
+++
Let $X$ be a scheme, $A$ a category, and $G$ an $A$-valued sheaf on its small etale site [def-weil-pbc-etale-site]. Let $V$ be an object of the site, $W_i$ an indexed family of objects, and $\pi_i:W_i\to V$ monomorphisms. Assume that their generated sieve is covering and that the images of the underlying scheme maps $\pi_i$ and $\pi_j$ are disjoint whenever $i\ne j$. If the categorical product of the $G(W_i)$ exists, the restriction map $G(V)\to\prod_iG(W_i)$ is an isomorphism. The index set is arbitrary, including empty.
