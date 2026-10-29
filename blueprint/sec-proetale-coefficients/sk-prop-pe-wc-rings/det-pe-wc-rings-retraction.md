+++
id = "det-pe-wc-rings-retraction"
kind = "lemma"
title = "Retraction of a faithfully flat ind-étale algebra over a w-contractible ring"
lean = ["IsWContractibleRing.exists_retraction_of_zeroLocus_map_eq_closedPoints", "IsWContractibleRing.exists_retraction", "exists_retraction_of_bijectiveOnStalks", "exists_retraction_of_isClosed_of_bijOn", "Algebra.WeaklyEtale.bijectiveOnStalks", "RingHom.IsWLocal.bijective_of_bijective", "WContractification.Restriction"]
order = 939
uses = ["det-pe-wc-rings-w-local-refinement", "det-pe-wc-rings-local-iso", "det-pe-stonean-projective", "det-pe-wlocal-components", "det-pe-wlocal-strict-contractible", "lem-weil-pbc-ind-etale-stability"]
+++
Let $R$ be w-contractible [det-pe-wlocal-strict-contractible] and let $I\subset R$ be an
ideal with $V(I)=(\operatorname{Spec}R)^c$.

1. Let $R\to S$ be faithfully flat and ind-étale, with $\operatorname{Spec}S$ w-local and
   with closed points exactly the points of $V(IS)$. Then $R\to S$ has an $R$-algebra
   retraction $S\to R$.
2. Every faithfully flat ind-étale ring map $R\to B$ has an $R$-algebra retraction
   $B\to R$: apply 1 to $S=B'$ of [det-pe-wc-rings-w-local-refinement] and compose with
   $B\to B'$.
