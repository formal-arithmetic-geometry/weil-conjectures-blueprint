+++
id = "lem-chow-segre"
kind = "lemma"
title = "The Segre embedding is a closed immersion"
order = 621
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isClosedImmersion_pi", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_segre", "AlgebraicGeometry.ProjectiveSpace.isProper_pi_hom"]
uses = ["def-chow-segre"]
+++
The morphism $s$ of [def-chow-segre] is a closed immersion. Consequently,
for index sets $n_1,\dots,n_m$ there are an index set $N$ and a closed
immersion of $S$-schemes

$$
\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S
\longrightarrow\mathbf P^{N}_S ;
$$

one may take $N=n_1\times\dots\times n_m$. Moreover, if all the $n_i$ are
finite, then $\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S\to S$ is
proper.

## Proof

Being a closed immersion is local on the target and on $S$, so we may assume
$S=\Spec A$ is affine and check the assertion on the standard affine charts
$D_+(X_e)\subseteq\mathbf P^N_S$, which cover $\mathbf P^N_S$. For a
multi-index $e$ one has

$$
s^{-1}\bigl(D_+(X_e)\bigr)=\prod_{i=1}^m D_+(x_{i,e_i}),
$$

which is affine, being a finite fibre product of affine schemes over the affine
base. On these charts $s$ is induced by the $A$-algebra homomorphism

$$
\mathcal O_{\mathbf P^N_S}\bigl(D_+(X_e)\bigr)
\longrightarrow
\mathcal O_{\mathbf P^{n_1}_S}\bigl(D_+(x_{1,e_1})\bigr)\otimes_A\dots
\otimes_A\mathcal O_{\mathbf P^{n_m}_S}\bigl(D_+(x_{m,e_m})\bigr),
\qquad
\frac{X_f}{X_e}\longmapsto\prod_{i=1}^m\frac{x_{i,f_i}}{x_{i,e_i}}.
$$

This homomorphism is surjective: for each $i$ and each $0\leq f_i\leq n_i$ the
multi-index $f=(e_1,\dots,e_{i-1},f_i,e_{i+1},\dots,e_m)$ satisfies
$X_f/X_e\mapsto x_{i,f_i}/x_{i,e_i}$, and these ratios generate the target as
an $A$-algebra. Hence $s$ is, locally on the target, the morphism of affine
schemes attached to a surjective ring homomorphism, i.e. a closed immersion.
Compare 01WD. (The argument above is written for a general
$m$; the formalisation carries it out for the binary case $m=2$ over
$\Spec\mathbf Z$, obtains a general base $S$ by base change, and reduces the
general $m$ to the binary case by the induction below.)

The $m$-fold statement follows by induction on the index set of the product.
For the empty product the fibre product is $S$ itself, which is
$\mathbf P^{N}_S$ for a one-element index set $N$; and if
$\mathbf P^{n_2}_S\times_S\dots\times_S\mathbf P^{n_m}_S\to\mathbf P^{N}_S$ is
a closed immersion, then so is

$$
\mathbf P^{n_1}_S\times_S\bigl(\mathbf P^{n_2}_S\times_S\dots\times_S
\mathbf P^{n_m}_S\bigr)
\longrightarrow\mathbf P^{n_1}_S\times_S\mathbf P^{N}_S
\longrightarrow\mathbf P^{n_1\times N}_S,
$$

the first morphism because closed immersions are stable under base change and
the second by the binary case.

The last assertion does not use the Segre embedding: a finite fibre product of
proper $S$-schemes is proper over $S$, because properness is stable under base
change and under composition, and $\mathbf P^{n_i}_S\to S$ is proper by
01WC.
