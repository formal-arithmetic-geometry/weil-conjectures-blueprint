+++
kind = "proof"
of = "det-tf-restriction-zero-localization"
uses = ["det-tf-supported-restriction"]
+++
*(i).* Since $K_{\bar y}=0$, the open–closed triangle
$j_{Y!}j_Y^*K\to K\to i_*i^*K$ has vanishing third term, so $K=j_{Y!}Q$. Applying
duality, $\mathbb D_XK=\mathbb D_X j_{X!}(K|_{X-y})=Rj_{X*}\mathbb D_{X-y}(K|_{X-y})=Rj_{X*}N$,
where $N$ is the dual of $K|_{X-y}$ for the restriction of $\omega_X$. The ordinary
external Künneth comparison for $Rj_{X*}N\boxtimes j_{Y!}Q$ gives
$P\simeq Rf_*g_!(N\boxtimes Q)$: extension by zero in the second factor is $g_!$ away
from $V$, and the direct image in the first factor is $Rf_*$ across $V$.

*(ii).* $T$ and $B$ are strictly local, so $R\Gamma$ is the stalk at the closed point,
which is $(\mathbb D_XK)_{\bar y}\otimes^{\mathbf L}K_{\bar y}=0$.

*(iii).* The localization triangles
$R\Gamma_G(T,P)\to R\Gamma(T,P)\to R\Gamma(T-G,P)$ and
$R\Gamma_y(B,b^*P)\to R\Gamma(B,b^*P)\to R\Gamma(B-y,b^*P)$ are compatible with
restriction along $b$, by the construction of $\rho_{a,b}$ in
[det-tf-supported-restriction]. By (ii) the middle terms vanish, so the boundary maps
identify $\rho_{a,b}$, shifted by one, with the restriction
$R\Gamma(T-G,P)\to R\Gamma(B-y,b^*P)$. By (i), $R\Gamma(T-G,P)=
R\Gamma(T-(V\cup G),g_!(N\boxtimes Q))$, since $R\Gamma(W,Rf_*M)=R\Gamma(W\cap(T-V),M)$ for
every open $W\subseteq T$, and $(b^*P)|_{B-y}=(N\boxtimes Q)|_{B-y}$,
since $B-y$ lies in $T-(H\cup V)$.
