+++
kind  = "proof"
of    = "lem-weil-karoubi-envelope-fully-faithful"
+++
By [def-weil-karoubi-envelope] the objects of $\Kar(\mathcal T)$ are the
pairs $(K,e)$ with $e^2=e$, the morphisms $(K,e)\to(L,d)$ are the morphisms
$u:K\to L$ of $\mathcal T$ satisfying $u=d\,u\,e$, and composition and
identities are those of $\mathcal T$. For $f:K\to L$ the condition is
$\operatorname{id}_L\,f\,\operatorname{id}_K=f$, which every morphism $f$
satisfies, so the map

$$
 \Hom_{\mathcal T}(K,L)\longrightarrow
 \Hom_{\Kar(\mathcal T)}\bigl((K,\operatorname{id}_K),
 (L,\operatorname{id}_L)\bigr),\qquad f\longmapsto f,
$$

is bijective; it is the identity on underlying morphisms, so it preserves
composition and identities. Hence the canonical functor is full and faithful.
