+++
id = "det-def-sfb-sheaf-tensor-structure"
kind = "definition"
title = "The symmetric monoidal structure on $\\mathcal A$-valued sheaves"
lean = ["CategoryTheory.Sheaf.monoidalCategory", "CategoryTheory.Sheaf.braidedCategory", "CategoryTheory.Sheaf.symmetricCategory", "CategoryTheory.GrothendieckTopology.monoidalCategory_sheaf_of_essentiallySmall", "CategoryTheory.GrothendieckTopology.symmetricCategory_sheaf_of_essentiallySmall", "AddCommGrpCat.monoidalCategory"]
order = 1136
uses = ["det-def-sfb-sheaf-tensor-local-iso", "def-weil-pbc-proetale-site", "det-def-sfb-sheaf-tensor-presheaf"]
+++
Let $\mathcal A$ and $C$ be as in [det-def-sfb-sheaf-tensor-presheaf]; for instance $C$ is the
small pro-étale site $X_{\mathrm{proét}}$ of a scheme ([def-weil-pbc-proetale-site]) or the
category of profinite sets with the coherent topology, and $\mathcal A=\Ab$ with
$\otimes_{\mathbf Z}$ and unit $\mathbf Z$, or $\mathcal A=\Mod_R$ for a commutative ring $R$.
For sheaves $\mathcal F,\mathcal G,\mathcal H$ define:

- the *tensor product* $\mathcal F\otimes\mathcal G:=a(\mathcal F\otimes_p\mathcal G)$, with
  $a$ sheafification, and on morphisms $a(\varphi\otimes_p\psi)$;
- the *unit* $\mathbf 1_{\Sh}:=a(\underline{\mathbf 1})$;
- the *associator*
  $(\mathcal F\otimes\mathcal G)\otimes\mathcal H\cong\mathcal F\otimes(\mathcal G\otimes\mathcal H)$
  as the composite
  $$
  a\bigl(a(\mathcal F\otimes_p\mathcal G)\otimes_p\mathcal H\bigr)\cong a\bigl((\mathcal F\otimes_p\mathcal G)\otimes_p\mathcal H\bigr)\xrightarrow{a(\alpha)}a\bigl(\mathcal F\otimes_p(\mathcal G\otimes_p\mathcal H)\bigr)\cong a\bigl(\mathcal F\otimes_pa(\mathcal G\otimes_p\mathcal H)\bigr),
  $$
  where $\alpha$ is the objectwise associator and the outer isomorphisms are $a$ applied to the
  maps $\eta\otimes_p\mathcal H$, $\mathcal F\otimes_p\eta$ (units of $a$), which are invertible
  after $a$ by [det-def-sfb-sheaf-tensor-local-iso];
- the *unitors* and the *symmetry* in the same way from the objectwise ones and the unit maps
  $\underline{\mathbf 1}\to a(\underline{\mathbf 1})$.

Then $(\Sh(C,\mathcal A),\otimes,\mathbf 1_{\Sh})$ is a symmetric monoidal category, and
sheafification $a\colon(\mathrm{PSh}(C,\mathcal A),\otimes_p)\to(\Sh(C,\mathcal A),\otimes)$ is
strong symmetric monoidal, with structure isomorphisms
$a(F)\otimes a(G)=a(aF\otimes_paG)\cong a(F\otimes_pG)$ and
$\mathbf 1_{\Sh}=a(\underline{\mathbf 1})$. For $\mathcal A=\Ab$, $\mathcal F\otimes\mathcal G$ is the
sheafified objectwise $\otimes_{\mathbf Z}$ and the unit is the constant sheaf
$\underline{\mathbf Z}$.
