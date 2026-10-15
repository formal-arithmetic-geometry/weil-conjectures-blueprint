+++
kind = "proof"
of = "sk-cor-sf-direct-image-ctf"
uses = ["sk-cor-geo-open-finiteness", "sk-cor-geo-open-finiteness-ii", "sk-cor-pe-finite-tor-comparison", "sk-prop-pe-unbounded-classical"]
+++
Bounded constructibility is [sk-cor-geo-open-finiteness], and
$\operatorname{cd}_\ell(j)$ is finite by [sk-cor-geo-open-finiteness-ii]. For
the Tor amplitude we work on the étale site, where geometric points are
conservative. Write $K=\nu_U^*K_{\mathrm{ét}}$ by
[sk-cor-pe-finite-tor-comparison]; the pro-étale pullback of
$Rj_{\mathrm{ét},*}K_{\mathrm{ét}}\in D(X_{\mathrm{ét}},A)$ is $Rj_*K$, computed
by $Rj_*\colon D(U_{\mathrm{proét}},A)\to D(X_{\mathrm{proét}},A)$, by
[sk-prop-pe-unbounded-classical].

The main step is the scalar projection formula: for every $A$-module $M$, of
arbitrary projective dimension and viewed as a constant sheaf, the projection
morphism is an isomorphism in $D(X_{\mathrm{proét}},A)$

$$
(Rj_*K)\otimes_A^{\mathbf L}\underline M_X
  \xrightarrow{\ \sim\ }
Rj_*\bigl(K\otimes_A^{\mathbf L}\underline M_U\bigr).
\qquad(\ast)
$$

Its étale version, the projection morphism for
$Rj_{\mathrm{ét},*}\colon D(U_{\mathrm{ét}},A)\to D(X_{\mathrm{ét}},A)$, follows
by applying the projection formula of Stacks, Tag
[0F12](https://stacks.math.columbia.edu/tag/0F12) to every quasi-compact étale
$V\to X$ and to $V\times_XU$, both of finite $\ell$-cohomological dimension; the
resulting isomorphisms identify the derived sections of the two sides,
compatibly with the projection morphism. Since inverse image is exact and
symmetric monoidal and commutes with unbounded direct image, the pullback of the
étale isomorphism is $(\ast)$.

The complex $K\otimes_A^{\mathbf L}\underline M_U$ has cohomology in $[a,b]$, so
the étale version of the right side of $(\ast)$ lies in $[a,b+d]$. Taking
geometric stalks gives this Tor bound for every stalk of
$Rj_{\mathrm{ét},*}K_{\mathrm{ét}}$. On the étale site, testing against
constant $A$-modules suffices: tensor product and cohomology commute with the
conservative geometric stalks, and the stalk of any étale module sheaf is an
$A$-module. Hence $Rj_{\mathrm{ét},*}K_{\mathrm{ét}}$ has Tor amplitude in
$[a,b+d]$.

To pass to $X_{\mathrm{proét}}$, pull back a bounded flat constructible model of
$Rj_{\mathrm{ét},*}K_{\mathrm{ét}}$ in degrees $[a,b+d]$ (Stacks, Tag
[0F4M](https://stacks.math.columbia.edu/tag/0F4M)). This gives the same
interval against every pro-étale module sheaf, including nonclassical ones,
for which geometric stalks are not available as a test.
