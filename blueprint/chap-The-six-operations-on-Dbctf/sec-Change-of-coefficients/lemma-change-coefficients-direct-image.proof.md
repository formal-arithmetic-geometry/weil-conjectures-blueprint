+++
kind = "proof"
of = "lemma-change-coefficients-direct-image"
order = 637
uses = ["proposition-pro-etale-affines-form-basis", "corollary-continuity-cohomology", "lemma-comparison-completed-coefficients", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "definition-sp-scalar-extension", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
The argument depends on the kind of map $\Lambda\to\Lambda'$. For maps of finite rings we use a projection formula, whereas in the other cases extension of
scalars is either a finite construction (finite sums and a cone), with
which every exact functor commutes, or a filtered colimit, with which
$Rf_*$ commutes on uniformly bounded below systems.

*Maps $A\to B$ of finite rings.* We compute on the étale site using
Proposition [proposition-comparison-etale-derived-category], which
identifies the pro-étale and étale categories in this case, and we test
the comparison on derived sections over quasi-compact étale objects. For a
quasi-compact étale $V\to Y$, we apply the projection formula for constant
coefficients [Stacks, [0F12](https://stacks.math.columbia.edu/tag/0F12)] on both $V$ and $X_V=X\times_YV$ and obtain

$$
R\Gamma(V,(Rf_*K)_B)
\simeq R\Gamma(X_V,K)\otimes_A^{\mathbf L}B
\simeq R\Gamma(X_V,K_B).
$$

Here the first identification uses the projection formula on $V$ and
then $R\Gamma(V,Rf_*K)=R\Gamma(X_V,K)$, and the second is the projection
formula on $X_V$. This projection formula needs only cohomological bounds
for $\ell$-primary coefficients, which hold for schemes of finite type over
$k$, and so it applies to every finite $A$-algebra $B$. Since
these isomorphisms commute with restriction in $V$, the comparison map is
an isomorphism in $D(Y_{\acute{e}t},B)$, and hence, by
Proposition [proposition-comparison-etale-derived-category], in
$D(Y_{\mathrm{pro}\acute{e}t},B)$.

*Maps $\mathcal O_E\to A$ with $A$ finite.* Since $\mathcal O_E$ is a
discrete valuation ring, $A$ has a finite free $\mathcal O_E$-resolution of
length at most one. Its condensed version is again exact. Indeed, a
continuous map from a profinite set to the finite quotient $A$ is constant
on the pieces of a finite clopen partition, and hence lifts to a continuous
map to the free module. The pullback of this resolution to $X$ is a finite free resolution of $A_X$ over
$\mathcal O_{E,X}$. Consequently, tensoring with $A_X$ is computed by finite
sums and a cone, and these commute with the exact functor $Rf_*$.

*Finite extensions.* For $\mathcal O_E\to\mathcal O_F$ and $E\to F$,
the ring $\mathcal O_F$ is free of rank $[F:E]$ over $\mathcal O_E$. Hence
$K_{\mathcal O_F}$ is, as an $\mathcal O_E$-complex, a finite direct sum of
copies of $K$. The assertion follows because $Rf_*$ commutes with finite
sums.

*The maps $\mathcal O_E\to E$ and $E\to\overline{\mathbf Q}_\ell$.* These are not finite,
and we use continuity. For $\mathcal O_E\to E$, the complex $K_E$ is the
colimit of $K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, and for
$E\to\overline{\mathbf Q}_\ell$, the complex $K_{\overline{\mathbf Q}_\ell}$ is the filtered colimit of the $K_F$
over finite extensions $F/E$ in $\overline{\mathbf Q}_\ell$. Since $K$ is bounded, all terms of
these systems are bounded below by a common integer. Hence the colimits
commute with $Rf_*$ by Corollary [corollary-continuity-cohomology].
