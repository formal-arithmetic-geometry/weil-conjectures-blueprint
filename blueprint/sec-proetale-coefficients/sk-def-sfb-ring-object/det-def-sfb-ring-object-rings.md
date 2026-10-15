+++
id = "det-def-sfb-ring-object-rings"
kind = "lemma"
title = "Rings are ring objects of $\\Ab$"
uses = ["det-def-sfb-ring-object-monoid"]
+++
Give $\Ab$ the monoidal structure $\otimes_{\mathbf Z}$ with unit $\mathbf Z$ and its usual
associator, unitors and symmetry $a\otimes b\mapsto b\otimes a$. For a ring $R$ let
$\eta_R\colon\mathbf Z\to R$, $n\mapsto n\cdot1$, and let
$\mu_R\colon R\otimes_{\mathbf Z}R\to R$ be the map with $a\otimes b\mapsto ab$. Then:

1. $(R,\mu_R,\eta_R)$ is a ring object of $\Ab$ ([det-def-sfb-ring-object-monoid]);
2. every ring homomorphism $f\colon R\to R'$ is a morphism of ring objects, so $R\mapsto(R,\mu_R,\eta_R)$
   is a functor from rings to $\mathrm{Mon}(\Ab)$;
3. if $R$ is commutative, then the ring object $R$ is commutative.
