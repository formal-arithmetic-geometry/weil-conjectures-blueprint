+++
kind = "proof"
of = "det-pe-derived-nakayama-first-reduction"
+++
*Vanishing.* Suppose $K_1=0$. By [det-pe-derived-nakayama-resolution] there is a
triangle $K_1\to K_{n+1}\to K_n\to$ for every $n\geq1$. If $K_n=0$, its outer terms
vanish, so $K_{n+1}=0$. By induction all $K_n$ vanish, hence
$R\varprojlim_nK_n=0$, and completeness gives $K\cong R\varprojlim_nK_n=0$.

*Cones.* Represent $f$ by a map of complexes of $\mathcal O_{E,X}$-modules and let
$C=\operatorname{cone}(f)$ be the mapping cone. By
[det-pe-derived-nakayama-resolution], $K_n$ is represented functorially by the
mapping cone of $\pi_E^n$ on the complex $K$, and $R\varprojlim_n$ of a strict
tower of complexes $(M_n)$ is represented by the fibre of
$1-\text{shift}\colon\prod_nM_n\to\prod_nM_n$ formed termwise; this computes the
derived limit because countable products are exact on $X_{\Proet}$
([det-pe-products-exact]), so that termwise products of complexes are products in
the derived category ([det-pe-products-derived]). Both constructions are functorial on complexes and
commute with mapping cones up to canonical isomorphism, so the canonical maps
$K\to R\varprojlim_nK_n$, $L\to R\varprojlim_nL_n$ and
$C\to R\varprojlim_nC_n$ form a morphism of distinguished triangles. If the
first two are isomorphisms, so is the third, by the five lemma on cohomology
sheaves. Shifts are clear. So $C$ is derived complete.

*Isomorphisms.* With $C$ as above, $C_1=\operatorname{cone}(f_1)=0$ when $f_1$ is
an isomorphism. By the first part $C=0$, so $f$ is an isomorphism.
