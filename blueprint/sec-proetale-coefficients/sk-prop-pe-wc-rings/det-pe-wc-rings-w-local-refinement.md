+++
id = "det-pe-wc-rings-w-local-refinement"
kind = "lemma"
title = "A w-local refinement over the closed points"
uses = ["def-weil-pbc-w-localization", "lem-weil-pbc-w-localization-points", "def-weil-pbc-retained-localization", "lem-weil-pbc-retained-localization", "lem-weil-pbc-ind-etale-stability", "det-pe-wlocal-strict-contractible"]
+++
Let $R$ be w-local [det-pe-wlocal-strict-contractible] and let $R\to B$ be faithfully flat
and ind-étale. There is an ind-Zariski $B$-algebra $B'$ such that

1. $R\to B'$ is ind-étale;
2. $\operatorname{Spec}B'$ is w-local;
3. every closed point of $\operatorname{Spec}B'$ lies over a closed point of
   $\operatorname{Spec}R$, and the induced map
   $(\operatorname{Spec}B')^c\to(\operatorname{Spec}R)^c$ is surjective;
4. every local ring of $B'$ is a local ring of $B$ (via $B\to B'$).
