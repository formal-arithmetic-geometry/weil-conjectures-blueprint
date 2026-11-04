+++
id = "theorem-poincare-duality-frobenius"
kind = "theorem"
title = "Poincaré duality and Frobenius"
order = 884
lean = ["AlgebraicGeometry.Etale.TateOrientation.isWeilPairing_poincarePairing", "AlgebraicGeometry.Etale.isWeilPairing_poincarePairing", "AlgebraicGeometry.Etale.TateOrientation.isWeilPairing_untwistedPoincarePairing", "AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing_frobeniusOperator", "AlgebraicGeometry.Etale.TateOrientation.untwistedDegreewisePoincarePairing_frobeniusOperator", "AlgebraicGeometry.Etale.TateOrientation.conj_frobeniusOperator_eq_smul_inverse_dualMap", "AlgebraicGeometry.Etale.TateOrientation.roots_map_charpoly_frobeniusOperator"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
Let $X_0/\mathbf F_q$ be smooth and separated of pure dimension
$d$, let $X=X_0\times\overline{\mathbf F}_q$, and let
$(K,\phi_K)$ be a Weil complex on $X$ (Definition [definition-weil-structure])
with $K$ locally perfect.
Equip the dual with the contragredient Weil structure

$$
\operatorname{Fr}_X^*K^\vee
\simeq(\operatorname{Fr}_X^*K)^\vee
\xrightarrow{\ (\phi_K^{-1})^\vee\ }K^\vee.
$$

For every admissible $\Lambda$ the Poincaré pairing $\beta_K$ of (10.7)
is a morphism of Weil complexes. Thus, with $F$ the Frobenius operators
defined above, the pairing
$H^i_c(X,K)\times H^{2d-i}(X,K^\vee(d))\to\Lambda$ satisfies
$\langle Fx,Fy\rangle=\langle x,y\rangle$, and the pairing
$H^i_c(X,K)\times H^{2d-i}(X,K^\vee)\to\Lambda(-d)$ satisfies

$$
\langle Fx,Fy\rangle=q^d\langle x,y\rangle.
$$

If $\Lambda$ is a field, then $F$ is invertible on $H^i_c(X,K)$, and
with respect to the second pairing $F$ on $H^{2d-i}(X,K^\vee)$ is $q^d$
times the inverse transpose of $F$ on $H^i_c(X,K)$. Hence the two
spaces have the same dimension $b$, the eigenvalues of $F$ on
$H^{2d-i}(X,K^\vee)$ are the $q^d/\alpha$, with multiplicities, where
$\alpha$ ranges over the eigenvalues on $H^i_c(X,K)$, and
$\det(F\mid H^i_c(X,K))\det(F\mid H^{2d-i}(X,K^\vee))=q^{db}$.
