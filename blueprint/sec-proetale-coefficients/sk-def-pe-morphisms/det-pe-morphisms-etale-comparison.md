+++
id = "det-pe-morphisms-etale-comparison"
kind = "lemma"
title = "Étale, affine pro-étale and weakly étale morphisms"
uses = ["def-weil-weakly-etale-morphism", "def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability"]
+++
Let $u\colon U\to X$ be a morphism of schemes.

1. If $u$ is étale, then $u$ is weakly étale [def-weil-weakly-etale-morphism].
2. If $X=\operatorname{Spec}R$ and $u$ is affine pro-étale, i.e. $U=\operatorname{Spec}B$
   with $R\to B$ ind-étale [def-weil-pbc-ind-etale-algebra], then $u$ is weakly étale.
3. If $u$ is weakly étale and locally of finite presentation, then $u$ is étale.
4. On affine charts $U\supset\operatorname{Spec}B\to\operatorname{Spec}R\subset X$, $u$ is
   weakly étale if and only if $R\to B$ and the multiplication $B\otimes_RB\to B$ are flat.
