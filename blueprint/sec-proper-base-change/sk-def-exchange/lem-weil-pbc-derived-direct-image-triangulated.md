+++
id = "lem-weil-pbc-derived-direct-image-triangulated"
kind = "lemma"
title = "The derived direct image on bounded below derived categories is a triangulated functor"
order = 1055
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-kinjective-resolutions", "def-weil-triangulated-category", "def-weil-pbc-derived-categories"]
lean = ["branch", "declarations", "note"]
tags = ["stacks-05SE"]
+++
Let $v:\mathcal A\to\mathcal B$ be an additive left exact functor between abelian categories, $\mathcal A$ having enough injectives (for example $u_*:\Ab(U_{\Et})\to\Ab(V_{\Et})$ for a morphism of schemes $u:U\to V$ [def-weil-pbc-direct-image], $\Ab(U_{\Et})$ being a Grothendieck abelian category). For $K\in D^+(\mathcal A)$ choose a K-injective resolution $K\to I(K)$ [def-weil-pbc-kinjective-resolutions] (a bounded below complex of injectives quasi-isomorphic to $K$ will do) and set $RvK=v(I(K))\in D^+(\mathcal B)$, on morphisms through the homotopy classes of the induced maps of resolutions. Let $\sigma_K:Rv(K[1 ])\xrightarrow{\sim}(RvK)[1 ]$ be the isomorphism $v(I(K[1 ]))\cong v(I(K)[1 ])=v(I(K))[1 ]$ given by the unique-up-to-homotopy comparison of the two K-injective resolutions $K[1 ]\to I(K[1 ])$ and $K[1 ]\to I(K)[1 ]$. Then $(Rv,\sigma)$ is a triangulated functor $D^+(\mathcal A)\to D^+(\mathcal B)$ [def-weil-triangulated-category]: $\sigma$ is natural in $K$, and for every distinguished triangle $K_1\xrightarrow{a}K_2\xrightarrow{b}K_3\xrightarrow{c}K_1[1 ]$ of $D^+(\mathcal A)$ the triangle $RvK_1\xrightarrow{Rv\,a}RvK_2\xrightarrow{Rv\,b}RvK_3\xrightarrow{\sigma_{K_1}\circ Rv\,c}(RvK_1)[1 ]$ is distinguished in $D^+(\mathcal B)$. In particular $Ru_*:\Dplus(U_{\Et})\to\Dplus(V_{\Et})$ [def-weil-pbc-derived-categories] is triangulated with this shift isomorphism.
