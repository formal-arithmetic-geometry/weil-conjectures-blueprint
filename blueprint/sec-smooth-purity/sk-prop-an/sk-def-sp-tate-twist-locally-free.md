+++
id = "det-def-sp-tate-twist-locally-free"
kind = "lemma"
title = "Tate twists are well defined and locally free of rank one"
uses = ["def-pur-roots-of-unity-sheaf", "lem-pur-finite-kummer-level", "def-coefficient-twists-detailed", "det-prop-sfb-qlbar-colimit-x-integral-limit", "det-prop-sfb-qlbar-colimit-x-invert-ell"]
+++
Let $X$ be a scheme on which $\ell$ is invertible, and let $\mu_{\ell^n,X}$ be the sheaf of
$\ell^n$th roots of unity [def-pur-roots-of-unity-sheaf], with transition maps
$\mu_{\ell^{n+1},X}\to\mu_{\ell^n,X}$, $u\mapsto u^\ell$.

1. There is a pro-étale cover $\widetilde X\to X$ and a compatible system
   $(\zeta_n)_{n\ge1}$, $\zeta_n\in\mu_{\ell^n,X}(\widetilde X)$, $\zeta_{n+1}^\ell=\zeta_n$,
   such that each $\zeta_n$ generates: $(\mathbf Z/\ell^n)_{\widetilde X}\to\mu_{\ell^n,\widetilde X}$,
   $a\mapsto\zeta_n^a$, is an isomorphism.
2. For a finite ring $A$ with $\ell^rA=0$ and $r'\ge r$, the Kummer map
   $\mu_{\ell^{r'},X}\to\mu_{\ell^r,X}$, $u\mapsto u^{\ell^{r'-r}}$, induces an isomorphism
   $\mu_{\ell^{r'},X}\otimes_{\mathbf Z/\ell^{r'}}A_X\cong\mu_{\ell^r,X}\otimes_{\mathbf Z/\ell^r}A_X$;
   so $A_X(1)$ is independent of $r$ up to canonical isomorphism.
3. For $\Lambda\in\{A,\cO_E,E,\Qlb\}$ the sheaf $\Lambda_X(1)$ is an invertible
   $\Lambda_X$-module: on $\widetilde X$ it is isomorphic to $\Lambda_{\widetilde X}$. Hence
   so are $\Lambda_X(d)$ and $\Lambda_X(-d)$ for $d\ge0$, $\Lambda_X(d)\otimes\Lambda_X(-d)\cong\Lambda_X$,
   and $K\mapsto K(d)$ is an autoequivalence of $D(X_{\mathrm{proét}},\Lambda)$ with inverse
   $K\mapsto K(-d)$.
