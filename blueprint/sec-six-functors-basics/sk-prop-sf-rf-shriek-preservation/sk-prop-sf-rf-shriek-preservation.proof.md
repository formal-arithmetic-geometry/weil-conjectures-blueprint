+++
kind = "proof"
of = "sk-prop-sf-rf-shriek-preservation"
uses = ["sk-lem-formal-closed-support", "sk-cor-sf-direct-image-ctf", "sk-prop-geo-p1-adjunction", "sk-lem-geo-affine-local", "sk-prop-cohsm", "sk-prop-ctf-finite-proper"]
+++
Locally on $X$ and $Y$, $f$ is a closed immersion followed by the projection
from an affine space, so we treat these two cases and then glue.

Let $i:Z\hookrightarrow X$ be a closed immersion with open complement
$j:U\hookrightarrow X$, and let $R\underline\Gamma_Z$ be as in
[sk-lem-formal-closed-support], so that for $K\in\Dctf(X,A)$ there is a
triangle in $D(X_{\mathrm{proét}},A)$

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
      \longrightarrow i_*R\underline\Gamma_ZK[1].
$$

By [sk-cor-sf-direct-image-ctf] the two right-hand terms lie in $\Dctf$, hence
so does $R\underline\Gamma_ZK$; explicitly, a Tor interval $[a,b]$ for $K$
gives the interval $[a,b+\operatorname{cd}_\ell(j)+1]$ for
$R\underline\Gamma_ZK$. Since
$R\underline\Gamma_Z\colon D(X_{\mathrm{proét}},A)\to D(Z_{\mathrm{proét}},A)$
is right adjoint to $i_*$ ([sk-lem-formal-closed-support] (1)) and
$\Loc(\Dctf(-,A))$ is a full subcategory of $D((-)_{\mathrm{proét}},A)$,
uniqueness of right adjoints identifies $R\underline\Gamma_ZK$ with $i^!K$ in
$\Loc(\Dctf(Z,A))$.

For the projection $a:\mathbf A^d_Y\to Y$, the projective-line adjunction
$Rq_*\dashv q^*(1)[2]$ of [sk-prop-geo-p1-adjunction] and
[sk-lem-geo-affine-local] give $a^!=a^*(d)[2d]$ as functors
$\Loc(\Dctf(Y,A))\to\Loc(\Dctf(\mathbf A^d_Y,A))$. This functor preserves
$\Dctf$, because pullback preserves a bounded constructible flat model and the
Tate twist is locally free of rank one. More generally, [sk-prop-cohsm] proves
the same for smooth morphisms, whose dualizing complexes are locally an
invertible sheaf shifted by $2d$.

Finally, after restricting to affine opens in $X$ and $Y$, a finite-type
morphism factors as a closed immersion into an affine space over $Y$ followed
by its projection. Composition and open locality of the adjunction identify the
restriction of $f^!K$ with the composite of the two functors just considered,
so $f^!K$ is bounded constructible of finite Tor amplitude locally on $X$. A
finite affine cover of the quasi-compact scheme $X$ gives one cohomological
interval and one Tor interval valid everywhere. Since $Rf_!$ preserves $\Dctf$
by [sk-prop-ctf-finite-proper], both sides of the adjunction lie in $\Dctf$, and
its Hom bijections restrict.
