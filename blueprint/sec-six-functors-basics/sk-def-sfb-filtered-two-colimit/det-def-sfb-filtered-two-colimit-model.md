+++
id = "det-def-sfb-filtered-two-colimit-model"
kind = "definition"
title = "The category $\\mathcal C_\\infty$ of a directed pseudofunctor and its comparison functor"
order = 2578
uses = ["det-def-sfb-filtered-two-colimit-cocone"]
+++
Let $I$ be a directed preordered set and $(T_{ij},\Phi_i,\theta_{ij})$ a cocone of categories with
vertex $\mathcal D$ ([det-def-sfb-filtered-two-colimit-cocone]). Assume it is *coherent*: there
are natural isomorphisms $\tau_{ijk}\colon T_{jk}\circ T_{ij}\xrightarrow{\sim}T_{ik}$ for
$i\le j\le k$ such that

- (normalization) $T_{ii}=\mathrm{Id}$, $\theta_{ii}=\mathrm{id}$, and $\tau_{iij}$, $\tau_{ijj}$ are identities;
- (cocycle) for $i\le j\le k\le l$, $\tau_{ikl}\circ T_{kl}(\tau_{ijk})=\tau_{ijl}\circ(\tau_{jkl})_{T_{ij}}$ as maps $T_{kl}T_{jk}T_{ij}\to T_{il}$;
- (compatibility) for $i\le j\le k$, $\theta_{ik}=\theta_{ij}\circ(\theta_{jk})_{T_{ij}}\circ\Phi_k(\tau_{ijk})^{-1}$ as maps $\Phi_kT_{ik}\to\Phi_i$.

Define the category $\mathcal C_\infty$:

- objects are pairs $(i,x)$ with $i\in I$ and $x\in\mathcal C_i$;
- for objects $(i,x)$, $(j,y)$ and $k\ge i,j$ put $H_k:=\Hom_{\mathcal C_k}(T_{ik}x,T_{jk}y)$, and
  for $k\le k'$ let $t_{kk'}\colon H_k\to H_{k'}$ be
  $t_{kk'}(g):=\tau_{jkk',y}\circ T_{kk'}(g)\circ\tau_{ikk',x}^{-1}$. Then
  $$
  \Hom_{\mathcal C_\infty}\bigl((i,x),(j,y)\bigr):=\colim_{k\ge i,j}H_k ,
  $$
  a filtered colimit of sets; write $[k,g]$ for the class of $g\in H_k$;
- the composite of $[k,g]\colon(i,x)\to(j,y)$ and $[k',h]\colon(j,y)\to(l,z)$ is
  $[m,\,t_{k'm}(h)\circ t_{km}(g)]$ for any $m\ge k,k'$, and the identity of $(i,x)$ is $[i,\mathrm{id}_x]$.

The *comparison functor* $\Phi\colon\mathcal C_\infty\to\mathcal D$ is
$\Phi(i,x):=\Phi_i(x)$ and $\Phi([k,g]):=\theta_{jk,y}\circ\Phi_k(g)\circ\theta_{ik,x}^{-1}$.
These are well defined, $\mathcal C_\infty$ is a category and $\Phi$ is a functor.
