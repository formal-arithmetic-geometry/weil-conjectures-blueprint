+++
kind = "proof"
of = "sk-cor-sf-direct-image-ctf"
uses = ["sk-cor-geo-open-finiteness", "sk-prop-classical-inputs", "sk-cor-pe-finite-tor-comparison", "sk-prop-pe-unbounded-classical"]
+++
The complex $Rj_*K$ is bounded constructible by
Corollary [sk-cor-geo-open-finiteness], and $\operatorname{cd}_\ell(j)$ is finite
by [Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10) (Remark [sk-prop-classical-inputs]). To bound the Tor amplitude, we
work on the étale site, where geometric points are conservative. By Corollary [sk-cor-pe-finite-tor-comparison],
$K\simeq\nu_U^*K_{\acute{e}t}$ for some $K_{\acute{e}t}\in D^b_{\mathrm{ctf}}(U_{\acute{e}t},A)$, and the pro-étale pullback of
$Rj_{\acute{e}t,*}K_{\acute{e}t}$ is $Rj_*K$ by
Proposition [sk-prop-pe-unbounded-classical].

We first prove the projection formula for constant coefficients: for every $A$-module $M$, viewed as a constant sheaf, the
projection morphism

$$
(Rj_*K)\otimes_A^{\mathbf L}\underline M_X
\xrightarrow{\ \sim\ }
Rj_*\bigl(K\otimes_A^{\mathbf L}\underline M_U\bigr)
\tag{7.23}
$$

is an isomorphism. Recall that for a scheme $V$
with $\operatorname{cd}_\ell(V)<\infty$, the projection formula of
[Stacks, Tag 0F12](https://stacks.math.columbia.edu/tag/0F12) identifies
$R\Gamma(V,K)\otimes^{\mathbf L}_AM$ with
$R\Gamma(V,K\otimes^{\mathbf L}_A\underline M)$. Applying it to every
quasi-compact étale $V\to X$ and to $V\times_XU$, we obtain isomorphisms
between the derived sections of the two sides of the étale version of
(7.23), compatibly with the projection
morphism. Hence the étale version holds. Since inverse image is exact and symmetric monoidal and
commutes with unbounded direct image, the pullback of the étale
isomorphism is (7.23).

On the étale site it suffices to bound Tor against constant $A$-modules.
Indeed, for an étale sheaf of $A$-modules $G$ and a geometric point
$\bar x$, the stalk of $Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_AG$ at $\bar x$
is that of $Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_A\underline M$ with
$M=G_{\bar x}$, and geometric stalks are conservative. Now
$K\otimes_A^{\mathbf L}\underline M_U$ has cohomology in $[a,b]$, and
hence the étale version of the right-hand side of
(7.23) lies in $[a,b+d]$. By the projection
formula, so does $Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_A\underline M$, and
therefore $Rj_{\acute{e}t,*}K_{\acute{e}t}$ has Tor amplitude in $[a,b+d]$.

To pass to $X_{\mathrm{pro}\acute{e}t}$, we pull back a bounded flat constructible model
of $Rj_{\acute{e}t,*}K_{\acute{e}t}$ in degrees $[a,b+d]$ [Stacks, Tag 0F4M](https://stacks.math.columbia.edu/tag/0F4M). Its pullback to
$X_{\mathrm{pro}\acute{e}t}$ is again a complex of flat sheaves in degrees $[a,b+d]$, since
pullback preserves flatness. Hence its tensor product with any sheaf of
$A$-modules on $X_{\mathrm{pro}\acute{e}t}$ is computed termwise and lies in degrees
$[a,b+d]$. This covers also the sheaves that are not pulled back from
$X_{\acute{e}t}$, for which the Tor amplitude cannot be read off from geometric
stalks.
