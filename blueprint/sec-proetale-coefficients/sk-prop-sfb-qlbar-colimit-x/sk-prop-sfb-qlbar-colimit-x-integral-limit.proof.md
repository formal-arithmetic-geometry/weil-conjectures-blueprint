+++
kind  = "proof"
of    = "det-prop-sfb-qlbar-colimit-x-integral-limit"
+++
*Step 1: finite constant sheaves.* For $U\in X_{\mathrm{proét}}$, a morphism of $X$-schemes
$U\to\coprod_TX$ is the same as a decomposition of $U$ into open and closed pieces
$U_t$, $t\in T$, that is, a locally constant function $|U|\to T$. The sheaf of locally
constant functions to $T$ is the constant sheaf $T_X$ (the pro-étale site is
subcanonical, and a locally constant function is the sheafification of a constant one).
So $\coprod_TX$ represents $T_X$.

*Step 2: limits of representables.* The transition maps $\cO_E/\pi_E^{n+1}\to\cO_E/\pi_E^n$
induce affine morphisms $\coprod_{\cO_E/\pi_E^{n+1}}X\to\coprod_{\cO_E/\pi_E^n}X$, each
finite étale, so the inverse limit $X[\cO_E]$ exists as a scheme pro-étale over $X$. For
every $U$ we have $\Hom_X(U,\varprojlim_nY_n)=\varprojlim_n\Hom_X(U,Y_n)$ by the universal
property of the limit. Hence the sheaf represented by $X[\cO_E]$ is
$\varprojlim_nh_{Y_n}$ with $Y_n=\coprod_{\cO_E/\pi_E^n}X$, which is
$\varprojlim_n(\cO_E/\pi_E^n)_X$ by Step 1. This proves (1).

*Step 3: the pullback of a representable condensed set.* The condensed set underlying
$\underline{\cO_E}$ is $S\mapsto C(S,\cO_E)=\Hom_{\mathrm{cont}}(S,\cO_E)$, i.e. it is
represented by the profinite set $\cO_E$ in $*_{\mathrm{proét}}$. By
[sk-def-sfb-pullback-from-point], $p_X^*$ is the inverse image along the continuous,
finite-limit preserving functor $u_X\colon S\mapsto X[S]$. Such an inverse image sends the
sheaf represented by $S$ to the sheafification of the presheaf represented by $u_X(S)$,
and since $X_{\mathrm{proét}}$ is subcanonical this is the sheaf represented by
$X[S]$. With $S=\cO_E$ this is (2). (The inverse image on abelian sheaves and on sheaves of
sets are compatible with the forgetful functors, since both are left exact inverse images
of the same morphism of topoi.)

*Step 4: ring structures.* The ring operations of $\underline{\cO_E}$ are given by the
continuous maps $+,\cdot\colon\cO_E\times\cO_E\to\cO_E$ and the constants $0,1$. Since $u_X$
preserves finite products, $p_X^*$ transports them to the maps of representing schemes
$X[\cO_E]\times_XX[\cO_E]=X[\cO_E\times\cO_E]\to X[\cO_E]$ induced by these maps. On the
other side, the ring operations of $\varprojlim_n(\cO_E/\pi_E^n)_X$ are the limits of the
ring operations of the finite rings $\cO_E/\pi_E^n$, which are the maps of the
$\coprod_{\cO_E/\pi_E^n}X$ induced by the operations of $\cO_E/\pi_E^n$. Since the
operations of $\cO_E$ are the limits of those of $\cO_E/\pi_E^n$, the two sets of
operations correspond under the identifications of Steps 2 and 3 by the Yoneda lemma. This
proves (3).

The proof does not claim that $p_X^*$ commutes with inverse limits: in general it does not.
The point is that $\underline{\cO_E}$ is representable and $u_X$ commutes with the relevant
cofiltered limit of profinite sets.
