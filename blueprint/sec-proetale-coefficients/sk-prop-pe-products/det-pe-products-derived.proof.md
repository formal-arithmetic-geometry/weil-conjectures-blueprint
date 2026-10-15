+++
kind = "proof"
of = "det-pe-products-derived"
+++
*Cohomology.* $H^p(K)=\ker(d^p)/\operatorname{im}(d^{p-1})$ is built from kernels and
cokernels. Products always commute with kernels, and they commute with cokernels and
images because they are exact ([det-pe-products-exact]). Hence
$H^p(\prod_iK_i)=\prod_iH^p(K_i)$, naturally in the family. In particular a product of
quasi-isomorphisms is a quasi-isomorphism, and a product of acyclic complexes is acyclic.

*Product in $D$.* The category of $\mathcal R$-modules is Grothendieck, so each $K_i$ has a
K-injective resolution $K_i\to I_i$ (Stacks, Tag 079P). The termwise product
$\prod_iI_i$ is K-injective: for an acyclic complex $C$,
$\Hom_{K}(C,\prod_iI_i)=\prod_i\Hom_K(C,I_i)=0$, as products in the homotopy category
are termwise. For any complex $C$, using that maps into K-injective complexes in $D$ are
computed in the homotopy category,

$$
\Hom_D\Bigl(C,\prod_iI_i\Bigr)=\Hom_K\Bigl(C,\prod_iI_i\Bigr)=\prod_i\Hom_K(C,I_i)
=\prod_i\Hom_D(C,I_i)=\prod_i\Hom_D(C,K_i),
$$

so $\prod_iI_i$ is a product of the $K_i$ in $D$. By the first paragraph
$\prod_iK_i\to\prod_iI_i$ is a quasi-isomorphism, so the termwise product
$\prod_iK_i$ is also a product of the $K_i$ in $D$, with the projections induced by the
termwise projections.
