+++
id = "lem-weil-pbc-etale-inverse-image-restriction"
kind = "lemma"
title = "Inverse image along an etale morphism is restriction"
uses = ["def-weil-etale-morphism", "def-weil-pbc-etale-site", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image", "def-weil-pbc-direct-image", "def-pc-fibre-product"]
lean = ["AlgebraicGeometry.Etale.localizationRestriction", "AlgebraicGeometry.Etale.upperStarIsoLocalizationRestriction", "AlgebraicGeometry.Etale.localizationRestrictionLowerStarAdjunction", "AlgebraicGeometry.Etale.localizationRestrictionLowerStarAdjunction_unit_app_hom_app", "CategoryTheory.Adjunction.unit_leftAdjointUniq_hom_app"]
order = 1833
tags = ["stacks-03S2"]
+++
Let $j:Y\to X$ be an etale morphism of schemes [def-weil-etale-morphism], with small etale sites [def-weil-pbc-etale-site]. An object $V\to Y$ of $Y_{\Et}$ gives the object $V\to Y\xrightarrow{j}X$ of $X_{\Et}$ (a composite of etale morphisms is etale), and a morphism over $Y$ is a morphism over $X$; write $\iota_j:Y_{\Et}\to X_{\Et}$ for this functor. For an abelian sheaf $G$ on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves] let $G|_Y=G\circ\iota_j$, i.e. $G|_Y(V\to Y)=G(V\to X)$ with the restriction maps of $G$. Let $j^{-1}$, $j_*$ and $\eta_j:\mathrm{id}\to j_*j^{-1}$ be the inverse image, the direct image $(j_*F)(W)=F(W\times_XY)$ and the unit of $j^{-1}\dashv j_*$ [def-weil-pbc-inverse-image], [def-weil-pbc-direct-image]. Then:

1. $G|_Y$ is an abelian sheaf on $Y_{\Et}$, and there is an isomorphism $\rho_G:j^{-1}G\xrightarrow{\sim}G|_Y$ of abelian sheaves on $Y_{\Et}$, natural in $G$.
2. Under $\rho$, the unit is restriction: for every object $W$ of $X_{\Et}$, $\rho_G(W\times_XY)\circ\eta_{j,G}(W):G(W)\to G|_Y(W\times_XY)=G(W\times_XY)$ is the restriction map of $G$ along the projection $W\times_XY\to W$ (a morphism of $X_{\Et}$). In particular, on global sections, $\rho_G(Y)\circ\eta_{j,G}(X):\Gamma(X,G)=G(X)\to G(Y)$ is the restriction of $G$ along $j:Y\to X$, and $\rho_G(Y):\Gamma(Y,j^{-1}G)\xrightarrow{\sim}G(Y)$.
