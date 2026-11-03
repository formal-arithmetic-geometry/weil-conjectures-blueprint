+++
kind  = "proof"
of    = "det-lem-coefficient-finite-descent-lisse"
+++
(1) Choose a covering $\{V_k\to X\}$ on which $L$ is free, $L|_{V_k}\cong\QbarX^{r}|_{V_k}$ (the
rank is locally constant; work on each of the finitely many open and closed pieces of
constant rank). Since $X$ is quasi-compact, finitely many $V_k$ suffice, and we may take them
affine. Since $X$ is quasi-separated, $V_{kk'}=V_k\times_XV_{k'}$ and the triple products are
quasi-compact. The trivializations give transition matrices
$g_{kk'}\in\GL_r(\QbarX(V_{kk'}))$ with $g_{kk}=1$ and $g_{kk'}g_{k'k''}=g_{kk''}$ on
$V_{kk'k''}$. By [det-lem-coefficient-finite-descent-sections] (2) the finitely many entries
of all $g_{kk'}$ and $g_{kk'}^{-1}$ lie in $E_X(V_{kk'})$ for a single finite $E$. The cocycle
identities hold in $\GL_r(E_X(V_{kk'k''}))$ because $E_X\to\QbarX$ is injective on sections. By
descent of sheaves along the covering, the cocycle defines a module $L_E$, locally free of
rank $r$ over $E_X$, and $\QbarX\otimes_{E_X}L_E$ is described by the same cocycle viewed over
$\QbarX$, hence is isomorphic to $L$.

(2) Injectivity: if $\phi\colon M_F\to N_F$ becomes zero over $\Qlb$, then on a trivializing
cover its matrix entries vanish in $\QbarX(V)\supseteq F_X(V)$, so $\phi=0$. Surjectivity: a
morphism $M_{\Qlb}\to N_{\Qlb}$ is given on a finite trivializing cover by finitely many
matrices with entries in $\QbarX(V_k)$ satisfying the compatibility with the transition
matrices of $M$ and $N$ on $V_{kk'}$; their entries lie in $F_X(V_k)$ for a finite $F\supseteq E$,
the compatibilities hold over $F_X$ by injectivity, so they glue to $M_F\to N_F$.
