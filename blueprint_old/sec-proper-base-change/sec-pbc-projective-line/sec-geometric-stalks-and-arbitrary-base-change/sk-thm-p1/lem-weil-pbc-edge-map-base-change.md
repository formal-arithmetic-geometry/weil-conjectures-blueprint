+++
id = "lem-weil-pbc-edge-map-base-change"
kind = "lemma"
title = "The edge map of a direct image commutes with base change"
uses = ["def-weil-pbc-cartesian-square", "lem-weil-pbc-inverse-image-composition", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-underived-exchange", "def-weil-pbc-cohomology-pullback", "def-weil-pbc-inverse-image", "lem-weil-pbc-cohomology-pullback-functorial", "def-weil-pbc-direct-image", "def-sp-kinjective-bridge"]
lean = ["AlgebraicGeometry.Etale.cohomology_edgeMap_baseChange", "AlgebraicGeometry.Etale.bijective_edgeMap_baseChange"]
order = 1960
tags = ["stacks-03SB"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a cartesian square of schemes [def-weil-pbc-cartesian-square], $$X'\xrightarrow{g'}X,\quad f':X'\to Y',\quad f:X\to Y,\quad Y'\xrightarrow{g}Y,\qquad fg'=gf',$$ whose specified isomorphism $\theta_\square:f'^{-1}g^{-1}\xrightarrow{\sim}g'^{-1}f^{-1}$ is $c_{f,g'}^{-1}\circ c_{g,f'}$ for the composition isomorphisms $c$ of [lem-weil-pbc-inverse-image-composition] (with $(g\circ f')^{-1}=(f\circ g')^{-1}$). Let $F$ be an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves] and $\Ex^0_{\square,F}:g^{-1}f_*F\to f'_*g'^{-1}F$ the underived exchange morphism [def-weil-pbc-underived-exchange]. For a morphism $u:S\to T$ and an abelian sheaf $E$ on $S_{\Et}$ write $e^q_{u,E}=H^q(\varepsilon_{u,E})\circ u^*:H^q(T_{\Et},u_*E)\to H^q(S_{\Et},E)$ for the edge map (pullback map $u^*$ of [def-weil-pbc-cohomology-pullback] followed by the map induced by the counit $\varepsilon_u$ of [def-weil-pbc-inverse-image], as in [lem-weil-pbc-cohomology-pullback-functorial]). Then for every $q\ge0$ $$g'^*\circ e^q_{f,F}=e^q_{f',g'^{-1}F}\circ H^q(\Ex^0_{\square,F})\circ g^*:\ H^q(Y_{\Et},f_*F)\longrightarrow H^q(X'_{\Et},g'^{-1}F).$$ No hypothesis on $f$ is needed. In particular, when $f$ (hence $f'$) is finite and $\Ex^0_{\square,F}$ is an isomorphism, $g^*$ on $H^q(Y,f_*F)$ is identified with $g'^*$ on $H^q(X,F)$ through isomorphisms.
