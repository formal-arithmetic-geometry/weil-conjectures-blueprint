+++
id = "def-weil-pbc-tensor-bicomplex"
kind = "definition"
title = "The unsigned tensor bicomplex and its maps"
lean = ["HomologicalComplex₂.tensorBicomplex", "HomologicalComplex₂.tensorBicomplexMap"]
order = 1770
+++
Let $R$ be a commutative ring and $P,Q$ chain complexes of $R$-modules indexed by $\mathbf N$. The *tensor bicomplex* $A(P,Q)$ has terms $A(p,q)=P_p\otimes_RQ_q$, horizontal differential $d_P\otimes1$ and vertical differential $1\otimes d_Q$ (no signs). The differentials square to zero and commute. For chain maps $a:P\to P'$ and $b:Q\to Q'$, the map $A(a,b):A(P,Q)\to A(P',Q')$ is defined termwise by $a_p\otimes b_q$.
