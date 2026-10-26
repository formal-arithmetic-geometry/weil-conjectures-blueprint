+++
id = "lem-weil-pbc-finite-pushforward-cohomology"
kind = "lemma"
title = "Finite direct image does not change etale cohomology (edge map)"
uses = ["def-weil-finite-integral-morphism", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "lem-weil-pbc-cohomology-pullback-functorial"]
lean = ["AlgebraicGeometry.Etale.bijective_edgeMap_of_isFinite"]
order = 1835
tags = ["stacks-03SB"]
+++
Let $f:X\to Y$ be a finite morphism of schemes [def-weil-finite-integral-morphism] and let $F$ be an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves], with direct image $f_*F$ [def-weil-pbc-direct-image] and counit $\varepsilon_{f,F}:f^{-1}f_*F\to F$ of the adjunction $f^{-1}\dashv f_*$ [def-weil-pbc-inverse-image]. For $q\ge0$ define the *edge map* $$e^q_{f,F}=H^q(\varepsilon_{f,F})\circ f^*:\ H^q(Y_{\Et},f_*F)\xrightarrow{\ f^*\ }H^q(X_{\Et},f^{-1}f_*F)\xrightarrow{\ H^q(\varepsilon_{f,F})\ }H^q(X_{\Et},F),$$ where $f^*$ is the pullback map of [def-weil-pbc-cohomology-pullback] and $H^q(\varepsilon_{f,F})$ the map induced on the cohomology groups of [def-weil-pbc-etale-cohomology] by a morphism of sheaves, as in [lem-weil-pbc-cohomology-pullback-functorial]. Then $e^q_{f,F}$ is an isomorphism for every $q\ge0$. (In degree $0$ it is the identity of $\Gamma(Y,f_*F)=F(X\times_YY)=\Gamma(X,F)$.)
