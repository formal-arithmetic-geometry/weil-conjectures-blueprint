+++
kind = "proof"
of = "sk-prop-sf-rf-shriek-preservation"
uses = ["sk-cor-sf-direct-image-ctf", "sk-lem-formal-closed-support", "sk-prop-geo-p1-adjunction", "sk-lem-geo-affine-local", "sk-lem-sf-mate", "sk-prop-ctf-finite-proper"]
+++
Locally on $X$ and $Y$, the morphism $f$ is a closed immersion followed by
the projection from an affine space. We therefore treat these two cases and
then glue.

Let $i:Z\hookrightarrow X$ be a closed immersion with open complement
$j:U\hookrightarrow X$, and let $R\underline\Gamma_Z$ be the local cohomology
functor of [sk-lem-formal-closed-support]. For $K\in\Dctf(X,A)$, there is a
triangle

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
      \longrightarrow i_*R\underline\Gamma_ZK[1].
$$

By [sk-cor-sf-direct-image-ctf], the two terms on the right lie in $\Dctf$,
and hence so does $i_*R\underline\Gamma_ZK$. Since $i^*i_*=\mathrm{id}$ and
$i^*$ preserves $\Dctf$, also $R\underline\Gamma_ZK\in\Dctf(Z,A)$. Explicitly,
if $K$ has Tor amplitude in $[a,b]$, then $R\underline\Gamma_ZK$ has Tor
amplitude in $[a,b+\operatorname{cd}_\ell(j)+1]$. Since
$R\underline\Gamma_Z\colon D(X_{\mathrm{proét}},A)\to D(Z_{\mathrm{proét}},A)$
is right adjoint to $i_*$ ([sk-lem-formal-closed-support] (1)) and
$\Loc(\Dctf(-,A))$ is a full subcategory of $D((-)_{\mathrm{proét}},A)$,
uniqueness of right adjoints identifies $R\underline\Gamma_ZK$ with $i^!K$ in
$\Loc(\Dctf(Z,A))$.

For the projection $p:\mathbf A^d_Y\to Y$, we deduce from the adjunction
$Rq_*\dashv q^*(1)[2]$ for the projective line $q:\mathbf P^1_Y\to Y$
([sk-prop-geo-p1-adjunction]) and from [sk-lem-geo-affine-local] that
$p^!\simeq p^*(-)(d)[2d]$ on $\Loc(\Dctf(Y,A))$. This functor preserves
$\Dctf$, since pullback preserves a bounded constructible flat model and the
Tate twist is locally free of rank one.

Finally, after restricting to affine opens in $X$ and $Y$, a morphism of
finite type factors as a closed immersion into an affine space over $Y$
followed by its projection. Since $f^!$ is compatible with composition and
restriction to opens ([sk-lem-sf-mate]), the restriction of $f^!K$ is
obtained by applying the two functors just considered. Hence $f^!K$ is
bounded constructible of finite Tor amplitude locally on $X$, and a finite
affine cover of the quasi-compact scheme $X$ gives a single cohomological
interval and a single interval of Tor amplitude valid everywhere. Since
$Rf_!$ preserves $\Dctf$ by [sk-prop-ctf-finite-proper], both sides of the
adjunction lie in $\Dctf$, and its Hom bijections restrict.
