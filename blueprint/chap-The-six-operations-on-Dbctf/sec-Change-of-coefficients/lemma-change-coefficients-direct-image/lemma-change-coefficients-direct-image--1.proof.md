+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--1"
order = 636003
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
