+++
id = "lem-chow-segre"
kind = "lemma"
title = "The Segre embedding is a closed immersion"
order = 421
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isClosedImmersion_pi", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_segre", "AlgebraicGeometry.ProjectiveSpace.isProper_pi_hom", "AlgebraicGeometry.ProjectiveSpace.nonempty_twistRestrict_segre_iso", "AlgebraicGeometry.IsVeryAmple.tensorObj"]
uses = ["def-chow-segre", "def-nagata-affine-proj", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions"]
+++
The binary Segre embedding
$s:\mathbf P^{n}_S\times_S\mathbf P^{m}_S\to\mathbf P^{n\times m}_S$ of
[def-chow-segre] is a closed immersion, for arbitrary index sets $n,m$.
Consequently, for finitely many finite index sets $n_1,\dots,n_m$ there are a
finite index set $N$ and a closed immersion of $S$-schemes

$$
\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S
\longrightarrow\mathbf P^{N}_S .
$$

Moreover, $\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S\to S$ is
proper.

For arbitrary index sets $n,m$, writing $p_1,p_2$ for the two projections of
$\mathbf P^{n}_S\times_S\mathbf P^{m}_S$, there is an isomorphism

$$
s^*\mathcal O(1)\cong p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)
=\mathcal O(1)\boxtimes\mathcal O(1).
$$

In particular, let $f\colon X\to S$ be a morphism of schemes and let
$\mathcal M,\mathcal N$ be $\mathcal O_X$-modules with
$\mathcal M\cong i^*\mathcal O(1)$ and $\mathcal N\cong j^*\mathcal O(1)$ for
closed immersions $i\colon X\to\mathbf P^{n}_S$ and $j\colon X\to\mathbf P^{m}_S$
over $S$, with $n,m$ finite. Then $s\circ(i,j)\colon X\to\mathbf P^{n\times m}_S$
is a closed immersion over $S$ and
$(s\circ(i,j))^*\mathcal O(1)\cong\mathcal M\otimes\mathcal N$.
