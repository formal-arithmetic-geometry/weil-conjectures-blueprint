+++
id = "lem-weil-pbc-truncation-couple-morphism"
kind = "lemma"
title = "The exchange morphisms on the truncation triangles form a morphism of exact couples"
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-inverse-image", "def-weil-pbc-direct-image", "lem-weil-pbc-derived-direct-image-triangulated", "def-weil-pbc-derived-exchange", "lem-weil-pbc-truncation-triangle", "def-weil-derived-cohomology-sheaves", "def-sp-exact-couple", "lem-weil-pbc-exact-functor-bounded-below"]
refines = "def-weil-pbc-truncation-exact-couples"
tags = ["sheaf-dag", "stacks-0DDE"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a cartesian square of schemes [def-weil-pbc-cartesian-square], with $f:X\to Y$, $g:Y'\to Y$, $f':X'\to Y'$, $g':X'\to X$. On the bounded below derived categories of etale abelian sheaves [def-weil-pbc-derived-categories] put
$$
 \Phi=g^{-1}\circ Rf_*,\qquad \Psi=Rf'_*\circ g'^{-1}:\ \Dplus(X_{\Et})\longrightarrow\Dplus(Y'_{\Et}),
$$
with $u^{-1}$ the inverse image [def-weil-pbc-derived-inverse-image] and $Ru_*$ the derived direct image [def-weil-pbc-direct-image], and let $\xi_L:\Phi(L[1 ])\xrightarrow{\sim}\Phi(L)[1 ]$, $\zeta_L:\Psi(L[1 ])\xrightarrow{\sim}\Psi(L)[1 ]$ be the composite shift-commutation isomorphisms (for $u^{-1}$ the identity of termwise shifted complexes, for $Ru_*$ the isomorphism $\sigma$ of [lem-weil-pbc-derived-direct-image-triangulated]). Let $\Ex_\square:\Phi\to\Psi$ be the derived exchange transformation [def-weil-pbc-derived-exchange]. Let $K\in\Dplus(X_{\Et})$ and, for $q\in\mathbf Z$, let
$$
 T_q:\quad \tau_{\leq q-1}K\xrightarrow{\,i_q\,}\tau_{\leq q}K\xrightarrow{\,j_q\,}\mathcal H^q(K)[-q ]\xrightarrow{\,k_q\,}(\tau_{\leq q-1}K)[1 ]
$$
be the truncation triangle [lem-weil-pbc-truncation-triangle], $\mathcal H^n$ denoting cohomology sheaves [def-weil-derived-cohomology-sheaves]. For $F\in\{\Phi,\Psi\}$, with $c_F=\xi$ resp. $\zeta$, define bigraded etale sheaves on $Y'$ and maps
$$
 D_F^{p,q}=\mathcal H^{p+q}(F\tau_{\leq q}K),\qquad E_F^{p,q}=\mathcal H^{p+q}\bigl(F(\mathcal H^q(K)[-q ])\bigr),
$$
$$
 \alpha_F=\mathcal H^{p+q}(F i_{q+1}):D_F^{p,q}\to D_F^{p-1,q+1},\qquad g_F=\mathcal H^{p+q}(F j_q):D_F^{p,q}\to E_F^{p,q},
$$
$$
 f_F:E_F^{p,q}\xrightarrow{\mathcal H^{p+q}(c_{F,\tau_{\leq q-1}K}\circ F k_q)}\mathcal H^{p+q}\bigl((F\tau_{\leq q-1}K)[1 ]\bigr)=\mathcal H^{p+q+1}(F\tau_{\leq q-1}K)=D_F^{p+2,q-1},
$$
and put $t_D^{p,q}=\mathcal H^{p+q}(\Ex_{\square,\tau_{\leq q}K}):D_\Phi^{p,q}\to D_\Psi^{p,q}$ and $t_E^{p,q}=\mathcal H^{p+q}(\Ex_{\square,\mathcal H^q(K)[-q ]}):E_\Phi^{p,q}\to E_\Psi^{p,q}$.

Then:

(1) for $F=\Phi$ and $F=\Psi$, $(D_F,E_F,\alpha_F,f_F,g_F)$ is an exact couple [def-sp-exact-couple];

(2) $(t_D,t_E)$ is a morphism of exact couples from the $\Phi$-couple to the $\Psi$-couple: $t_D\circ\alpha_\Phi=\alpha_\Psi\circ t_D$, $t_E\circ g_\Phi=g_\Psi\circ t_D$ and $t_D^{p+2,q-1}\circ f_\Phi=f_\Psi\circ t_E^{p,q}$ in every bidegree;

(3) for every $(p,q)$, under the canonical isomorphisms $E_\Phi^{p,q}\cong\mathcal H^p(\Phi\,\mathcal H^q(K))=g^{-1}R^pf_*\mathcal H^q(K)$ and $E_\Psi^{p,q}\cong\mathcal H^p(\Psi\,\mathcal H^q(K))=R^pf'_*g'^{-1}\mathcal H^q(K)$ (given by $\mathcal H^{p+q}$ of the iterated shift isomorphisms $\xi^{(-q)},\zeta^{(-q)}$, the identity $\mathcal H^{p+q}(L[-q ])=\mathcal H^p(L)$, and $\mathcal H^p\circ g^{-1}=g^{-1}\circ\mathcal H^p$), the map $t_E^{p,q}$ is the degree-$p$ exchange map of the sheaf $\mathcal H^q(K)$,
$$
 \mathcal H^p(\Ex_{\square,\mathcal H^q(K)}):\ g^{-1}R^pf_*\mathcal H^q(K)\longrightarrow R^pf'_*g'^{-1}\mathcal H^q(K).
$$
