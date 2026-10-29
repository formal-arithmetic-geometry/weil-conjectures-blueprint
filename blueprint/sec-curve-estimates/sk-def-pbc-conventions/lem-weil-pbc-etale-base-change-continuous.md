+++
id = "lem-weil-pbc-etale-base-change-continuous"
kind = "lemma"
title = "Base change between small etale sites is continuous; direct image preserves sheaves of sets"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-pc-fibre-product", "def-weil-pbc-etale-sheaf-of-sets", "def-weil-pbc-abelian-etale-sheaves"]
lean = ["AlgebraicGeometry.Scheme.Hom.Etale", "AlgebraicGeometry.Scheme.Hom.coverPreserving_etale", "AlgebraicGeometry.Scheme.Hom.isContinuous_etale", "CategoryTheory.Functor.sheafPushforwardContinuous", "AlgebraicGeometry.Etale.lowerStar_obj_val_obj"]
order = 1387
tags = ["stacks-00WV"]
+++
Let $u:U\to V$ be a morphism of schemes [def-pc-scheme], $V_{\Et}$, $U_{\Et}$ the small etale sites [def-weil-pbc-etale-site] and $b:V_{\Et}\to U_{\Et}$, $W\mapsto U\times_VW$, $(g:W_1\to W_2)\mapsto\mathrm{id}_U\times g$, the base-change functor. Then: (1) $b$ sends coverings to coverings: if $\{W_i\to W\}_{i}$ is a covering of $V_{\Et}$ (etale morphisms over $V$, jointly surjective), then $\{U\times_VW_i\to U\times_VW\}_i$ is a covering of $U_{\Et}$; (2) for a morphism $W'\to W$ and a morphism $W''\to W$ of $V_{\Et}$ the canonical map $U\times_V(W'\times_WW'')\to(U\times_VW')\times_{U\times_VW}(U\times_VW'')$ is an isomorphism; (3) consequently $b$ is a continuous functor of sites (Stacks, Sites, Definition 00WV), and for every sheaf of sets $\mathcal F$ on $U_{\Et}$ the presheaf $u_*\mathcal F=\mathcal F\circ b$, $W\mapsto\mathcal F(U\times_VW)$, is a sheaf of sets on $V_{\Et}$; the sheaf condition of $u_*\mathcal F$ for a covering $\{W_i\to W\}$ is the sheaf condition of $\mathcal F$ for the covering $\{U\times_VW_i\to U\times_VW\}$. The same holds for sheaves of abelian groups and of commutative rings, whose sheaf condition is that of the underlying presheaf of sets.
