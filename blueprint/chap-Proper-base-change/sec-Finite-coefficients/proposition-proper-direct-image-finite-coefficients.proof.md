+++
kind = "proof"
of = "proposition-proper-direct-image-finite-coefficients"
order = 406
uses = ["theorem-comparison-direct-images", "corollary-finite-tor-amplitude-under-comparison"]
+++
By Corollary [corollary-finite-tor-amplitude-under-comparison] the
étale and pro-étale categories $D^b_{\mathrm{ctf}}$ agree, and by
Theorem [theorem-comparison-direct-images] so do the proper direct
images of their bounded below complexes. We can therefore transport bounded constructibility and the Tor bound
from the étale site.

On the étale site, let $C\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$. The proper
direct image of a constructible torsion sheaf is constructible
[Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)], and $\operatorname{cd}_\ell(p)<\infty$
[Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. Hence $Rp_*C\in\Dbc(Y_{\acute{e}t},A)$.

To check finite Tor amplitude, suppose that $C$ has Tor amplitude $[a,b]$, and let
$d$ be an integer with $\operatorname{cd}_\ell(X_{\bar y})\leq d$ for
all geometric points $\bar y$ of $Y$. Derived tensor products are computed
stalkwise. It therefore suffices to show that each stalk $(Rp_*C)_{\bar y}$ has
Tor amplitude in $[a,b+d]$ as a complex of $A$-modules. In other words,
$(Rp_*C)_{\bar y}\otimes^{\mathbf L}_AN=((Rp_*C)\otimes_A^{\mathbf L}N_Y)_{\bar y}$
should have cohomology in $[a,b+d]$ for every $A$-module $N$. By proper base change
and the projection formula for constant modules [Stacks, [0F12](https://stacks.math.columbia.edu/tag/0F12)], this stalk is

$$
R\Gamma\bigl(X_{\bar y},
C|_{X_{\bar y}}\otimes_A^{\mathbf L}N_{X_{\bar y}}\bigr).
$$

The complex $C|_{X_{\bar y}}\otimes_A^{\mathbf L}N_{X_{\bar y}}$ has
cohomology in $[a,b]$, because restriction to the fibre preserves Tor
amplitude. Since $R\Gamma(X_{\bar y},-)$ preserves $D^{\geq a}$ and has
cohomological dimension at most $d$, it keeps the lower bound and raises the upper bound by
at most $d$. Thus $Rp_*C\in D^b_{\mathrm{ctf}}(Y_{\acute{e}t},A)$, with Tor amplitude in $[a,b+d]$.
