+++
id = "definition-frobenius-correspondences-their-operators--5"
kind = "definition"
title = "Frobenius correspondences and their operators (5)"
name_showing = false
order = 952006
aliases = ["bp-r289-5"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator_ofGraph", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ofGraph", "AlgebraicGeometry.ProEtale.CondensedRing.compactPullback", "AlgebraicGeometry.ProEtale.CondensedRing.frobeniusCompactOperator", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator_frobeniusGraph", "AlgebraicGeometry.Etale.frobeniusCompactOperator", "AlgebraicGeometry.Etale.lowerShriekPullback", "AlgebraicGeometry.ProEtale.StrictWeilComplex.globalFrobenius"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--6", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-underived-base-change-map--1", "theorem-proper-base-change-classical-pro--2", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--7", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--3", "proposition-composition-base-change-rf-shriek--7", "proposition-forgetting-supports-composition--3", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-weil-structure--2", "definition-frobenius-operator--1", "definition-correspondence--2", "definition-action-correspondence--1", "definition-frobenius-correspondences-their-operators--4", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $c_m=(\operatorname{id}_X,\Phi_X^m):X\to X\times_sX$ be the graph
of $\Phi_X^m$. Since its first leg is the identity, $\psi_m$ is a
cohomological correspondence on $(X,K)$ for $c_m$. Its operator on
cohomology with compact support
(Definition [definition-action-correspondence]) is the endomorphism

$$
T_{c_m}(\psi_m)
=R\Gamma_c(X,\psi_m)\circ(\Phi_X^m)^*,
$$

where $(\Phi_X^m)^*:R\Gamma_c(X,K)\to R\Gamma_c(X,(\Phi_X^m)^*K)$ is the
pullback map induced by the unit of $(\Phi_X^m)^*\dashv R(\Phi_X^m)_*$.
