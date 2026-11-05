+++
kind = "proof"
of = "theorem-f-shriek-ell-adic-coefficients"
order = 617
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
