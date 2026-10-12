+++
id = "prop-weil-pbc-derived-inverse-image-adjunction"
kind = "proposition"
title = "Derived adjunction of inverse and direct image on D^+"
uses = ["def-pc-scheme", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image", "def-weil-pbc-derived-inverse-image", "def-weil-pbc-direct-image", "def-weil-pbc-kinjective-resolutions", "lem-weil-pbc-derived-direct-image-triangulated", "def-weil-pbc-derived-categories"]
lean = ["branch", "declarations", "note"]
tags = ["sheaf-dag", "stacks-0DVC"]
+++
Let $u:U\to V$ be a morphism of schemes [def-pc-scheme], with the adjunction $u^{-1}\dashv u_*$ on the abelian sheaves on the small etale sites [def-weil-pbc-abelian-etale-sheaves], unit $\eta_u$ and counit $\varepsilon_u$ [def-weil-pbc-inverse-image], the inverse image $u^{-1}:\Dplus(V_{\Et})\to\Dplus(U_{\Et})$ on bounded below derived categories [def-weil-pbc-derived-inverse-image] and the derived direct image $Ru_*:\Dplus(U_{\Et})\to\Dplus(V_{\Et})$, $Ru_*K=u_*I(K)$ for a K-injective resolution $K\to I(K)$ [def-weil-pbc-direct-image], [def-weil-pbc-kinjective-resolutions], on morphisms through the homotopy classes of the induced maps of resolutions [lem-weil-pbc-derived-direct-image-triangulated]. Then $u^{-1}\dashv Ru_*$: there is an adjunction, with unit $\eta^D_u:\mathrm{id}\to Ru_*u^{-1}$ and counit $\varepsilon^D_u:u^{-1}Ru_*\to\mathrm{id}$, uniquely determined by the following two properties.
(1) For a bounded below K-injective complex $I$ of sheaves on $U_{\Et}$ (so that $u_*I$ represents $Ru_*I$), the counit $\varepsilon^D_{u,I}:u^{-1}u_*I\to I$ is the class in $\Dplus(U_{\Et})$ of the morphism of complexes $(\varepsilon_{u,I^r})_r$.
(2) For a bounded below complex $M$ of sheaves on $V_{\Et}$ and a K-injective resolution $u^{-1}M\to J$, the unit $\eta^D_{u,M}:M\to Ru_*u^{-1}M=u_*J$ is the class of $M\xrightarrow{(\eta_{u,M^r})_r}u_*u^{-1}M\to u_*J$.
Equivalently, $\operatorname{Hom}_{\Dplus(U_{\Et})}(u^{-1}M,K)\cong\operatorname{Hom}_{\Dplus(V_{\Et})}(M,Ru_*K)$ bifunctorially, by the bijection sending $a$ to $Ru_*(a)\circ\eta^D_{u,M}$.
