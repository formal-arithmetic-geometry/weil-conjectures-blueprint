+++
id = "lem-weil-pbc-etale-cover-detects-iso"
kind = "lemma"
title = "A morphism of etale sheaves is an isomorphism iff it is one on an etale covering"
uses = ["def-pc-scheme", "def-weil-etale-morphism", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image"]
tags = ["stacks-0EZR"]
+++
Let $T$ be a scheme [def-pc-scheme] and let $(t_i:T_i\to T)_{i\in I}$ be a family of etale morphisms [def-weil-etale-morphism] which is jointly surjective (every point of $T$ lies in the image of some $t_i$). Let $\varphi:G\to H$ be a morphism in the category $\Ab(T_{\Et})$ of abelian sheaves on the small etale site [def-weil-pbc-abelian-etale-sheaves]. Then $\varphi$ is an isomorphism if and only if for every $i$ its inverse image [def-weil-pbc-inverse-image] $t_i^{-1}\varphi:t_i^{-1}G\to t_i^{-1}H$ is an isomorphism in $\Ab(T_{i,\Et})$. (For $I=\emptyset$, $T$ is empty and every morphism of $\Ab(T_{\Et})$ is an isomorphism.)
