+++
id = "det-def-sfb-sheaf-tensor-presheaf"
kind = "definition"
title = "Objectwise tensor product and internal hom of presheaves"
lean = ["CategoryTheory.Monoidal.functorCategoryMonoidal", "CategoryTheory.Monoidal.functorCategorySymmetric", "CategoryTheory.Enriched.FunctorCategory.functorEnrichedHom", "CategoryTheory.MonoidalClosed.FunctorCategory.monoidalClosed", "CategoryTheory.Presheaf.functorEnrichedHomCoyonedaObjEquiv"]
order = 1177
+++
Let $\mathcal A$ be a Grothendieck abelian category with a closed symmetric monoidal structure
$(\otimes,\mathbf 1)$, additive in each variable, with internal hom $\underline{\Hom}_{\mathcal A}$,
so that $\Hom_{\mathcal A}(A\otimes B,C)\cong\Hom_{\mathcal A}(B,\underline{\Hom}_{\mathcal A}(A,C))$.
Let $C$ be a site whose underlying category is essentially small. Write $\mathrm{PSh}(C,\mathcal A)$
for the category of functors $C^{\mathrm{op}}\to\mathcal A$.

1. The *objectwise tensor product* of presheaves $F,G$ is $(F\otimes_pG)(U):=F(U)\otimes G(U)$,
   with restriction maps $F(u)\otimes G(u)$, and its unit is the constant presheaf
   $\underline{\mathbf 1}$. The associator, unitors and symmetry are those of $\mathcal A$, applied
   at each $U$.
2. The *internal hom* of presheaves $F,G$ is the presheaf
   $$
   [F,G](U):=\int_{(V\to U)\in C/U}\underline{\Hom}_{\mathcal A}\bigl(F(V),G(V)\bigr),
   $$
   the end over the slice category $C/U$; a morphism $U'\to U$ acts by restricting along the
   functor $C/U'\to C/U$.

Then $(\mathrm{PSh}(C,\mathcal A),\otimes_p,\underline{\mathbf 1})$ is a closed symmetric monoidal
category: for every object $A$ of $\mathcal A$ and every $U$,
$$
\Hom_{\mathcal A}\bigl(A,[F,G](U)\bigr)\cong\Bigl\{\text{families }\bigl(\varphi_{v}\colon F(V)\otimes A\to G(V)\bigr)_{(v\colon V\to U)\in C/U}\text{ natural in }(V,v)\Bigr\},
$$
and $\Hom(F\otimes_pH,G)\cong\Hom(H,[F,G])$ naturally in $F,G,H$.
