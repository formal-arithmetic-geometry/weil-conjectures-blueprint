+++
kind  = "proof"
of    = "lem-pc-k-sheaf"
+++
Let $\{T_i\to T\}_{i\in I}$ be an fppf covering and let
$\mathcal{L}_i\in K(T_i)$ with $\mathcal{L}_i$ and $\mathcal{L}_j$ mapping to the same element of
$K(T_i\times_TT_j)$ (the restriction maps of $K$ are those of the
subfunctor [lem-pc-sigma-subfunctor]).
Choose an isomorphism $\alpha_i:\mathcal{O}_{T_i}\to\sigma_{T_i}^*\mathcal{L}_i$ for all
$i$, and an isomorphism

$$
\varphi_{ij}:\mathcal{L}_i|_{X_{T_i\times_TT_j}}\longrightarrow
\mathcal{L}_j|_{X_{T_i\times_TT_j}} .
$$

The composite

$$
\alpha_j^{-1}|_{T_{ij}}\circ\sigma_{T_{ij}}^*\varphi_{ij}\circ\alpha_i|_{T_{ij}}:
\mathcal{O}_{T_{ij}}\longrightarrow\mathcal{O}_{T_{ij}}
$$

is multiplication by some unit $u_{ij}$; replacing $\varphi_{ij}$ by
$u_{ij}^{-1}\varphi_{ij}$ we may assume the composite is
multiplication by $1$, i.e. that the $\varphi_{ij}$ are compatible with
the $\alpha$'s along $\sigma$.
Now the self-map of $\mathcal{L}_i|_{X_{T_{ijk}}}$

$$
\varphi_{ki}\circ\varphi_{jk}\circ\varphi_{ij}
$$

is multiplication by a unit
$u_{ijk}\in\Gamma(X_{T_{ijk}},\mathcal{O}^*)$; by the equality
$\Gamma(X_{T_{ijk}},\mathcal{O}^*)=\Gamma(T_{ijk},\mathcal{O}^*)$ (from the hypothesis)
we may regard $u_{ijk}$ as a unit on $T_{ijk}$, and its image under
$\sigma^*$ is $1$ by the $\alpha$-compatibility —since
$\sigma^*:\Gamma(X_T,\mathcal{O}^*)\to\Gamma(T,\mathcal{O}^*)$ is inverse to
the pullback $f^*$, $u_{ijk}=1$ and the $\varphi_{ij}$ satisfy the cocycle
condition. Thus $\{\mathcal{L}_i|_{X_{T_i}},\varphi_{ij}\}$ is a descent datum
for invertible modules on the fppf (in particular fpqc) covering
$\{X_{T_i}\to X_T\}$; by [lem-pc-fpqc-descent] there exists an
invertible $\mathcal{O}_{X_T}$-module $\mathcal{L}$ with
$\mathcal{L}|_{X_{T_i}}=\mathcal{L}_i$ (with the given gluing isomorphisms). Since the
gluing isomorphisms are compatible with the trivializations $\alpha_i$,
the module $\sigma_T^*\mathcal{L}$ restricts to the trivial module on $T_i$ in a
compatible way, so $\sigma_T^*\mathcal{L}\cong\mathcal{O}_T$ by descent: hence
$\mathcal{L}\in K(T)$. Uniqueness of gluing gives the uniqueness in the sheaf
condition. This proves the lemma.
