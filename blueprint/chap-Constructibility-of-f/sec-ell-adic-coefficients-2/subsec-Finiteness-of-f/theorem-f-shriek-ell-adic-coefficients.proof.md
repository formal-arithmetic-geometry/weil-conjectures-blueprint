+++
kind = "proof"
of = "theorem-f-shriek-ell-adic-coefficients"
order = 617
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
