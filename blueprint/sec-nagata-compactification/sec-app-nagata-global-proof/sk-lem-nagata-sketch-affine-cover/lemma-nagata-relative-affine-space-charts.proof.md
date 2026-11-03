+++
kind  = "proof"
of    = "lemma-nagata-relative-affine-space-charts"
+++
(1) For an affine open $V=\operatorname{Spec}(R)$ of $S$, the base change of
$\mathbb A^n_S=S\times\operatorname{Spec}\mathbf Z[T_i:i\in n]$ along the
open immersion $V\to S$ is
$V\times\operatorname{Spec}\mathbf Z[T_i]=\operatorname{Spec}(R[T_i])$, and
the chart is the resulting projection. As a base change of an open immersion
it is an open immersion, and its image is the preimage of $V$. The affine
opens of $S$ cover $S$, so their preimages cover $\mathbb A^n_S$.

(2) Both composites are morphisms into the fibre product
$\mathbb A^n_S$ whose two components agree: on the factor $S$ both are
$\operatorname{Spec}(R'[T_i])\to V'\to S$, and on the factor
$\operatorname{Spec}\mathbf Z[T_i]$ both are induced by
$\mathbf Z[T_i]\to R'[T_i]$. The cocycle condition holds already on rings,
since both composites send each polynomial to the polynomial obtained by
restricting its coefficients from $V$ to $V''$.

(3) The square with sides $\mathbb A^n_T\to\mathbb A^n_S$ (the base change
of $g$), the two structure morphisms and $g$ is cartesian by the pasting law
for fibre products, since both $\mathbb A^n_T$ and $\mathbb A^n_S$ are base
changes of $\operatorname{Spec}\mathbf Z[T_i]$; this gives the isomorphism.
The compatibility with the charts is again a comparison of the two
components of morphisms into a fibre product, both of which are induced by
the ring map $\mathcal O_S(V)[T_i]\to\mathcal O_T(W)[T_i]$ given by
$g^\sharp$ on coefficients.
