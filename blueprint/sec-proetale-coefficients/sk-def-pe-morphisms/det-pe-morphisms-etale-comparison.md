+++
id = "det-pe-morphisms-etale-comparison"
kind = "lemma"
title = "Étale, affine pro-étale and weakly étale morphisms"
lean = ["AlgebraicGeometry.etale_le_weaklyEtale", "AlgebraicGeometry.proAffineEtale.weaklyEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.WeaklyEtale.etale", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty"]
order = 904
uses = ["def-weil-weakly-etale-morphism", "def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability"]
+++
Let $u\colon U\to X$ be a morphism of schemes.

1. If $u$ is étale, then $u$ is weakly étale [def-weil-weakly-etale-morphism].
2. If $X=\operatorname{Spec}R$ and $u$ is affine pro-étale, i.e. $U=\operatorname{Spec}B$
   with $R\to B$ ind-étale [def-weil-pbc-ind-etale-algebra], then $u$ is weakly étale.
3. If $u$ is weakly étale and locally of finite presentation, then $u$ is étale.
4. $u$ is weakly étale if and only if, for all affine opens $\operatorname{Spec}R\subset X$
   and $\operatorname{Spec}B\subset u^{-1}(\operatorname{Spec}R)$, the ring map $R\to B$ and
   the multiplication $B\otimes_RB\to B$ are flat.
