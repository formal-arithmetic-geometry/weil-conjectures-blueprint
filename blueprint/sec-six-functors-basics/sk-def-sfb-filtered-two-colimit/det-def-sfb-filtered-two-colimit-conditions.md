+++
id = "det-def-sfb-filtered-two-colimit-conditions"
kind = "definition"
title = "Filtered 2-colimit conditions"
order = 2577
uses = ["det-def-sfb-filtered-two-colimit-cocone"]
+++
A cocone of categories $(T_{ij},\Phi_i,\theta_{ij})$ with vertex $\mathcal D$
([det-def-sfb-filtered-two-colimit-cocone]) *is a filtered 2-colimit* if the following three
conditions hold.

- **(Obj)** For every object $d$ of $\mathcal D$ there are $i\in I$, $x\in\mathcal C_i$ and an
  isomorphism $d\cong\Phi_i(x)$.
- **(Hom-surj)** For all $i,j\in I$, $x\in\mathcal C_i$, $y\in\mathcal C_j$ and every morphism
  $\varphi\colon\Phi_i(x)\to\Phi_j(y)$ of $\mathcal D$, there are $k\in I$ with $k\ge i$, $k\ge j$
  and a morphism $g\colon T_{ik}x\to T_{jk}y$ of $\mathcal C_k$ such that
  $$
  \varphi=\theta_{jk,y}\circ\Phi_k(g)\circ\theta_{ik,x}^{-1}.
  $$
- **(Hom-inj)** For every $k\in I$ and all morphisms $g,g'\colon x\to y$ of $\mathcal C_k$ with
  $\Phi_k(g)=\Phi_k(g')$, there is $k'\ge k$ with $T_{kk'}(g)=T_{kk'}(g')$.

Thus, in a filtered 2-colimit, every object of $\mathcal D$ is isomorphic to one coming from a single
stage $\mathcal C_i$ (this is (Obj)), every morphism between objects coming from stages comes from a
morphism at a later stage (this is (Hom-surj)), and two morphisms of $\mathcal C_k$ that become equal
in $\mathcal D$ already become equal at some later stage $\mathcal C_{k'}$ (this is (Hom-inj)). The
definition is a property of ordinary categories and functors.
