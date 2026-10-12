+++
id = "lem-weil-pbc-truncation-triangle"
kind = "lemma"
title = "The truncation triangle tau_{<=q-1}K -> tau_{<=q}K -> H^q(K)[-q] is distinguished"
uses = ["def-weil-abstract-derived-category", "def-weil-triangulated-category", "def-sbc-standard-tstructure-derived-category", "lem-weil-pbc-truncation-descends", "def-weil-pbc-derived-categories"]
refines = "def-weil-pbc-truncation-exact-couples"
tags = ["sheaf-dag", "stacks-08J5"]
+++
Let $\mathcal A$ be an abelian category with derived category $D(\mathcal A)$ [def-weil-abstract-derived-category], a triangulated category [def-weil-triangulated-category], with cohomology functors $H^n$ and shift $[1 ]$, $(M[1 ])^r=M^{r+1}$, $d_{M[1 ]}=-d_M$. For a complex $K$ of $\mathcal A$ and $q\in\mathbf Z$ let $\tau_{\leq q}K$ be the canonical truncation, the subcomplex $\cdots\to K^{q-2}\to K^{q-1}\to\Ker(d^q_K)\to0\to\cdots$ of $K$ (the truncation of the standard t-structure [def-sbc-standard-tstructure-derived-category]), so that $\tau_{\leq q-1}K\subseteq\tau_{\leq q}K$, and let $H^q(K)[-q ]$ be the complex with the single object $H^q(K)$ placed in degree $q$. Let $i_q:\tau_{\leq q-1}K\to\tau_{\leq q}K$ be the inclusion and $j_q:\tau_{\leq q}K\to H^q(K)[-q ]$ the morphism of complexes which in degree $q$ is the projection $\Ker(d^q_K)\to H^q(K)$ and zero in the other degrees. Then there is a unique morphism $k_q:H^q(K)[-q ]\to(\tau_{\leq q-1}K)[1 ]$ in $D(\mathcal A)$ such that
$$
 \tau_{\leq q-1}K\xrightarrow{\,i_q\,}\tau_{\leq q}K\xrightarrow{\,j_q\,}H^q(K)[-q ]\xrightarrow{\,k_q\,}(\tau_{\leq q-1}K)[1 ]
$$
is a distinguished triangle $T_q(K)$ of $D(\mathcal A)$ (namely $k_q=\delta\circ\bar j_q^{-1}$, where $\delta$ is the boundary morphism of the distinguished triangle of the short exact sequence of complexes $0\to\tau_{\leq q-1}K\to\tau_{\leq q}K\to\tau_{\leq q}K/\tau_{\leq q-1}K\to0$ and $\bar j_q:\tau_{\leq q}K/\tau_{\leq q-1}K\to H^q(K)[-q ]$ is the quasi-isomorphism induced by $j_q$). The triangle is functorial in $K$: $\tau_{\leq q}$, $\tau_{\leq q-1}$ and $H^q(-)[-q ]$ preserve quasi-isomorphisms and so act on morphisms of $D(\mathcal A)$ [lem-weil-pbc-truncation-descends], and for every morphism $f:K\to L$ of $D(\mathcal A)$ between complexes $K,L$ the triple $(\tau_{\leq q-1}f,\tau_{\leq q}f,H^q(f)[-q ])$ is a morphism of triangles $T_q(K)\to T_q(L)$. If $K$ is bounded below (as a complex, or only in cohomology: $H^n(K)=0$ for $n\ll0$), so are the three terms; in particular for $\mathcal A=\Ab(T_{\Et})$ the triangle lies in $\Dplus(T_{\Et})$ [def-weil-pbc-derived-categories].
