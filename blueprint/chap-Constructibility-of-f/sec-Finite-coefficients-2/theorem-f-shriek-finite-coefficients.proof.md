+++
kind = "proof"
of = "theorem-f-shriek-finite-coefficients"
order = 594
uses = ["theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-forgetting-supports-composition", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Locally on $X$ and $Y$, the morphism $f$ is a closed immersion followed by
the projection from an affine space. We therefore treat these two cases and
then glue.

*Closed immersions.* Let $i:Z\hookrightarrow X$ be a closed immersion with open
complement $j:U\hookrightarrow X$, and let [$R\underline\Gamma_Z$](@definition-local-cohomology) be the
[local cohomology functor](@definition-local-cohomology) of Section [sec-Extension-by-zero-and-completion]. We show that [$R\underline\Gamma_Z$](@definition-local-cohomology) preserves [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves) and that it is [$i^!$](@theorem-existence-exceptional-inverse-image). For
$K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}$, there is a triangle

$$
i_*\href{@definition-local-cohomology}{R\underline\Gamma_ZK}\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*\href{@definition-local-cohomology}{R\underline\Gamma_ZK}[1].
$$

By Proposition [proposition-open-direct-image-preserves-finite], the two terms on the right lie in
[$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves), and hence so does $i_*\href{@definition-local-cohomology}{R\underline\Gamma_ZK}$. Since
$i^*i_*=\mathrm{id}$ and $i^*$ preserves [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves), we get
$\href{@definition-local-cohomology}{R\underline\Gamma_ZK}\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Z,A)}$. Explicitly, if $K$ has [Tor
amplitude](@definition-constructible-sheaves) in $[a,b]$, then [$R\underline\Gamma_ZK$](@definition-local-cohomology) has [Tor amplitude](@definition-constructible-sheaves) in
$[a,b+\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}+1]$. The functor
$\href{@definition-local-cohomology}{R\underline\Gamma_Z}:D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)\to D(\href{@definition-small-pro-etale-site}{Z_{\mathrm{pro}\acute{e}t}},A)$ is right adjoint
to $i_*$ (Lemma [lemma-sections-support-closed-subscheme](1)), and
[$\Loc(D^b_{\mathrm{ctf}}(-,A))$](@definition-localizing-subcategory) is a full subcategory of $D(\href{@definition-small-pro-etale-site}{(-)_{\mathrm{pro}\acute{e}t}},A)$. By
uniqueness of right adjoints, [$R\underline\Gamma_ZK$](@definition-local-cohomology) is therefore [$i^!K$](@theorem-existence-exceptional-inverse-image) in
[$\Loc(D^b_{\mathrm{ctf}}(Z,A))$](@definition-localizing-subcategory).

*Projections.* Let $p:\mathbf A^d_Y\to Y$ be the projection. From the
adjunction $Rq_*\dashv q^*\href{@definition-tate-twists}{(1)}[2]$ for the projective line
$q:\mathbf P^1_Y\to Y$
(Proposition [proposition-adjunction-projective-line]) and from
Lemma [lemma-affine-space-etale-localization], we deduce that
$\href{@theorem-existence-exceptional-inverse-image}{p^!}\simeq p^*(-)\href{@definition-tate-twists}{(d)}[2d]$ on [$\Loc(D^b_{\mathrm{ctf}}(Y,A))$](@definition-localizing-subcategory). This functor preserves
[$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves), since pullback preserves a bounded [constructible](@definition-constructible-sheaves) flat model and
the [Tate twist](@definition-tate-twists) is locally free of rank one.

For example, for the origin $i:0\hookrightarrow\mathbf A^1$ over $\bar k$
and $K=A$, the triangle gives $\href{@theorem-existence-exceptional-inverse-image}{i^!A}\simeq \href{@definition-tate-twists}{A(-1)}[-2]$
(Example [example-closed-support] below). Its [Tor amplitude](@definition-constructible-sheaves) $[2,2]$ lies in the
predicted interval $[0,0+1+1]$.

*Gluing.* After restricting to affine opens in $X$ and $Y$, a
morphism of finite type factors as a closed immersion into an affine
space over $Y$ followed by its projection. Since [$f^!$](@theorem-existence-exceptional-inverse-image) is compatible
with composition and restriction to opens
(Proposition [proposition-composition-open-restriction-compactifications-f]),
the restriction of [$f^!K$](@theorem-existence-exceptional-inverse-image) is obtained by applying the two functors just
considered. Thus [$f^!K$](@theorem-existence-exceptional-inverse-image) is bounded [constructible](@definition-constructible-sheaves) of [finite Tor amplitude](@definition-constructible-sheaves)
locally on $X$. A finite affine cover of the quasi-compact scheme $X$
gives a single cohomological interval and a single interval of [Tor
amplitude](@definition-constructible-sheaves) valid everywhere. Finally, [$Rf_!$](@proposition-construction-independence-rf-shriek) preserves [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves) by
Proposition [proposition-proper-direct-image-finite-coefficients].
Both sides of the adjunction therefore lie in [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves), and its Hom
bijections restrict.
