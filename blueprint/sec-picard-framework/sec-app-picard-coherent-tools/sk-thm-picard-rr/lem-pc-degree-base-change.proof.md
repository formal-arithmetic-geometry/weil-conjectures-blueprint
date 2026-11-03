+++
kind  = "proof"
of    = "lem-pc-degree-base-change"
+++
*(3).* This is exactly [lem-pc-euler-additive].

*(1).* For the field extension $K/k$ put
$X_K:=X\times_{\operatorname{Spec}(k)}\operatorname{Spec}(K)$ ([def-pc-base-change]).
By flat base change ([lem-pc-flat-base-change-cohom], along the flat
morphism $\operatorname{Spec}(K)\to\operatorname{Spec}(k)$) one has
$H^i(X_K,\mathcal{L}\otimes_kK)=H^i(X,\mathcal{L})\otimes_kK$ and
$H^i(X_K,\mathcal{O}_{X_K})=H^i(X,\mathcal{O}_X)\otimes_kK$ for all $i$; the $H^i$ are
finite-dimensional and vanish for $i\gg0$
([lem-pc-euler-characteristic-well-defined]), and $X_K$ is proper over $K$
([lem-pc-proper-base-change]), so
[def-pc-euler-characteristic] and [def-pc-degree-line-bundle]
apply and give

$$
\deg_{X_K}(\mathcal{L}_K)
=\sum_i(-1)^i\dim_K\bigl(H^i(X,\mathcal{L})\otimes_kK\bigr)
-\sum_i(-1)^i\dim_K\bigl(H^i(X,\mathcal{O}_X)\otimes_kK\bigr)
=\deg_X(\mathcal{L}),
$$

because $\dim_K(V\otimes_kK)=\dim_kV$ for a finite-dimensional
$k$-vector space $V$.

*(2), effective divisors.* Now $X$ is smooth of relative dimension $1$.
Let $D\subset X$ be an effective Cartier divisor
([def-nagata-invertible-ideal]) with ideal sheaf $\mathcal{I}_D$ and
put $\mathcal{M}=\mathcal{O}_X(D)=\mathcal{I}_D^\vee$
([def-pc-divisor-line-bundle]). The closed subscheme $D$ is finite over
$k$: it is proper, and it is quasi-finite, because a local equation of
$D$ is a non-zero-divisor in a one-dimensional local ring of $X$, so $D$
contains no generic point of $X$. Tensoring
$0\to\mathcal{I}_D\to\mathcal{O}_X\to\mathcal{O}_D\to0$ with the invertible
(hence flat) module $\mathcal{L}\otimes\mathcal{M}$ and using
$\mathcal{I}_D\otimes\mathcal{M}\cong\mathcal{O}_X$ gives the exact sequence

$$
0\to\mathcal{L}\to\mathcal{L}\otimes\mathcal{M}\to(\mathcal{L}\otimes\mathcal{M})|_D\to0 .
$$

The restriction $(\mathcal{L}\otimes\mathcal{M})|_D$ is an invertible module on
the finite, hence affine, $k$-scheme $D$, so its higher cohomology vanishes
([pqf-lem-affine-vanishing]) and, $D$ being a finite disjoint union of
spectra of Artinian local rings, it is isomorphic to $\mathcal{O}_D$; thus
$\chi\bigl(X,(\mathcal{L}\otimes\mathcal{M})|_D\bigr)=\dim_kH^0(D,\mathcal{O}_D)$.
Additivity (3) gives
$\chi(X,\mathcal{L}\otimes\mathcal{M})=\chi(X,\mathcal{L})+\dim_kH^0(D,\mathcal{O}_D)$.
With $\mathcal{L}=\mathcal{O}_X$ this is
$\deg(\mathcal{M})=\chi(\mathcal{M})-\chi(\mathcal{O}_X)=\dim_kH^0(D,\mathcal{O}_D)$
([def-pc-degree-line-bundle]), and substituting back gives
$\chi(X,\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\chi(X,\mathcal{M})$.
(At a point $P$ of $D$ the local ring $\mathcal{O}_{X,P}$ is a discrete
valuation ring ([lem-sc-smooth-regular], [lem-sc-regular-dim1-dvr]), and if
$\mathcal{I}_{D,P}=\mathfrak m_P^{n_P}$ then
$\dim_k\mathcal{O}_{D,P}=n_P[\kappa(P):k]$, so
$\dim_kH^0(D,\mathcal{O}_D)=\sum_Pn_P[\kappa(P):k]$ is the classical degree of
$D$.)

A $k$-rational point $P$ with its reduced structure is an effective Cartier
divisor ([lem-sc-point-cartier]) with $H^0(P,\mathcal{O}_P)=k$, so
$\deg(\mathcal{O}_X(P))=1$. The sum $D=\sum_in_i[P_i]$ has ideal sheaf
$\prod_i\mathcal{I}_{P_i}^{n_i}$, hence
$\mathcal{O}_X(D)\cong\bigotimes_i\mathcal{O}_X(P_i)^{\otimes n_i}$, and the
additivity of the degree proved next gives
$\deg(\mathcal{O}_X(D))=\sum_in_i$.

*(2), additivity of the degree.* Every invertible $\mathcal{M}$ is
$\mathcal{O}_X(D_1)\otimes\mathcal{O}_X(D_2)^{-1}$ for effective Cartier
divisors $D_1,D_2$. Indeed, choose a closed point on each of the finitely
many connected components of $X$ and let $D_0$ be their sum; by the
formula just proved, $h^0(\mathcal{M}\otimes\mathcal{O}_X(nD_0))
\ge\chi(\mathcal{M}\otimes\mathcal{O}_X(nD_0))\ge\chi(\mathcal{M})+n$ on each
component (by Grothendieck vanishing on the one-dimensional Noetherian space $X$,
cohomology vanishes in degrees $\ge2$), so for
$n\gg0$ the module $\mathcal{M}\otimes\mathcal{O}_X(D_2)$, $D_2=nD_0$, has a
global section $s$ which is nonzero on every (integral) component; its zero
scheme $D_1$ is then an effective Cartier divisor, and $s$ identifies
$\mathcal{M}\otimes\mathcal{O}_X(D_2)$ with $\mathcal{O}_X(D_1)$. Applying the
effective case twice,

$$
\chi(\mathcal{L}\otimes\mathcal{M})+\deg D_2=\chi(\mathcal{L}\otimes\mathcal{O}_X(D_1))=\chi(\mathcal{L})+\deg D_1,
$$

and the same identity with $\mathcal{L}=\mathcal{O}_X$ reads
$\chi(\mathcal{M})+\deg D_2=\chi(\mathcal{O}_X)+\deg D_1$. Subtracting,
$\chi(\mathcal{L}\otimes\mathcal{M})-\chi(\mathcal{L})=\chi(\mathcal{M})-\chi(\mathcal{O}_X)$,
i.e. $\deg(\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\deg(\mathcal{M})$.

For the last assertion, $X_K$ is again proper and smooth of relative
dimension $1$ over $K$ ([lem-pc-proper-base-change]), so additivity on
$X_K$ and (1) give
$\deg(\mathcal{L}'\otimes\mathcal{M}_K)=\deg(\mathcal{L}')+\deg(\mathcal{M}_K)
=\deg(\mathcal{L}')+\deg(\mathcal{M})$.
