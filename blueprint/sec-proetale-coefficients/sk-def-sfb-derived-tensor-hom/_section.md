+++
id = "sk-def-sfb-derived-tensor-hom"
kind = "definition"
title = "Derived tensor product and derived internal hom"
order = 863
uses = ["sk-def-sfb-derived-categories"]
lean = ["DerivedCategory.hasDerivedMonoidalCategory", "DerivedCategory.monoidalClosed", "AlgebraicGeometry.ProEtale.derivedTensor", "AlgebraicGeometry.ProEtale.isLeftDerivedFunctor₂_derivedTensor", "AlgebraicGeometry.ProEtale.derivedHom", "AlgebraicGeometry.ProEtale.derivedTensorHomAdjunction", "AlgebraicGeometry.ProEtale.derivedTensorHomAdjunction₂", "CategoryTheory.Mod.derivedMonoidalCategory", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensor", "AlgebraicGeometry.ProEtale.CondensedRing.isLeftDerivedFunctor₂_derivedTensor", "CategoryTheory.Mod.isLeftDerivedFunctor₂_curriedTensor", "AlgebraicGeometry.ProEtale.CondensedRing.derivedHom", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction₂"]
tags = ["sketch"]
+++
Let $X$ be a scheme. Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian
category whose tensor product is additive and which has functorial flat resolutions. Let
$\Lambda$ be a commutative condensed ring [sk-def-sfb-condensed-ring] with pulled-back
ring object $\Lambda_X=p_X^*\Lambda$ [sk-def-sfb-pulled-back-coefficients]. The derived
categories are those of [sk-def-sfb-derived-categories].

- **Layer A.** $D(X_{\mathrm{proét}},\mathcal A)$ is monoidal for the *derived tensor
  product* $-\otimes^{\mathrm L}-$. This is the left derived functor, in two variables,
  of the tensor product of complexes of sheaves [sk-def-sfb-sheaf-tensor], computed by
  replacing an argument by a K-flat resolution. The localization functor from complexes
  is lax monoidal.
- **Layer B.** $D(\Mod_{\Lambda_X})$ is monoidal for $-\otimes^{\mathrm L}_{\Lambda_X}-$.
  This is the two-variable K-flat derived functor of the *relative* tensor product
  $\otimes_{\Lambda_X}$ of module objects [sk-prop-sfb-module-category], not a derived
  tensor product over $\mathbf Z$ followed by a quotient.
- **Internal hom.** Both monoidal structures are closed. The *derived internal hom* is
  *defined* as the internal hom of this closed structure. It is a bifunctor
  $\RHom(-,-)\colon D^{\mathrm{op}}\times D\to D$ with
  $K\otimes^{\mathrm L}-\dashv\RHom(K,-)$ for every $K$, naturally in $K$. Likewise there
  is $\RHom_{\Lambda_X}$ with
  $K\otimes^{\mathrm L}_{\Lambda_X}-\dashv\RHom_{\Lambda_X}(K,-)$.
