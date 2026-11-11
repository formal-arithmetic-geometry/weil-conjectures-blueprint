+++
kind = "proof"
of = "theorem-f-shriek-ell-adic-coefficients--2"
order = 616005
uses = ["proposition-pro-etale-affines-form-basis", "definition-derived-base-change-map", "lemma-finite-cover-projective-space", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-picard-scheme-jacobian-over-separably", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-exact-products--2", "proposition-milnor-sequence--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "lemma-reduction-derived-nakayama--3", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-descent-finite-coefficient-field--3", "lemma-integral-models--3", "proposition-inverting-ell--2", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--2", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "corollary-cohomology-geometric-fibres--2", "proposition-comparison-etale-derived-category--5", "lemma-inverse-image-tensor-product--3", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--1", "proposition-composition-open-restriction-compactifications-f--4", "proposition-exceptional-inverse-image-smooth-morphism--4", "corollary-open-direct-image-over-field--1", "proposition-sp-unique-adjoint--1", "definition-sp-scalar-extension--2", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-uniqueness-maps-dense-open--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--3", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
Take $\Lambda=E$.

Choose finite affine covers of $X$ and $Y$ and closed immersions
$U\hookrightarrow\mathbf A^d_V$. Here $u:U\to X$ and $v:V\to Y$ are the
inclusions of the affine opens, and $i:U\hookrightarrow\mathbf A^d_V$ and
$p:\mathbf A^d_V\to V$ are the two factors. Then $u^*f^!\simeq i^!p^!v^*$
(Proposition [proposition-composition-open-restriction-compactifications-f]), and being in $\Dbc$ is local
on $X$, so it suffices to show that $p^!$ and $i^!$ preserve $\Dbc$.

For $E$ and $\overline{\mathbf Q}_\ell$ we argue as in Section [sec-Finite-coefficients-2]. We use
Proposition [proposition-projective-line-rational-coefficients], the
adjunction $j_!\dashv j^*$ for $\mathbf A^1_V\subset\mathbf P^1_V$, and
Proposition [proposition-composition-open-restriction-compactifications-f]
applied $d$ times. They give $p^!\simeq p^*(d)[2d]$, which preserves
$\Dbc$. For $i$, let $j'$ be the inclusion of the open complement of $U$ in
$\mathbf A^d_V$. The localization triangle before
Example [example-closed-support], with $j'$ in place of $j$, shows that
$i^!K\in\Dbc(U,\Lambda)$ for $K\in\Dbc(\mathbf A^d_V,\Lambda)$. Indeed, its
third term $Rj'_*j'^*K$ is in $\Dbc$ by
Proposition [proposition-direct-image-along-open-immersion], and
$i^*i_*=\mathrm{id}$.

*Source:* the proof of Theorem [theorem-f-shriek-ell-adic-coefficients].
