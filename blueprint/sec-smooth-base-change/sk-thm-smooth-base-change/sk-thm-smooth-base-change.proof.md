+++
kind = "proof"
of = "sk-thm-smooth-base-change"
uses = ["sk-lem-induction", "sk-prop-deg0", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-lem-universal-datum", "sk-thm-vanishing", "sk-prop-normal-form"]
+++
Since $F$ is classical, $F=\nu_X^*F_{\mathrm{\acute et}}$ for a torsion abelian sheaf
$F_{\mathrm{\acute et}}$ on $X_{\mathrm{\acute et}}$. Since $f$ and $f'$ are qcqs,
[sk-thm-pe-direct-image-comparison] and
[sk-lem-sbc-exchange-compatibility] identify both sides and the
exchange map with the inverse images of their étale models. The proof
below therefore takes place on the étale sites, and in it $g^{-1}$
denotes inverse image of étale sheaves.

Fix an integer $n$ invertible on $Y$. For $r\geq0$, $\mathrm{BC}(g,n,r)$ means: for every
scheme $T$ over $Y$, Noetherian or not and not necessarily of finite type over $k$, every
qcqs morphism $Z\to T$, every sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\mathrm{\acute et}}$,
and every $0\leq i\leq r$, the degree-$i$ exchange map for the square with base change
$Y'\times_YT\to T$ and direct image along $Z\to T$ is an isomorphism
([Stacks, Tag 0F02](https://stacks.math.columbia.edu/tag/0F02)).

The exchange map is local for étale coverings of $Y'$ and of $Y$,
since restriction to an étale object is localization of the site, and
exchange maps compose when two base changes are composed
([Stacks, Tag 0EZR](https://stacks.math.columbia.edu/tag/0EZR),
[Stacks, Tag 0EZS](https://stacks.math.columbia.edu/tag/0EZS)). Both facts hold in each
fixed degree and for the property $\mathrm{BC}(g,n,r)$.
For smooth $g$, étale coordinates
([Stacks, Tag 054L](https://stacks.math.columbia.edu/tag/054L)) give, locally on
$Y'$ and $Y$ and with all schemes affine, a factorization

$$
 Y'\longrightarrow\mathbf A^{d-1}_Y
   \longrightarrow\cdots\longrightarrow\mathbf A^1_Y
   \longrightarrow Y,
$$

whose first arrow is an étale map to $\mathbf A^d_Y$ followed by
projection; each displayed arrow is smooth of relative dimension one.
The case $d=0$ is étale localization. It therefore suffices, in the
induction on the degree, to treat affine $Y$ and $Y'$ with $g$ smooth of
relative dimension one.
Finally, $F$ is the filtered union of the subsheaves $F[n]$, ordered by divisibility of
integers invertible on $Y$. Inverse image commutes with this colimit,
and so do higher direct images along qcqs morphisms
([Stacks, Tag 09Z1](https://stacks.math.columbia.edu/tag/09Z1)).
It therefore suffices to treat $\mathbf Z/n$-modules for each such $n$.

A smooth morphism is flat, locally of finite presentation, and has
geometrically reduced fibres, so degree zero is
[sk-prop-deg0]. Let $q\geq1$ and assume the theorem in
all degrees less than $q$. Fix $n$ invertible on $Y$. Smoothness is
stable under base change, so the induction hypothesis applied after
every base change $T\to Y$ gives $\mathrm{BC}(g,n,q-1)$. By étale
coordinates and composition of exchange maps it suffices to treat $g$
affine and smooth of relative dimension one.

If $\mathrm{BC}(g,n,q)$ failed, [sk-lem-universal-datum]
would give $S$, $C$, $h$ and $d$ with $R^qh_*\underline{\mathbf Z/d}\neq0$,
contradicting [sk-thm-vanishing]. Hence
$\mathrm{BC}(g,n,q)$ holds, and so degree $q$ holds for every smooth $g$
and every sheaf of $\mathbf Z/n$-modules. The filtered union of the
$F[n]$ gives the theorem for $F$, and
[sk-thm-pe-direct-image-comparison] transports the isomorphism and
the exchange map from the étale sites to $Y'_{\mathrm{pro\acute et}}$.

*Complement.* *Negative degrees*: both sides vanish for $q<0$.
*Degree zero*: [sk-prop-deg0] (smooth is flat, of finite
presentation, with geometrically reduced fibres).
*Filtered torsion*: $\mathcal F=\varinjlim_n\mathcal F[n]$
over the integers $n$ invertible on $S$, where $\mathcal F[n]$ is the
$n$-torsion subsheaf; inverse images are left adjoints and
$R^qg_*$, $R^qh_*$ commute with filtered colimits for qcqs $g,h$;
so it suffices to handle sheaves annihilated by a single $n$
invertible on $S$. Such a sheaf is a sheaf of $\Lambda/n\Lambda$-modules, and
the higher direct images and the base-change map of a sheaf of
$\Lambda$-modules are those of its underlying abelian sheaf, hence also those
computed for $\Lambda/n\Lambda$-modules. So it suffices to prove
$\mathrm{BC}(f,\Lambda,q)$ for every $q\ge0$ and every coefficient ring
$\Lambda$ in which some $n$ invertible on $S$ vanishes.
*Reduction to relative dimension one*: the assertion is
étale local on $X$ and $S$; the relative dimension of $f$ is locally
constant, so we may assume it constant, equal to $d$; by [sk-prop-normal-form] one may
assume $X$ and $S$
affine and $X\to S$ factoring as an étale morphism to $\Aaf^d_S$ followed by
the projection; writing $\Aaf^d_S\to \Aaf^{d-1}_S\to\cdots\to\Aaf^1_S\to S$
and using the composition compatibility of the base-change map (and that
étale morphisms satisfy base change trivially), it suffices to prove
the assertion for affine smooth $X\to S$ of relative dimension one
with $X$ affine; $n$ remains invertible on each intermediate base.
*Induction on $q$*: for such $f$, prove by strong induction on $q$ that
$\mathrm{BC}(f,\Lambda,q)$ holds universally. For $q\le0$ this is the
negative-degree and degree-zero cases applied to every base change of $f$
(again smooth). For $q\ge1$, with the statement known universally in all
degrees $<q$, [sk-lem-induction] gives $\mathrm{BC}(f,\Lambda,q)$
universally. Specialising along the identity of $S$ gives
$\mathrm{BC}(f,\Lambda,q)$, and running the filtered colimit back over $n$
finishes the proof.
