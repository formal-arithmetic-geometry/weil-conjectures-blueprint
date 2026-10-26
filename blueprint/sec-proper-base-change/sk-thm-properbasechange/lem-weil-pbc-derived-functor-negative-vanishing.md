+++
id = "lem-weil-pbc-derived-functor-negative-vanishing"
kind = "lemma"
title = "Right derived functors move to the right"
uses = ["def-sp-left-exact-additive", "def-sp-grothendieck-abelian", "def-sp-kinjective-bridge"]
lean = ["CategoryTheory.Functor.isZero_homologyFunctor_rightDerivedFunctorPlus_obj_of_isGE"]
order = 1985
tags = ["stacks-05TC"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories, $\mathcal A$ with enough injectives (for example $\mathcal A$ Grothendieck abelian [def-sp-grothendieck-abelian]), let $v:\mathcal A\to\mathcal B$ be an additive functor (in the applications left exact additive [def-sp-left-exact-additive]), and let $Rv:D^+(\mathcal A)\to D^+(\mathcal B)$ be its right derived functor, computed on a bounded below complex $L$ by a K-injective resolution $L\to I$, for instance a bounded below complex of injective objects, as $RvL=v(I)$ [def-sp-kinjective-bridge]. Let $b\in\mathbf Z$. If $L\in D^+(\mathcal A)$ satisfies $\mathcal H^i(L)=0$ for all $i<b$, then $\mathcal H^j(RvL)=0$ for all $j<b$. In particular, for an object $X$ of $\mathcal A$ placed in degree $0$, $\mathcal H^j(Rv(X[0 ]))=0$ for all $j<0$.
