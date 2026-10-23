+++
id = "lem-sp-derived-functor-single-identification"
kind = "lemma"
title = "The derived functor on an object placed in degree 0 computes the classical right derived functors"
uses = ["def-sp-left-exact-additive", "def-sp-grothendieck-abelian", "def-sp-kinjective-bridge", "def-sp-injective-resolutions", "def-weil-pbc-bounded-derived-subcategories"]
lean = ["CategoryTheory.Functor.homologyRightDerivedFunctorPlusObjSingleFunctorIso", "CategoryTheory.Functor.singleFunctorCompRightDerivedFunctorPlusCompHomologyFunctorIso"]
order = 1996
tags = ["stacks-015A"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories, $\mathcal A$ with enough injectives (for example $\mathcal A$ Grothendieck abelian [def-sp-grothendieck-abelian]), let $v:\mathcal A\to\mathcal B$ be an additive functor (in the application left exact additive [def-sp-left-exact-additive]), and let $Rv:D^+(\mathcal A)\to D^+(\mathcal B)$ [def-weil-pbc-bounded-derived-subcategories] be its right derived functor, computed on a bounded below complex $L$ by a K-injective resolution $L\to I(L)$, for instance a bounded below complex of injective objects, as $RvL=v(I(L))$ [def-sp-kinjective-bridge]. For an object $X$ of $\mathcal A$ let $X[0 ]$ be the complex with $X$ in degree $0$, and let $R^pv(X)=\mathcal H^p(v(I^\bullet))$, $p\ge0$, be the right derived functors defined by an injective resolution $X\to I^\bullet$ [def-sp-left-exact-additive], [def-sp-injective-resolutions]. Then for every $p\geq0$ there is an isomorphism

$$
 \theta^p_X:\ \mathcal H^p\bigl(Rv(X[0 ])\bigr)\xrightarrow{\ \sim\ }R^pv(X),
$$

natural in $X\in\mathcal A$: it is induced by the isomorphism $Rv(X[0 ])\cong v(I^\bullet)$ in $D^+(\mathcal B)$ coming from the fact that the injective resolution $X[0 ]\to I^\bullet$ is a K-injective resolution, and for a morphism $f:X\to Y$ both sides are functorial through a lift of $f$ to the injective resolutions, which is unique up to homotopy.
