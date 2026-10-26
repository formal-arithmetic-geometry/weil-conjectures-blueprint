+++
id = "lem-weil-pbc-etale-cech-sectionwise-short-exact"
kind = "lemma"
title = "Sectionwise short exactness gives a short exact sequence of etale Cech complexes"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.etale_cech_shortExact_of_sections"]
order = 1703
+++
Let $X$ be a scheme with small étale site $X_{\Et}$ [def-weil-pbc-etale-site], and let $0\to F_1\to F_2\xrightarrow{g}F_3\to0$ be a short exact sequence of abelian sheaves on $X_{\Et}$. Let $U$ be an object of $X_{\Et}$ and $(f_t:V_t\to U)_{t\in T}$ any family of morphisms of $X_{\Et}$, not necessarily a covering. Suppose that for every $p\ge0$ and every tuple $(a_0,\dots,a_p)\in T^{p+1}$ the map $g$ is surjective on sections over the fibre product $V_{a_0}\times_U\cdots\times_UV_{a_p}$. Then applying the Čech complex of the family $(f_t)_{t\in T}$ gives a short exact sequence of cochain complexes of abelian groups
$$0\to\check C^\bullet(\{V_t\to U\},F_1)\to\check C^\bullet(\{V_t\to U\},F_2)\to\check C^\bullet(\{V_t\to U\},F_3)\to0.$$
No injectivity or Čech-acyclicity assumption is needed.
