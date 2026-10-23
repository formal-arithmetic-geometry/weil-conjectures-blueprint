+++
id = "def-weil-pbc-cohomology-pullback"
kind = "definition"
title = "Pullback map on etale cohomology"
lean = ["AlgebraicGeometry.Etale.cohomologyMap", "AlgebraicGeometry.Etale.derivedCohomologyPullback_eq_derivedUnit"]
order = 1628
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-sp-kinjective-bridge", "prop-weil-pbc-kinjective-resolutions-exist", "prop-weil-pbc-inverse-image-exact", "def-weil-pbc-etale-cohomology", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-inverse-image", "def-weil-abstract-derived-category", "prop-weil-pbc-cohomology-resolution-independent"]
tags = ["stacks-01F7"]
+++
Let $u:Y\to X$ be a morphism of schemes [def-pc-scheme], with small etale sites $X_{\Et}$, $Y_{\Et}$ [def-weil-pbc-etale-site], and let $G$ be an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves]. Let $u_*$ be the direct image, $(u_*F)(W)=F(W\times_XY)$ [def-weil-pbc-direct-image], so that $\Gamma(X,u_*F)=(u_*F)(X)=F(Y)=\Gamma(Y,F)$ for every abelian sheaf $F$ on $Y_{\Et}$, where $\Gamma(T,-)$ is evaluation at the final object $T$ of $T_{\Et}$; let $u^{-1}$ be the inverse image, with unit $\eta_u:\mathrm{id}\to u_*u^{-1}$ of the adjunction $u^{-1}\dashv u_*$ [def-weil-pbc-inverse-image]. Choose a K-injective resolution $G\to I^\bullet$ [def-sp-kinjective-bridge] (one exists; a resolution by a bounded below complex of injective abelian sheaves is one [prop-weil-pbc-kinjective-resolutions-exist]) and a K-injective resolution $u^{-1}I^\bullet\to J^\bullet$ of the termwise inverse image on $Y_{\Et}$. Since $u^{-1}$ is exact [prop-weil-pbc-inverse-image-exact], it commutes with taking cohomology of complexes, so $u^{-1}G\to u^{-1}I^\bullet$ is a quasi-isomorphism and the composite $u^{-1}G\to u^{-1}I^\bullet\to J^\bullet$ is a K-injective resolution of $u^{-1}G$. The *pullback map*

$$
 u^*:H^q(X_{\Et},G)\longrightarrow H^q(Y_{\Et},u^{-1}G)\qquad(q\ge0)
$$

between the cohomology groups of [def-weil-pbc-etale-cohomology] (computed there as $\mathcal H^q(\Gamma(X,I^\bullet))$ and $\mathcal H^q(\Gamma(Y,J^\bullet))$, from the K-injective resolutions $I^\bullet$ and $J^\bullet$) is the map induced in degree $q$ by the morphism of complexes of abelian groups

$$
 \Gamma(X,I^\bullet)\xrightarrow{\ \Gamma(X,\eta_{u,I^\bullet})\ }\Gamma(X,u_*u^{-1}I^\bullet)=\Gamma(Y,u^{-1}I^\bullet)\longrightarrow\Gamma(Y,J^\bullet),
$$

that is, a section $a\in I^r(X)$ goes to the image of $\eta_{u,I^r}(a)\in(u^{-1}I^r)(Y)$ in $J^r(Y)$ ("pull back the section, then compare with the resolution"). For $K\in\Dplus(X_{\Et})$ [def-weil-pbc-derived-categories], represented by a bounded below complex $K^\bullet$, the same recipe, with $K^\bullet\to I^\bullet$ a K-injective resolution, $u^{-1}K^\bullet$ the termwise inverse image representing $u^{-1}K$ [def-weil-pbc-derived-inverse-image] and $u^{-1}I^\bullet\to J^\bullet$ a K-injective resolution, gives a morphism of complexes $\Gamma(X,I^\bullet)\to\Gamma(Y,J^\bullet)$ whose class in $\Dplus(\Ab)$ [def-weil-abstract-derived-category] is $u^*:\RGamma(X_{\Et},K)\to\RGamma(Y_{\Et},u^{-1}K)$, with $\RGamma$ as in [def-weil-pbc-etale-cohomology]. The definition depends on the chosen resolutions only through the canonical identifications of [prop-weil-pbc-cohomology-resolution-independent]. On $\RGamma$, $u^*$ is $\RGamma(X,-)$ applied to the unit $K\to Ru_*u^{-1}K$ of the derived adjunction, followed by the identification $\RGamma(X,Ru_*-)=\RGamma(Y,-)$.
