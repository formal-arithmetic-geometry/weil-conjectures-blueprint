+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--1"
order = 636003
uses = ["definition-derived-base-change-map", "definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--2", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
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
for $\ell$-primary coefficients. These hold for schemes of finite type over
$k$, and so the formula applies to every finite $A$-algebra $B$. Since
these isomorphisms commute with restriction in $V$, the comparison map is
an isomorphism in $D(Y_{\acute{e}t},B)$, and hence, by
Proposition [proposition-comparison-etale-derived-category], in
$D(Y_{\mathrm{pro}\acute{e}t},B)$.

*Source:* the proof of Lemma [lemma-change-coefficients-direct-image].
