+++
id = "def-weil-pbc-derived-inverse-image"
kind = "definition"
title = "Inverse image on bounded below derived categories"
uses = ["def-pc-scheme", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image", "prop-weil-pbc-inverse-image-exact", "lem-sf-exact-functor-derived-triangulated", "def-weil-abstract-derived-category", "lem-weil-pbc-exact-functor-derived-factorization", "def-weil-pbc-derived-categories", "lem-weil-pbc-exact-functor-bounded-below", "lem-weil-pbc-triangulated-functor-restriction", "prop-weil-pbc-inverse-image-modules-exact"]
lean = ["CategoryTheory.Functor.mapDerivedCategory", "CategoryTheory.Functor.mapDerivedCategoryFactors", "CategoryTheory.Functor.mapDerivedCategoryPlus", "CategoryTheory.Functor.mapDerivedCategoryPlusCompatibility", "AlgebraicGeometry.Etale.upperStar"]
order = 1398
tags = ["stacks-0735"]
+++
Let $u:U\to V$ be a morphism of schemes [def-pc-scheme], let $\Ab(T_{\Et})$ denote the category of abelian sheaves on the small etale site of a scheme $T$ [def-weil-pbc-abelian-etale-sheaves], and let $u^{-1}:\Ab(V_{\Et})\to\Ab(U_{\Et})$ be the inverse image [def-weil-pbc-inverse-image], an exact functor [prop-weil-pbc-inverse-image-exact]. Applying $u^{-1}$ termwise to cochain complexes, $K^\bullet\mapsto u^{-1}K^\bullet=(u^{-1}K^r,u^{-1}d^r)_r$, induces a triangulated functor $u^{-1}_D:D(V_{\Et})\to D(U_{\Et})$ [lem-sf-exact-functor-derived-triangulated] together with a natural isomorphism

$$
 \varphi_{K^\bullet}:u^{-1}_D(QK^\bullet)\xrightarrow{\ \sim\ }Q(u^{-1}K^\bullet),
$$

$Q$ denoting the localization functors from cochain complexes to the derived categories [def-weil-abstract-derived-category], compatible with the shift isomorphisms of $u^{-1}_D$ and of $Q$, the shift isomorphism $u^{-1}(K^\bullet[n ])=(u^{-1}K^\bullet)[n ]$ of the termwise functor being the identity in each degree [lem-weil-pbc-exact-functor-derived-factorization]. The functor $u^{-1}_D$ carries $\Dplus(V_{\Et})$ into $\Dplus(U_{\Et})$ [def-weil-pbc-derived-categories], [lem-weil-pbc-exact-functor-bounded-below]. The *inverse image on the bounded below derived categories*

$$
 u^{-1}:\Dplus(V_{\Et})\longrightarrow\Dplus(U_{\Et}),\qquad u^{-1}K=u^{-1}_DK,
$$

is the restriction of $u^{-1}_D$ to these full triangulated subcategories, with the restricted shift isomorphisms; it is a triangulated functor, and its composite with the inclusion $\Dplus(U_{\Et})\subset D(U_{\Et})$ is the composite of the inclusion $\Dplus(V_{\Et})\subset D(V_{\Et})$ with $u^{-1}_D$ [lem-weil-pbc-triangulated-functor-restriction]. No resolution is used: if $K^\bullet$ is a bounded below complex of abelian sheaves on $V_{\Et}$, then $QK^\bullet\in\Dplus(V_{\Et})$, $u^{-1}K^\bullet$ is bounded below, and $\varphi_{K^\bullet}:u^{-1}(QK^\bullet)\xrightarrow{\sim}Q(u^{-1}K^\bullet)$, so the termwise complex $u^{-1}K^\bullet$ represents $u^{-1}(QK^\bullet)$. Following the source this functor is written $u^{-1}$ rather than $Lu^{-1}$. For a commutative ring $R$, the same construction applied to the exact functor $u^{-1}:\Mod(V_{\Et},R)\to\Mod(U_{\Et},R)$ on sheaves of modules over the constant sheaves of rings [prop-weil-pbc-inverse-image-modules-exact] (in place of $u^{-1}$ on abelian sheaves; the three facts cited above are about arbitrary exact functors between abelian categories) defines $u^{-1}:\Dplus(V_{\Et},R)\to\Dplus(U_{\Et},R)$.
