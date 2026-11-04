+++
kind = "proof"
of = "theorem-f-shriek-finite-coefficients"
order = 587
uses = ["lemma-stability", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "corollary-cohomology-geometric-fibres", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "example-closed-support", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Locally on $X$ and $Y$, the morphism $f$ is a closed immersion followed by
the projection from an affine space. We therefore treat these two cases and
then glue.

*Closed immersions.* Let $i:Z\hookrightarrow X$ be a closed immersion with open
complement $j:U\hookrightarrow X$, and let $R\underline\Gamma_Z$ be the
local cohomology functor of Section [sec-Extension-by-zero-and-completion]. We show
that $R\underline\Gamma_Z$ preserves $D^b_{\mathrm{ctf}}$ and that it is $i^!$. For
$K\in D^b_{\mathrm{ctf}}(X,A)$, there is a triangle

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*R\underline\Gamma_ZK[1].
$$

By Proposition [proposition-open-direct-image-preserves-finite], the two terms on the right lie in
$D^b_{\mathrm{ctf}}$, and hence so does $i_*R\underline\Gamma_ZK$. Since
$i^*i_*=\mathrm{id}$ and $i^*$ preserves $D^b_{\mathrm{ctf}}$, we get
$R\underline\Gamma_ZK\in D^b_{\mathrm{ctf}}(Z,A)$. Explicitly, if $K$ has Tor
amplitude in $[a,b]$, then $R\underline\Gamma_ZK$ has Tor amplitude in
$[a,b+\operatorname{cd}_\ell(j)+1]$. The functor
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},A)\to D(Z_{\mathrm{pro}\acute{e}t},A)$ is right adjoint
to $i_*$ (Lemma [lemma-sections-support-closed-subscheme](1)), and
$\Loc(D^b_{\mathrm{ctf}}(-,A))$ is a full subcategory of $D((-)_{\mathrm{pro}\acute{e}t},A)$. By
uniqueness of right adjoints, $R\underline\Gamma_ZK$ is therefore $i^!K$ in
$\Loc(D^b_{\mathrm{ctf}}(Z,A))$.

*Projections.* Let $p:\mathbf A^d_Y\to Y$ be the projection. From the
adjunction $Rq_*\dashv q^*(1)[2]$ for the projective line
$q:\mathbf P^1_Y\to Y$
(Proposition [proposition-adjunction-projective-line]) and from
Lemma [lemma-affine-space-etale-localization], we deduce that
$p^!\simeq p^*(-)(d)[2d]$ on $\Loc(D^b_{\mathrm{ctf}}(Y,A))$. This functor preserves
$D^b_{\mathrm{ctf}}$, since pullback preserves a bounded constructible flat model and
the Tate twist is locally free of rank one.

For example, for the origin $i:0\hookrightarrow\mathbf A^1$ over $\bar k$
and $K=A$, the triangle gives $i^!A\simeq A(-1)[-2]$
(Example [example-closed-support] below). Its Tor amplitude $[2,2]$ lies in the
predicted interval $[0,0+1+1]$.

*Gluing.* After restricting to affine opens in $X$ and $Y$, a
morphism of finite type factors as a closed immersion into an affine
space over $Y$ followed by its projection. Since $f^!$ is compatible
with composition and restriction to opens
(Proposition [proposition-composition-open-restriction-compactifications-f]),
the restriction of $f^!K$ is obtained by applying the two functors just
considered. Thus $f^!K$ is bounded constructible of finite Tor amplitude
locally on $X$. A finite affine cover of the quasi-compact scheme $X$
gives a single cohomological interval and a single interval of Tor
amplitude valid everywhere. Finally, $Rf_!$ preserves $D^b_{\mathrm{ctf}}$ by
Proposition [proposition-proper-direct-image-finite-coefficients].
Both sides of the adjunction therefore lie in $D^b_{\mathrm{ctf}}$, and its Hom
bijections restrict.
