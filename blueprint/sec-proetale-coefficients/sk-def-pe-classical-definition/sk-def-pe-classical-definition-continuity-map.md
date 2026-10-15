+++
id = "det-pe-classical-definition-continuity-map"
kind = "definition"
title = "The continuity map and classical sheaves, in detail"
uses = ["def-weil-pbc-proetale-site", "def-weil-pbc-ind-etale-basis"]
+++
Let $X$ be a scheme and $F$ a sheaf of sets on $X_{\Proet}$
([def-weil-pbc-proetale-site]).

1. **Presentations.** A *pro-étale affine presentation* is an affine object
   $U$ of $X_{\Proet}$ together with a cofiltered system $(U_i)_{i\in I}$ of
   affine schemes étale over $X$, with transition morphisms
   $u_{ji}\colon U_j\to U_i$ ($j\geq i$) over $X$, and an isomorphism
   $U\cong\varprojlim_iU_i$ of $X$-schemes; write $u_i\colon U\to U_i$ for the
   projections. Each $U_i$ is an object of $X_{\Proet}$ (an étale morphism is
   weakly étale), and the $u_i$, $u_{ji}$ are morphisms of $X_{\Proet}$.
2. **The continuity map.** The restriction maps $F(u_{ji})\colon F(U_i)\to
   F(U_j)$ make $(F(U_i))_i$ a filtered system of sets, and the maps
   $F(u_i)\colon F(U_i)\to F(U)$ are compatible with it because
   $u_{ji}\circ u_j=u_i$. Hence they induce a unique map
   $$
   c_{F,U}\colon\varinjlim_iF(U_i)\longrightarrow F(U),
   $$
   natural in $F$.
3. **Classical sheaves.** $F$ is *classical* if $c_{F,U}$ is bijective for every
   pro-étale affine presentation. If $F$ is a sheaf of $\Lambda_X$-modules,
   the filtered colimit is taken in $\Lambda$-modules; $c_{F,U}$ is then
   $\Lambda$-linear, and $F$ is classical if every $c_{F,U}$ is an isomorphism
   of $\Lambda$-modules.
4. **Complexes.** A complex $K$ of $\Lambda_X$-module sheaves, or an object of
   $D(X_{\Proet},\Lambda)$, is *classical* if every cohomology sheaf
   $H^q(K)$ is classical. This depends only on the isomorphism class of $K$ in
   the derived category.

The objects $U$ admitting such a presentation are the affine ind-étale objects
of [def-weil-pbc-ind-etale-basis].
