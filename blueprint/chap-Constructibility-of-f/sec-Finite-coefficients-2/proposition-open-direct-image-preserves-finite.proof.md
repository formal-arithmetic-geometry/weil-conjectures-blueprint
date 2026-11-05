+++
kind = "proof"
of = "proposition-open-direct-image-preserves-finite"
order = 591
uses = ["proposition-etale-implications", "proposition-pro-etale-affines-form-basis", "theorem-comparison-direct-images", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
We test Tor amplitude by tensoring with modules. By a projection formula
for constant modules we may move the tensor product inside $Rj_*$. There
the complex $K\otimes^{\mathbf L}\underline M$ has amplitude $[a,b]$, and
$Rj_*$ adds at most $d$ degrees.

The complex $Rj_*K$ is bounded constructible by
Corollary [corollary-open-direct-image-over-field], and $\operatorname{cd}_\ell(j)$ is finite
by Theorem [theorem-results-from-etale-theory](3). To bound
the Tor amplitude, we work on the étale site, where geometric points are
conservative. By
Corollary [corollary-finite-tor-amplitude-under-comparison], we have
$K\simeq\nu_U^*K_{\acute{e}t}$ for some
$K_{\acute{e}t}\in D^b_{\mathrm{ctf}}(U_{\acute{e}t},A)$. By
Proposition [proposition-unbounded-comparison-finite-coefficients], the
pro-étale pullback of $Rj_{\acute{e}t,*}K_{\acute{e}t}$ is $Rj_*K$.

We first prove the projection formula for constant coefficients. Namely,
for every $A$-module $M$, viewed as a constant sheaf, the projection
morphism

$$
(Rj_*K)\otimes_A^{\mathbf L}\underline M_X
\xrightarrow{\ \sim\ }
Rj_*\bigl(K\otimes_A^{\mathbf L}\underline M_U\bigr)
\tag{6.23}
$$

is an isomorphism. Recall that for a scheme $V$
with $\operatorname{cd}_\ell(V)<\infty$, the projection formula of
[Stacks, [0F12](https://stacks.math.columbia.edu/tag/0F12)] identifies
$R\Gamma(V,K)\otimes^{\mathbf L}_AM$ with
$R\Gamma(V,K\otimes^{\mathbf L}_A\underline M)$. Moreover, a map of complexes of sheaves is an isomorphism if it induces isomorphisms on derived
sections over a basis of the site. Since the sections of $Rj_*$ over $V$ are the sections over $V\times_XU$, we apply the projection formula to
every quasi-compact étale $V\to X$ and to $V\times_XU$. This gives
isomorphisms between the derived sections of the two sides of the étale
version of (6.23), compatibly with the
projection morphism. Hence the étale version holds. Finally, inverse image is exact and symmetric monoidal, and it commutes with unbounded direct image, so the pullback of the étale isomorphism is
(6.23).

On the étale site it suffices to bound Tor against constant $A$-modules.
Indeed, let $G$ be an étale sheaf of $A$-modules and $\bar x$ a geometric
point. The stalk of $Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_AG$ at $\bar x$
is that of $Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_A\underline M$ with
$M=G_{\bar x}$, and geometric stalks are conservative. Now
$K\otimes_A^{\mathbf L}\underline M_U$ has cohomology in $[a,b]$. Hence the
étale version of the right-hand side of
(6.23) lies in $[a,b+d]$. By the
projection formula, so does
$Rj_{\acute{e}t,*}K_{\acute{e}t}\otimes^{\mathbf L}_A\underline M$. In other words,
$Rj_{\acute{e}t,*}K_{\acute{e}t}$ has Tor amplitude in $[a,b+d]$.

To pass to $X_{\mathrm{pro}\acute{e}t}$, we pull back a bounded flat constructible model
of $Rj_{\acute{e}t,*}K_{\acute{e}t}$ in degrees $[a,b+d]$ [Stacks, [0F4M](https://stacks.math.columbia.edu/tag/0F4M)]. Since pullback
preserves flatness, its pullback to $X_{\mathrm{pro}\acute{e}t}$ is again a complex of flat
sheaves in degrees $[a,b+d]$. Hence its tensor product with any sheaf of
$A$-modules on $X_{\mathrm{pro}\acute{e}t}$ is computed termwise and lies in degrees
$[a,b+d]$. This argument also covers the sheaves on $X_{\mathrm{pro}\acute{e}t}$ that are not pulled
back from $X_{\acute{e}t}$, for which geometric stalks would not detect the Tor amplitude.
