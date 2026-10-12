+++
id = "sk-def-sfb-sheaf-tensor"
kind = "definition"
title = "Tensor product of pro-étale sheaves"
order = 1452
uses = ["def-weil-pbc-proetale-site", "sec-picard-framework"]
lean = ["CategoryTheory.Sheaf.monoidalCategory", "AlgebraicGeometry.ProEtale.sheafMonoidalCategory", "AlgebraicGeometry.ProEtale.sheafSymmetricCategory", "AlgebraicGeometry.ProEtale.sheafMonoidalClosed", "AlgebraicGeometry.ProEtale.preservesColimitsOfSize_tensorLeft_sheaf", "AddCommGrpCat.monoidalCategory", "AddCommGrpCat.monoidalClosed"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category with a closed symmetric monoidal
structure $(\otimes,\mathbf 1)$. Examples are $\mathcal A=\Mod_R$ for a commutative
ring $R$, and $\mathcal A=\Ab$ with the tensor product $M\otimes N=M\otimes_{\mathbf Z}N$,
unit $\mathbf Z$ and internal hom the group $\Hom(M,N)$. For $\Ab$ this is the monoidal
structure used throughout, *not* the cartesian one.

Let $C$ be a site whose underlying category is essentially small, relative to the size of
the morphism groups of $\mathcal A$. Examples are the small pro-étale site
$X_{\mathrm{proét}}$ of a scheme $X$ ([def-weil-pbc-proetale-site]) and the category of
profinite sets with the coherent topology. Write $\Sh(C,\mathcal A)$ for the category of
$\mathcal A$-valued sheaves on $C$ and $a$ for sheafification.

The *tensor product* of $\mathcal F,\mathcal G\in\Sh(C,\mathcal A)$ is the sheafification
of the objectwise tensor product,

$$
\mathcal F\otimes\mathcal G:=a\bigl(U\longmapsto\mathcal F(U)\otimes\mathcal G(U)\bigr),
$$

with unit the sheafified constant presheaf $a(\underline{\mathbf 1})$. Then:

1. this is a symmetric monoidal structure on $\Sh(C,\mathcal A)$, and sheafification from
   $\mathcal A$-valued presheaves with the objectwise tensor product is a strong symmetric
   monoidal functor;
2. the structure is closed: every functor $\mathcal F\otimes-$ has a right adjoint
   $\mathcal{H}om(\mathcal F,-)$. Hence $\mathcal F\otimes-$ and $-\otimes\mathcal F$
   preserve colimits, and in particular they are right exact.

For $\mathcal A=\Ab$, the tensor product of abelian sheaves is the sheafified objectwise
$\otimes_{\mathbf Z}$, with unit the constant sheaf $\underline{\mathbf Z}$.
