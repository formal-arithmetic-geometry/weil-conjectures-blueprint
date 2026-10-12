+++
id = "lem-weil-pbc-derived-functor-negative-vanishing"
kind = "lemma"
title = "Right derived functors move to the right"
uses = ["def-sp-left-exact-additive", "def-sp-grothendieck-abelian", "def-sp-kinjective-bridge"]
lean = ["branch", "declarations", "note"]
tags = ["sheaf-dag", "stacks-05TC"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor [def-sp-left-exact-additive] between Grothendieck abelian categories [def-sp-grothendieck-abelian], and let $Rv:D^+(\mathcal A)\to D^+(\mathcal B)$ be its right derived functor, computed on a bounded below complex $L$ by a K-injective resolution $L\to I$ as $RvL=v(I)$ [def-sp-kinjective-bridge]. Let $b\in\mathbf Z$. If $L\in D^+(\mathcal A)$ satisfies $\mathcal H^i(L)=0$ for all $i<b$, then $\mathcal H^j(RvL)=0$ for all $j<b$. In particular, for an object $X$ of $\mathcal A$ placed in degree $0$, $R^jv(X)=\mathcal H^j(RvX)=0$ for all $j<0$.
