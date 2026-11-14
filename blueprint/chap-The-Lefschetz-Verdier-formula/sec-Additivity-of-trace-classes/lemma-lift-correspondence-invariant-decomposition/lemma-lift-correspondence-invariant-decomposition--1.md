+++
id = "lemma-lift-correspondence-invariant-decomposition--1"
kind = "lemma"
title = "Lifting a correspondence to an invariant decomposition (1)"
name_showing = false
order = 937001
aliases = ["bp-r285-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.openPieceCoeff_comp_map_counit", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.eq_openPieceCoeff_of_comp_map_counit", "AlgebraicGeometry.ProEtale.CondensedRing.homEquiv_symm_restrictedCoeffOfIsPullback", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointOpenPieceCoeff_comp_map_counit"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-correspondence--2", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $c:C\to X\times X$ be a correspondence, $i:Z\to X$ a closed
immersion with open complement $j:U\to X$, and suppose

$$
c_1^{-1}(Z)\subset c_2^{-1}(Z),
\qquad\text{equivalently }c_2^{-1}(U)\subset c_1^{-1}(U).
$$

Let $u$ be a cohomological correspondence on $(X,K)$, and write
$K_U=j_!j^*K$ and $K_Z=Ri_*i^*K$ for the two pieces of the localization
triangle $K_U\to K\to K_Z$. Then $u$ has a lift, unique up to
contractible choice, to a cohomological correspondence $\tilde u$ in the
filtered derived category on the two-step filtered complex given by this
triangle. Its graded pieces are cohomological correspondences $u_U$ on
$(X,K_U)$ and $u_Z$ on $(X,K_Z)$, and $\widehat u_Z$ restricted to $Z$ is

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*\Theta K
\xrightarrow{i^*\widehat u}i^*K.
$$
