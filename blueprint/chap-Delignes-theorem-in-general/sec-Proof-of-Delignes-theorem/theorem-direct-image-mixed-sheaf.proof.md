+++
kind = "proof"
of = "theorem-direct-image-mixed-sheaf"
order = 1356
+++
Say that a morphism has the property if the conclusion holds for it,
for every $w$ and every mixed $F$ of weights at most $w$. Quasi-finite
maps and projections of relative affine lines have the property, and by
Lemma [lemma-relative-noether-normalization-over-stratification]
every $f$ is built from these two kinds of maps. So it suffices to show
that the property is stable under composition and under finite partitions.

For composition, let $X_0\xrightarrow{h}Z_0\xrightarrow{g}Y_0$ and consider the Leray
spectral sequence for compact supports,

$$
E_2^{a,b}=R^ag_!(R^bh_!F)\ \Longrightarrow\ R^{a+b}(gh)_!F.
$$

It is Frobenius-equivariant by the naturality of the truncation tower
and of the composition isomorphism for direct image with compact
support. If both maps have the property, then $E_2^{a,b}$ is mixed of
weights at most $w+a+b$. Since each later page is a subquotient of the
previous one, the same holds for $E_\infty^{a,b}$. The abutment
filtration of $R^n(gh)_!F$ is finite, because the operations preserve
bounded constructible complexes. Its quotients are the
$E_\infty^{a,n-a}$, and by Lemma [lemma-weights-exact-sequence]
$R^n(gh)_!F$ is mixed of weights at most $w+n$.

For partitions, we apply Lemma [lemma-relative-noether-normalization-over-stratification] and refine the
partitions to filtrations by open and closed pieces. After this
refinement we can order the pieces so that each is open in the union
of itself and the later ones. This lets us apply the localization
sequences one piece at a time. The restriction
of $F$ to each source piece is again mixed of weights at most $w$. On
every refined source piece, the finite map to $\mathbf A^d_V$ restricts
to a separated quasi-finite map, which has the property by
Lemma [lemma-finite-quasi-finite-direct-images]. The projection
$\mathbf A^d_V\to V$ is a composition of $d$ projections of relative
affine lines. Each of them has the property by
Proposition [proposition-relative-affine-line], and by the
composition argument the map from the piece to $V$ has the property.
We assemble the pieces one at a time in the chosen order. By
Lemma [lemma-weight-bounds-partitions](1) on the source and
Lemma [lemma-weight-bounds-partitions](2) on the target, the bound
for the pieces implies the bound for $R^if_!F$ on $Y_0$.
