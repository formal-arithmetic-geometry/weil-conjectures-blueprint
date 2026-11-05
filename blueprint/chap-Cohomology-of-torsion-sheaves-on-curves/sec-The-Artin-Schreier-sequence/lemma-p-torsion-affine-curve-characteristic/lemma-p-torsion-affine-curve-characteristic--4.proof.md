+++
kind = "proof"
of = "lemma-p-torsion-affine-curve-characteristic--4"
uses = []
+++
Every étale covering of an affine étale $X$-scheme $V=\operatorname{Spec}A$
admits a finite affine refinement $V_i=\operatorname{Spec}B_i$, whose
Čech nerve consists of affine schemes. The map
$A\to\prod_iB_i$ is faithfully flat. The Čech complex of
$\mathbf G_a$ is identified with the corresponding complex of tensor
products of the $B_i$ over $A$; after this faithfully flat base change
the cover has sections and the complex is contractible in positive
degrees. Faithfully flat descent therefore gives exactness of the
original Čech complex.

The criterion that exactness on such covering families implies
vanishing of higher sheaf cohomology now applies, using the terminal
étale $X$-scheme $X$ itself. This is the route of
`AlgebraicGeometry.Scheme.exactAt_cechComplex_gaPresheaf` and
`CategoryTheory.Sheaf.subsingleton_H_succ_of_exactAt_cechComplex`.
