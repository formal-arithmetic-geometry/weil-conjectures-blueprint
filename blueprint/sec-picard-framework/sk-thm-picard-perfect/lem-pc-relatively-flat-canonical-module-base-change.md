+++
id = "lem-pc-relatively-flat-canonical-module-base-change"
kind = "lemma"
title = "Derived base change for a relatively flat module"
order = 777
lean = ["AlgebraicGeometry.exists_isIso_canonicalModuleBaseChange_of_isFlatOver"]
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "lem-pc-rf-base-change-flat-module"]
+++
Let $f:X\to S$ be a quasi-compact and separated morphism of schemes and
$\mathcal G$ a quasi-coherent $\mathcal O_X$-module flat over $S$. For every
cartesian square with bottom arrow $g:T\to S$ ([def-pc-base-change]), with
$f_T:X_T\to T$ and $\mathcal G_T$ the pullback of $\mathcal G$, the
canonical base-change map

$$
Lg^*Rf_*\mathcal G\longrightarrow Rf_{T,*}\mathcal G_T
$$

is an isomorphism in the derived category of $\mathcal O_T$-modules
([def-pc-derived-direct-image], [def-pc-derived-pullback]).
