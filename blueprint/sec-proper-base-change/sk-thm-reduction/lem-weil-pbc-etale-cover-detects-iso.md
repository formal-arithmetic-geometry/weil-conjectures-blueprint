+++
id = "lem-weil-pbc-etale-cover-detects-iso"
kind = "lemma"
title = "A morphism of etale sheaves is an isomorphism iff it is one on a jointly surjective family"
lean = ["AlgebraicGeometry.Etale.isIso_iff_forall_isIso_upperStar_map_of_jointlySurjective"]
order = 1943
uses = ["def-pc-scheme", "def-weil-etale-morphism", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image"]
tags = ["stacks-0EZR"]
+++
Let $T$ be a scheme [def-pc-scheme] and let $(t_i:T_i\to T)_{i\in I}$ be a family of morphisms of schemes which is jointly surjective (every point of $T$ lies in the image of some $t_i$), for instance an etale covering [def-weil-etale-morphism]. Let $\varphi:G\to H$ be a morphism of abelian sheaves on the small etale site of $T$ [def-weil-pbc-abelian-etale-sheaves] (more generally of sheaves of $\Lambda$-modules, or of sheaves with values in a concrete Grothendieck abelian category whose forgetful functor reflects isomorphisms, preserves filtered colimits and is compatible with the sheaf condition). Then $\varphi$ is an isomorphism if and only if for every $i$ its inverse image [def-weil-pbc-inverse-image] $t_i^{-1}\varphi:t_i^{-1}G\to t_i^{-1}H$ is an isomorphism. (For $I=\emptyset$, $T$ is empty and every morphism is an isomorphism.)
