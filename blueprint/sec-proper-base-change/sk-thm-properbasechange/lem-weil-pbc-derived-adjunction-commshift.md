+++
id = "lem-weil-pbc-derived-adjunction-commshift"
kind = "lemma"
title = "The unit and counit of the derived adjunction u^{-1} -| Ru_* commute with the shift isomorphisms"
lean = ["AlgebraicGeometry.Etale.derivedPlus_upperStarLowerStar_commShift"]
order = 2126
uses = ["def-pc-scheme", "def-weil-pbc-derived-inverse-image", "def-weil-pbc-direct-image", "def-weil-pbc-derived-categories", "prop-weil-pbc-derived-inverse-image-adjunction", "lem-weil-pbc-derived-direct-image-triangulated", "def-sp-kinjective-bridge", "lem-weil-pbc-triangulated-functor-composite"]
tags = ["stacks-0A8D"]
+++
Let $u:U\to V$ be a morphism of schemes [def-pc-scheme] and let $u^{-1}\dashv Ru_*$ be the adjunction between $u^{-1}:\Dplus(V_{\Et})\to\Dplus(U_{\Et})$ [def-weil-pbc-derived-inverse-image] and $Ru_*:\Dplus(U_{\Et})\to\Dplus(V_{\Et})$ [def-weil-pbc-direct-image] on the bounded below derived categories [def-weil-pbc-derived-categories], with unit $\eta^D_u:\mathrm{id}\to Ru_*u^{-1}$ and counit $\varepsilon^D_u:u^{-1}Ru_*\to\mathrm{id}$ [prop-weil-pbc-derived-inverse-image-adjunction]. Write $[1 ]$ for the shift, $(M[1 ])^r=M^{r+1}$, $d_{M[1 ]}=-d_M$. Give $u^{-1}$ the shift-commutation isomorphism $\iota_M:u^{-1}(M[1 ])\xrightarrow{\sim}(u^{-1}M)[1 ]$ which on a representing complex is the identity of the termwise shifted complex $u^{-1}(M^\bullet[1 ])=(u^{-1}M^\bullet)[1 ]$ [def-weil-pbc-derived-inverse-image], and give $Ru_*$ the shift-commutation isomorphism $\sigma_K:Ru_*(K[1 ])\xrightarrow{\sim}(Ru_*K)[1 ]$ obtained by comparing the K-injective resolutions $K[1 ]\to I(K[1 ])$ and $K[1 ]\to I(K)[1 ]$ [lem-weil-pbc-derived-direct-image-triangulated], [def-sp-kinjective-bridge]. Then for every $K\in\Dplus(U_{\Et})$ and every $M\in\Dplus(V_{\Et})$:

(a) (counit) $\varepsilon^D_{u,K[1 ]}=\varepsilon^D_{u,K}[1 ]\circ\iota_{Ru_*K}\circ u^{-1}(\sigma_K)$ as morphisms $u^{-1}Ru_*(K[1 ])\to K[1 ]$;

(b) (unit) $\sigma_{u^{-1}M}\circ Ru_*(\iota_M)\circ\eta^D_{u,M[1 ]}=\eta^D_{u,M}[1 ]$ as morphisms $M[1 ]\to(Ru_*u^{-1}M)[1 ]$.

That is, $\eta^D_u$ and $\varepsilon^D_u$ commute with the shift-commutation isomorphisms of the composite functors $Ru_*u^{-1}$ and $u^{-1}Ru_*$ (composites as in [lem-weil-pbc-triangulated-functor-composite]) and with the identity of $\mathrm{id}$, so that $u^{-1}\dashv Ru_*$ is an adjunction of triangulated functors; by iteration the same holds for the iterated isomorphisms $\iota^{(n)},\sigma^{(n)}$, $n\in\mathbf Z$.
