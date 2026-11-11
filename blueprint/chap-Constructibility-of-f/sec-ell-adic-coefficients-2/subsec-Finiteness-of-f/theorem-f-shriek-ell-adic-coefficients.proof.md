+++
kind = "proof"
of = "theorem-f-shriek-ell-adic-coefficients"
order = 617
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "lemma-descent-finite-coefficient-field", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-comparison-etale-derived-category", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "corollary-open-direct-image-over-field", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "lemma-uniqueness-maps-dense-open", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
As for finite coefficients, we factor $f$ locally into a closed
immersion and a projection from affine space, and treat the two factors
separately.

Choose finite affine covers of $X$ and $Y$ and closed immersions
$U\hookrightarrow\mathbf A^d_V$. Here $u:U\to X$ and $v:V\to Y$ are the
inclusions of the affine opens, and $i:U\hookrightarrow\mathbf A^d_V$ and
$p:\mathbf A^d_V\to V$ are the two factors. Then $u^*f^!\simeq i^!p^!v^*$
(Proposition [proposition-composition-open-restriction-compactifications-f]), and being in $\Dbc$ is local
on $X$, so it suffices to show that $p^!$ and $i^!$ preserve $\Dbc$.

For $E$ and $\overline{\mathbf Q}_\ell$ we argue as in Section [sec-Finite-coefficients-2]. For $p$ we use Proposition [proposition-projective-line-rational-coefficients], the adjunction $j_!\dashv j^*$ for $\mathbf A^1_V\subset\mathbf P^1_V$, and
Proposition [proposition-composition-open-restriction-compactifications-f]
applied $d$ times. They give $p^!\simeq p^*(d)[2d]$, which preserves
$\Dbc$. For $i$, let $j'$ be the inclusion of the open complement of $U$ in
$\mathbf A^d_V$. Then the localization triangle before Example [example-closed-support], with $j'$ in place of $j$, shows that
$i^!K\in\Dbc(U,\Lambda)$ for $K\in\Dbc(\mathbf A^d_V,\Lambda)$. Indeed, its
third term $Rj'_*j'^*K$ is in $\Dbc$ by
Proposition [proposition-direct-image-along-open-immersion], and
$i^*i_*=\mathrm{id}$.

For $\mathcal O_E$ that argument applies once its ingredients are
available with integral coefficients. They are as follows. First, the adjunction for the projective line comes from
Proposition [proposition-ell-adic-cycle-class-diagonal], with the
triangle identities verified as in
Proposition [proposition-projective-line-rational-coefficients]. Next, the projection formula is Lemma [lemma-projection-formula-integral-coefficients], and inverse image and tensor product preserve $\Dbc(-,\mathcal O_E)$ by
Lemma [lemma-inverse-image-tensor-product]. Moreover, the finiteness of $Rj_*$ and proper base change are Propositions [proposition-direct-image-along-open-immersion]
and [proposition-proper-base-change-localizing-categories]. We also
use that derived completeness is local on $X$; it is part of the criterion
for $\Dbc$ with $\mathcal O_E$-coefficients. Finally, $Rf_!$ preserves
$\Dbc$ (Proposition [proposition-construction-independence-rf-shriek]),
and so the adjunction restricts to $\Dbc$.
