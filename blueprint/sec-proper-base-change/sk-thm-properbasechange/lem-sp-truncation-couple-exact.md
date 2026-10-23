+++
id = "lem-sp-truncation-couple-exact"
kind = "lemma"
title = "The truncation couple is an exact couple"
order = 1974
lean = ["CategoryTheory.truncation_raw_exact"]
uses = ["def-sp-exact-couple", "def-sp-grothendieck-abelian", "def-sp-left-exact-additive", "def-sp-truncation-couple", "lem-sp-long-exact-of-triangle"]
+++
Let $v:\mathcal A\to\mathcal B$ be left exact and additive
[def-sp-left-exact-additive] between Grothendieck abelian categories
[def-sp-grothendieck-abelian], and let $K\in\operatorname{Ch}^+(\mathcal A)$
be bounded below with $\mathcal H^q(K)=0$ for $q<a$. Then the truncation
couple [def-sp-truncation-couple] of $K$, with the structure maps $\alpha$,
$f$, $g$ of bidegrees $(-1,+1)$, $(+2,-1)$, $(0,0)$ of
[def-sp-truncation-couple], is an exact couple [def-sp-exact-couple].
