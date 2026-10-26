+++
id = "lem-weil-pbc-inverse-image-composition"
kind = "lemma"
title = "Inverse images along a composite: the canonical isomorphism compatible with the units"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-pc-fibre-product"]
lean = ["AlgebraicGeometry.Etale.lowerStarComp", "AlgebraicGeometry.Etale.lowerStarComp_hom_app_hom_app", "AlgebraicGeometry.Etale.upperStarComp", "AlgebraicGeometry.Etale.conjugateIsoEquiv_upperStarComp", "AlgebraicGeometry.Etale.upperStarComp_hom_app_unit_app", "AlgebraicGeometry.Etale.lowerStarId", "AlgebraicGeometry.Etale.upperStarId", "AlgebraicGeometry.Etale.upperStarId_hom_app_unit_app"]
order = 1824
tags = ["stacks-03CB"]
+++
Let $u:Y\to X$ and $v:Z\to Y$ be morphisms of schemes [def-pc-scheme], with small etale sites [def-weil-pbc-etale-site], categories of abelian sheaves $\Ab(-_{\Et})$ [def-weil-pbc-abelian-etale-sheaves], direct images $u_*,v_*,(u\circ v)_*$ given by $(u_*F)(W)=F(W\times_XY)$ [def-weil-pbc-direct-image], and inverse images $u^{-1},v^{-1},(u\circ v)^{-1}$ with the units $\eta_u,\eta_v,\eta_{u\circ v}$ of the adjunctions $u^{-1}\dashv u_*$, $v^{-1}\dashv v_*$, $(u\circ v)^{-1}\dashv(u\circ v)_*$ [def-weil-pbc-inverse-image].

1. For an abelian sheaf $F$ on $Z_{\Et}$ and an object $W$ of $X_{\Et}$, the canonical isomorphism of $Z$-schemes $(W\times_XY)\times_YZ\xrightarrow{\sim}W\times_XZ$ [def-pc-fibre-product] induces isomorphisms $d_{u,v,F}(W):((u\circ v)_*F)(W)=F(W\times_XZ)\to F((W\times_XY)\times_YZ)=(u_*v_*F)(W)$, compatible with the restriction maps in $W$ and natural in $F$; they form an isomorphism of functors $d_{u,v}:(u\circ v)_*\xrightarrow{\sim}u_*\circ v_*$.
2. There is a unique isomorphism of functors $c_{u,v}:v^{-1}\circ u^{-1}\xrightarrow{\sim}(u\circ v)^{-1}$ from $\Ab(X_{\Et})$ to $\Ab(Z_{\Et})$ such that for every abelian sheaf $G$ on $X_{\Et}$
$$
 u_*v_*(c_{u,v,G})\circ u_*(\eta_{v,u^{-1}G})\circ\eta_{u,G}=d_{u,v,(u\circ v)^{-1}G}\circ\eta_{u\circ v,G}:\ G\longrightarrow u_*v_*(u\circ v)^{-1}G,
$$
that is, $c_{u,v}$ carries the unit $u_*\eta_vu^{-1}\circ\eta_u$ of the composite adjunction $v^{-1}u^{-1}\dashv u_*v_*$ to the unit of $(u\circ v)^{-1}\dashv(u\circ v)_*$, transported along $d_{u,v}$.
3. For $u=\mathrm{id}_X$, the isomorphisms $W\times_XX\xrightarrow{\sim}W$ give an isomorphism $d_X:(\mathrm{id}_X)_*\xrightarrow{\sim}\mathrm{id}$ as in (1), and there is a unique isomorphism of functors $e_X:\mathrm{id}_X^{-1}\xrightarrow{\sim}\mathrm{id}_{\Ab(X_{\Et})}$ with $e_{X,G}\circ d_{X,\mathrm{id}_X^{-1}G}\circ\eta_{\mathrm{id}_X,G}=\mathrm{id}_G$ for every $G$.

The same statements (1)-(3), with the same characterizations of $d_{u,v}$, $c_{u,v}$, $d_X$ and $e_X$, hold for sheaves of $\Lambda$-modules on the small etale sites, $\Lambda$ a commutative ring, with $\Ab(-_{\Et})$ replaced by the category of sheaves of $\Lambda$-modules and with the inverse and direct images and adjunction units of sheaves of $\Lambda$-modules.
