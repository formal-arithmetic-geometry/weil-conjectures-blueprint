+++
id = "det-prop-sfb-module-category"
kind = "proposition"
title = "Structure of $\\Mod_{\\mathcal R}(\\mathcal C)$"
order = 1183
uses = ["det-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.hom_ext", "CategoryTheory.Mod.isLimitKernelFork", "CategoryTheory.Mod.isColimitCokernelCofork", "CategoryTheory.Mod.instAbelian", "CategoryTheory.Mod.createsLimit", "CategoryTheory.Mod.createsColimit", "CategoryTheory.Mod.toBimod", "CategoryTheory.Mod.fullyFaithfulToBimod", "Bimod.IsSymmetric.iso", "Bimod.IsSymmetric.tensorBimod", "CategoryTheory.Mod.monoidalCategory", "CategoryTheory.Mod.symmetricCategory", "CategoryTheory.Mod.braidedCategory", "CategoryTheory.Mod.monoidalClosed", "CategoryTheory.Mod.isGrothendieckAbelian", "CategoryTheory.Mod.hasFunctorialFlatResolution", "CategoryTheory.GrothendieckTopology.isGrothendieckAbelian_sheaf_proEtTopology", "AlgebraicGeometry.ProEtale.sheafMonoidalClosed", "AlgebraicGeometry.ProEtale.hasFunctorialFlatResolution_sheaf", "AddCommGrpCat.hasFunctorialFlatResolution", "AlgebraicGeometry.ProEtale.isCommMonObj_condensedRingObj"]
+++
Let $\mathcal C$ be a monoidal category and $\mathcal R$ a monoid object of $\mathcal C$,
with module objects as in [det-def-sfb-module-objects]. The forgetful functor
$\Mod_{\mathcal R}(\mathcal C)\to\mathcal C$ is faithful.

1. **Abelian structure.** Let $\mathcal C$ be abelian with $\otimes$ additive in each
   variable, and let $\mathcal R\otimes-$ be right exact. Then $\Mod_{\mathcal R}(\mathcal C)$
   is abelian, and kernels and cokernels are computed in $\mathcal C$. More precisely, the
   kernel (cokernel) in $\mathcal C$ of a morphism of module objects carries a unique action
   of $\mathcal R$ that makes it the kernel (cokernel) in $\Mod_{\mathcal R}(\mathcal C)$. The
   forgetful functor is exact.
2. **Relative tensor product.** Let $\mathcal C$ be braided, with braiding $\beta$, and
   have coequalizers. Assume $X\otimes-$ and $-\otimes X$ preserve colimits for every $X$,
   and let $\mathcal R$ be commutative. Every $\mathcal R$-module object $M$ is then also a
   right module, via $\gamma_M\circ\beta_{M,\mathcal R}\colon M\otimes\mathcal R\to M$. This
   identifies $\Mod_{\mathcal R}(\mathcal C)$ with a full subcategory of the
   $\mathcal R$-$\mathcal R$-bimodules, the *symmetric* bimodules. The *relative tensor
   product* is the coequalizer
   $$
   M\otimes_{\mathcal R}N:=\operatorname{coeq}\Bigl(M\otimes\mathcal R\otimes N
   \rightrightarrows M\otimes N\Bigr)
   $$
   of $(\gamma_M\beta_{M,\mathcal R})\otimes N$ and
   $(M\otimes\gamma_N)\circ\alpha_{M,\mathcal R,N}$, with $\mathcal R$ acting through $M$.
   It makes $\Mod_{\mathcal R}(\mathcal C)$ a monoidal category with unit $\mathcal R$. If
   $\mathcal C$ is symmetric, the braiding of $\mathcal C$ descends to $\otimes_{\mathcal R}$
   and makes $\Mod_{\mathcal R}(\mathcal C)$ symmetric monoidal.
3. **Closed Grothendieck structure.** Let $\mathcal C$ be a closed symmetric monoidal
   Grothendieck abelian category with $\otimes$ additive in each variable, and let
   $\mathcal R$ be commutative. Then $\Mod_{\mathcal R}(\mathcal C)$, with
   $\otimes_{\mathcal R}$, is a closed symmetric monoidal Grothendieck abelian category.
   Call an object $F$ *flat* if $F\otimes-$ and $-\otimes F$ are exact. A *functorial flat
   resolution* is a functor $P$ to flat objects with a natural epimorphism $P(M)\to M$. If
   $\mathcal C$ has one, so does $\Mod_{\mathcal R}(\mathcal C)$, given by
   $$
   \mathcal R\otimes P(M)\to\mathcal R\otimes M\xrightarrow{\gamma_M}M .
   $$
4. **Sheaves of modules.** In particular, let $\Lambda$ be a commutative condensed ring
   and $X$ a scheme. Then $\Mod_{\Lambda_X}$ is a closed symmetric monoidal Grothendieck
   abelian category with unit $\Lambda_X$ and functorial flat resolutions. Its forgetful
   functor to $\Sh(X_{\mathrm{proét}},\Ab)$ is exact and faithful.
