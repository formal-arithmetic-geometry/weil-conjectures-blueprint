+++
id = "lem-weil-pbc-exact-functor-bounded-below"
kind = "lemma"
title = "Exact functors preserve bounded below derived objects"
uses = ["def-weil-abstract-derived-category", "lem-sf-exact-functor-derived-triangulated", "def-weil-pbc-bounded-derived-subcategories"]
lean = ["CategoryTheory.Functor.mapDerivedCategoryHomologyFunctorIso", "CategoryTheory.Functor.mapDerivedCategoryHomologyFunctorIso_hom_app_Q", "CategoryTheory.Functor.isGE_mapDerivedCategory_obj", "CategoryTheory.Functor.isLE_mapDerivedCategory_obj", "CategoryTheory.Functor.bounded_mapDerivedCategory_obj", "CategoryTheory.Functor.mapDerivedCategoryPlus"]
order = 1276
tags = ["stacks-015F"]
+++
Let $F:\mathcal A\to\mathcal B$ be an exact functor between abelian categories, and let $F:D(\mathcal A)\to D(\mathcal B)$ also denote the functor between the derived categories [def-weil-abstract-derived-category] induced by applying $F$ termwise to cochain complexes [lem-sf-exact-functor-derived-triangulated]. For every $K\in D(\mathcal A)$ and every $r\in\mathbf Z$ there is an isomorphism $H^r(FK)\cong F(H^rK)$, natural in $K$; when $K=Q(X)$ for a complex $X$, it is the composite $H^r(F(QX))\cong H^r(Q(FX))\cong H^r(FX)\cong F(H^rX)\cong F(H^r(QX))$ of the isomorphism $F\circ Q\cong Q\circ F$, the isomorphisms $H^r\circ Q\cong H^r$ of $D(\mathcal A)$ and $D(\mathcal B)$, and the isomorphism of complexes $H^r(FX)\cong F(H^rX)$ induced by $\ker F(d^r)=F(\ker d^r)$, $\operatorname{im}F(d^{r-1})=F(\operatorname{im}d^{r-1})$ (so the isomorphism is computed termwise on any representing complex). Consequently, for every $n\in\mathbf Z$, $F$ carries $D(\mathcal A)^{\ge n}$ (the $K$ with $H^r(K)=0$ for $r<n$) into $D(\mathcal B)^{\ge n}$, hence carries the bounded below derived category $D^+(\mathcal A)$ into $D^+(\mathcal B)$ [def-weil-pbc-bounded-derived-subcategories] (and likewise $D^-$ and $D^b$).
