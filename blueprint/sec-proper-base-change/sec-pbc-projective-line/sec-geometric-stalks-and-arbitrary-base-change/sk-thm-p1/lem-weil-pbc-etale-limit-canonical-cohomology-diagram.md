+++
id = "lem-weil-pbc-etale-limit-canonical-cohomology-diagram"
kind = "lemma"
title = "Cohomology of a compatible system of inverse images on a cone"
uses = ["def-pc-scheme", "def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.etale_limit_canonical_cohomology_diagram"]
order = 1956
+++
Let $I$ be a nonempty directed preorder, $D:I^{\mathrm{op}}\to\mathrm{Sch}$ an arbitrary inverse system of schemes [def-pc-scheme], with transition morphisms $D_{ji}:D_j\to D_i$ for $i\le j$, and $(S,(f_i:S\to D_i)_{i\in I})$ any cone over $D$. Let $F_i$ be abelian sheaves on $(D_i)_{\Et}$ and $\varphi_{ij}:D_{ji}^{-1}F_i\to F_j$ ($i\le j$) morphisms such that $\varphi_{ii}$ is the canonical identification $\mathrm{id}^{-1}F_i\cong F_i$ and $\varphi_{ik}=\varphi_{jk}\circ D_{kj}^{-1}(\varphi_{ij})\circ c$ for $i\le j\le k$, where $c:D_{ki}^{-1}F_i\cong D_{kj}^{-1}D_{ji}^{-1}F_i$ is the composition isomorphism of inverse images [def-weil-pbc-inverse-image]. Let $G:I\to\mathrm{Ab}(S_{\Et})$ be a functor with isomorphisms $e_i:G_i\cong f_i^{-1}F_i$ such that, under $e_i$ and $e_j$, the transition map $G_i\to G_j$ is the composition isomorphism $f_i^{-1}F_i\cong f_j^{-1}D_{ji}^{-1}F_i$ followed by $f_j^{-1}(\varphi_{ij})$. Let $(L,(\lambda_i:G_i\to L)_{i\in I})$ be any cocone over $G$, not necessarily a colimit. Then for each $n\ge0$ there are
- a functor $H:I\to\mathrm{Ab}$ with isomorphisms $\epsilon_i:H_i\cong H^n(D_i,F_i)$ [def-weil-pbc-etale-cohomology] under which the transition map $H_i\to H_j$ is $H^n(\varphi_{ij})\circ D_{ji}^*$, with $D_{ji}^*$ the cohomological pullback [def-weil-pbc-cohomology-pullback];
- a cocone $(B,(\beta_i)_{i\in I})$ over $H$ and an isomorphism $\epsilon:B\cong H^n(S,L)$ such that $\epsilon\circ\beta_i=H^n(\lambda_i\circ e_i^{-1})\circ f_i^*\circ\epsilon_i$ for every $i$.

No limit property of $S$, no qcqs condition, no affineness of transition maps, and no exactness or connecting morphism is assumed or asserted.
