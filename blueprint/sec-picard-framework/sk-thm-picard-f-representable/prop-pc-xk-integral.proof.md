+++
kind  = "proof"
of    = "prop-pc-xk-integral"
+++
For (1): $X$ is reduced (smooth over a field) and connected, so
$k':=H^0(X,\mathcal{O}_X)$ is a finite-dimensional reduced $k$-algebra without
nontrivial idempotents, i.e. a finite field extension of $k$. Since $X$ is
smooth, it is geometrically reduced, so $k'\otimes_k\bar k\subseteq
H^0(X_{\bar k},\mathcal{O})$ is reduced and $k'/k$ is separable; as $k$ is
separably closed, $k'=k$. Since $H^0(X,\mathcal{O}_X)=k$, the quasi-coherent
$\mathcal{O}_k$-module $f_*\mathcal{O}_X$ is free of rank one, so
$f_*\mathcal{O}_X=\mathcal{O}_k$.

For (2): let $K/k$ be a field extension and let
$g:\operatorname{Spec}(K)\to\operatorname{Spec}(k)$. The morphism $g$ is flat
([lem-pc-flat-field]), both bases are affine, and $f$ is quasi-compact and
quasi-separated (it is proper), so
[lem-pc-flat-base-change-cohom] applied to $\mathcal{F}=\mathcal{O}_X$ gives

$$
H^i(X,\mathcal{O}_X)\otimes_kK\;\cong\;H^i(X_K,\mathcal{O}_{X_K})\qquad(i\ge0).
$$

For $i=0$ this gives $H^0(X_K,\mathcal{O}_{X_K})=k\otimes_kK=K$, hence
$f_{K,*}\mathcal{O}_{X_K}=\mathcal{O}_K$ ($\operatorname{Spec}(K)$ is a point,
and the canonical map $\mathcal{O}_K\to f_{K,*}\mathcal{O}_{X_K}$ is the
isomorphism $K\to H^0(X_K,\mathcal{O}_{X_K})$ on global sections); for $i=1$ it
gives $\dim_K H^1(X_K,\mathcal{O}_{X_K})=\dim_kH^1(X,\mathcal{O}_X)$.
The morphism $X_K\to\operatorname{Spec}(K)$ is smooth (base change of smooth,
[lem-pc-proper-base-change]) and proper (base change of proper,
[lem-pc-proper-base-change]), so $X_K$ is regular
([lem-sc-smooth-regular]), hence normal ([rem-pc-regular-normal])
and reduced. Moreover $X_K$ is geometrically reduced: for every $K'/K$,
$X_{K'}$ is smooth over $K'$, hence regular, hence reduced; and $X_K$ is
proper, so [lem-pc-h0-geom-connected] (with $k$ replaced by $K$ and
$X$ by $X_K$) shows that $X_K$ is geometrically connected, in particular
connected. A Noetherian normal connected scheme is irreducible by
[rem-pc-regular-normal]: the normal scheme $X_K$ is a finite disjoint
union of normal integral schemes, and connectedness forces a single
component. Hence $X_K$ is integral. By [lem-pc-dim-base-change]
the dimension of $X_K$ is $1$, and $X_K\to\operatorname{Spec}(K)$ is of finite type and
separated (base changes of finite type and separated morphisms), so $X_K$
is a variety of dimension $1$, i.e. a curve ([def-pc-curve]). This proves
(2); applying (2) to $K=k$ (and all extensions) gives geometric
integrality of $X$.
