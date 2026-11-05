+++
kind = "proof"
of = "det-pe-bounded-continuity-direct-image"
+++
*1.* For an abelian sheaf $M$ on $X_{\mathrm{proét}}$, $R^qf_*M$ is the sheafification of the
presheaf $P_M\colon V\mapsto H^q(X\times_YV,M)$ on $Y_{\mathrm{proét}}$: with an injective
resolution $M\to J^\bullet$, $R^qf_*M=H^q(f_*J^\bullet)$, $(f_*J)(V)=J(X\times_YV)$ (base
change functor of [def-sfb-finite-lower-star]), and cohomology sheaves are
sheafified sectionwise cohomology.

Let $M=\varinjlim_iM_i$. The canonical maps give a map of presheaves
$\varphi\colon\varinjlim_iP_{M_i}\to P_M$ (presheaf colimit). Let $V$ be an affine object of
$Y_{\mathrm{proét}}$. Then $Z=X\times_YV$ is a quasi-compact, quasi-separated object of
$X_{\mathrm{proét}}$, and $H^q(Z,-)$ commutes with filtered colimits: choose a hypercovering
$W_\bullet\to Z$ in which every $W_r$ is the spectrum of a w-contractible ring (cover $Z$, and
inductively the quasi-compact, quasi-separated matching objects, by finitely many affines of
the form of [det-pe-wcb-cover], and take finite disjoint unions, a finite product of
w-contractible rings being w-contractible; Stacks, Tag 09A1). Sections
over each $W_r$ are exact ([det-pe-wc-sections-exact]), so $H^q(Z,N)$ is the $q$-th
cohomology of $N(W_0)\to N(W_1)\to\cdots$, naturally in $N$ ([Stacks, Tag 09A2](https://stacks.math.columbia.edu/tag/09A2)). Each $W_r$ is
affine, hence quasi-compact, so $N\mapsto N(W_r)$ commutes with direct sums ([Stacks, Tag 0935](https://stacks.math.columbia.edu/tag/0935)); being exact, it commutes with all colimits, a colimit being a cokernel of a map between
direct sums. Filtered colimits of abelian groups are exact, so $\varphi(V)$ is an isomorphism.
Every object of $Y_{\mathrm{proét}}$ has a covering by affine objects ([det-pe-wcb-cover]), so
$\varphi$ is locally injective and locally surjective and $\varphi^{\#}$ is an isomorphism.
Sheafification commutes with colimits, so $(\varinjlim_iP_{M_i})^{\#}=\varinjlim_iR^qf_*M_i$,
which proves 1.

*2.* A direct sum $\bigoplus_bM_b$ is the filtered colimit of the finite subsums
$\bigoplus_{b\in F}M_b$ over finite $F\subset B$. The additive functor $R^qf_*$ preserves finite
direct sums, and it preserves this filtered colimit by 1.
