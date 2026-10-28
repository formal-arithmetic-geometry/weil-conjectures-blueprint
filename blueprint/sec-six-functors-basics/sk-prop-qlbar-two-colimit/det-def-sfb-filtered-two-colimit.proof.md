+++
kind  = "proof"
of    = "det-def-sfb-filtered-two-colimit"
+++
The two final assertions are (Obj) and (Hom-inj) restated.

The conditions characterise the 2-colimit. Suppose $I$ is directed and the transition functors
are coherent (a pseudofunctor $I\to\mathrm{Cat}$, with the $\theta_{ij}$ compatible with its
structure isomorphisms). The 2-colimit is then modelled by the ordinary category $\mathcal C_\infty$
whose objects are pairs $(i,x)$ with $x\in\mathcal C_i$ and whose morphisms are
$\Hom((i,x),(j,y))=\operatorname{colim}_{k\ge i,j}\Hom_{\mathcal C_k}(T_{ik}x,T_{jk}y)$, a
filtered colimit of sets, with composition defined after passing to a common index. The cocone
induces a comparison functor $\Phi\colon\mathcal C_\infty\to\mathcal D$,
$(i,x)\mapsto\Phi_i(x)$. It is essentially surjective if and only if (Obj) holds. On morphisms
it is the canonical map $\operatorname{colim}_k\Hom_{\mathcal C_k}(T_{ik}x,T_{jk}y)\to
\Hom_{\mathcal D}(\Phi_i x,\Phi_j y)$: (Hom-surj) is its surjectivity, and since the colimit is
filtered, two elements with the same image can be represented at a common index $k$, where
(Hom-inj) makes them equal at a later index; so (Hom-surj) and (Hom-inj) say that $\Phi$ is
fully faithful. Hence, under these assumptions, the cocone is a filtered 2-colimit if and only if
$\Phi$ is an equivalence of categories.
