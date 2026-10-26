+++
id = "lem-weil-pbc-higher-direct-image-sheafified-presheaf"
kind = "lemma"
title = "Higher direct images as sheafified cohomology presheaves"
uses = ["def-pc-scheme", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "def-weil-pbc-direct-image", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.higherDirectImageSheafifiedPresheaf"]
order = 1807
+++
Let $p:X\to S$ be any morphism of schemes [def-pc-scheme] and let $F\in\Ab(X_{\Et})$ be an abelian sheaf on the small etale site [def-weil-pbc-etale-site] of $X$. For an object $U$ of $X_{\Et}$ write $H^q(U,F)$ for the $q$-th right derived functor, evaluated at $F$, of the left exact functor $\Ab(X_{\Et})\to\Ab$, $G\mapsto G(U)$ [def-sp-left-exact-additive] (computed from an injective resolution of $F$ in $\Ab(X_{\Et})$ [def-sp-injective-resolutions]). For an etale $V\to S$ the base change $X\times_SV\to X$ is etale, hence an object of $X_{\Et}$, and a morphism $g:V'\to V$ of $S_{\Et}$ gives the morphism $\mathrm{id}_X\times g:X\times_SV'\to X\times_SV$ of $X_{\Et}$; the restriction map $H^q(X\times_SV,F)\to H^q(X\times_SV',F)$ is the map induced on $H^q$ by the restriction maps $I^\bullet(X\times_SV)\to I^\bullet(X\times_SV')$ of an injective resolution $F\to I^\bullet$. Then for every $q\geq0$ the higher direct image $R^qp_*F=\mathcal H^q(Rp_*F)$ of [def-weil-pbc-direct-image] is canonically isomorphic to the sheafification of the presheaf on $S_{\Et}$

$$
 V\longmapsto H^q(X\times_SV,F).
$$

No hypothesis (quasi-compactness, separatedness) is put on $p$.
