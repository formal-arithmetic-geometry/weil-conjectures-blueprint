+++
id = "lem-pc-rf-base-change-flat-module"
kind = "lemma"
title = "Derived base change for a relatively flat module"
order = 671
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "lem-pc-cech-resolution", "lem-pc-flat-complex-derived-pullback"]
+++
Let $f:X\to S$ be a quasi-compact separated morphism of schemes,
and let $\mathcal G$ be a quasi-coherent $\mathcal O_X$-module flat
over $S$. For every $g:T\to S$, derived pullback gives an isomorphism

$$
Lg^*Rf_*\mathcal G\;\cong\;Rf_{T,*}\mathcal G_T.
$$
