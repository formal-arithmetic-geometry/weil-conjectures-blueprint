+++
kind  = "proof"
of    = "lem-pd-degree-locally-constant"
+++
We work throughout in the situation of [def-pd-fibrewise-degree], so
that the degree is the [def-pc-degree-line-bundle] and $\chi$ is the
[def-pc-euler-characteristic] of the fibre, and fibre products are those
of [def-pc-base-change].

*(1) Local constancy.* Assume that $f$ is flat. The projection
$f_T:X_T\to T$ is the base change of $f$, hence proper, flat and locally
of finite presentation; over an affine open $T_0\subseteq T$ it is
quasi-compact and quasi-separated, hence of finite presentation.
$\mathcal{L}$ is invertible,
hence of finite presentation and (as $X_T$ is flat over $T$) flat over
$T$. Fix $t\in T$ and an affine open $T_0\ni t$. By
[lem-pc-rf-perfect-base-change](1), applied to $X_{T_0}\to T_0$, there are an open
$U\ni t$ and a bounded complex $P$ of finite free $\mathcal O_U$-modules,
concentrated in degrees $[0,d]$, with $P^i\cong\mathcal O_U^{n_i}$, such
that $\mathcal H^q(g^*P)\cong R^qf'_*\mathcal L'$ for every $g:T'\to U$
($f'$, $\mathcal L'$ the base changes). For $s\in U$ take
$g=g_s:\Spec\kappa(s)\to U$: the target is a point, on which the higher
direct images are the cohomology groups of the fibre, so
$H^q(X_s,\mathcal L_s)\cong H^q(P\otimes\kappa(s))$ for all $q$.
Therefore

$$
\chi\bigl(X_s,\mathcal{L}_s\bigr)
=\sum_i(-1)^i\dim_{\kappa(s)}H^i(P\otimes\kappa(s))
=\sum_i(-1)^i\dim_{\kappa(s)}\bigl(P^i\otimes\kappa(s)\bigr)
=\sum_i(-1)^in_i ,
$$

the middle equality being the Euler characteristic of a bounded complex
of finite dimensional vector spaces. So $s\mapsto\chi(X_s,\mathcal{L}_s)$
is constant on $U$, hence locally constant on $T$. The same argument for
$\mathcal{O}_{X_T}$ shows that
$s\mapsto\chi(X_s,\mathcal{O}_{X_s})$ is locally
constant. Subtracting gives (1).

*(2) Twisting by a pullback.* Fix $t\in T$. The fibre of
$\mathcal{L}\otimes f_T^*\mathcal{N}$ over $t$ is
$\mathcal{L}_t\otimes f_t^*\mathcal{N}_t$, where $\mathcal{N}_t$ is the
pullback of $\mathcal N$ to $\Spec\kappa(t)$ and $f_t:X_t\to\Spec\kappa(t)$.
An invertible module on the point $\Spec\kappa(t)$
([def-sc-invertible-module]) is a one-dimensional vector space, hence
trivial, so $f_t^*\mathcal{N}_t\cong\mathcal O_{X_t}$ and
$\mathcal{L}_t\otimes f_t^*\mathcal{N}_t\cong\mathcal{L}_t$. Isomorphic modules
have the same cohomology, hence the same Euler characteristic, and the
fibrewise degrees of $\mathcal{L}\otimes f_T^*\mathcal{N}$ and $\mathcal{L}$
agree at $t$.

*(3) Base change.* For $t'\in T'$ with image $t\in T$ the residue field
$\kappa(t')$ is an extension of $\kappa(t)$, the fibre of $X_{T'}\to T'$
over $t'$ is $X_{t'}=X_t\times_{\kappa(t)}\Spec\kappa(t')$ (fibre products
compose), and under this identification
$(g_X^*\mathcal{L})_{t'}=(\mathcal{L}_t)_{\kappa(t')}$. Since $X_t$ is proper
over $\kappa(t)$ (base change of the proper morphism $f$), the equality is
[lem-pc-degree-base-change](1) applied to $X_t$ and the field extension
$\kappa(t')\big/\kappa(t)$.

*(4) Field-valued points.* Apply (3) to $g=\tau:T'=\Spec(K)\to T$. The
scheme $\Spec(K)$ has a single point, with residue field $K$, and the fibre of
$X_K\to\Spec(K)$ over it is $X_K$ itself; so the fibrewise degree of
$\tau_X^*\mathcal{L}$ at that point is the degree of $\tau_X^*\mathcal{L}$ on the
proper $K$-scheme $X_K$ ([def-pc-degree-line-bundle]), and (3) identifies it
with $\deg_T(\mathcal{L})(t)$.
