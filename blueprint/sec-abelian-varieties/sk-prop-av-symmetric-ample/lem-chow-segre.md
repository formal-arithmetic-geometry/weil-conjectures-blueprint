+++
id = "lem-chow-segre"
kind = "lemma"
title = "The Segre embedding is a closed immersion"
order = 477
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isClosedImmersion_pi", "AlgebraicGeometry.ProjectiveSpace.isClosedImmersion_segre", "AlgebraicGeometry.ProjectiveSpace.isProper_pi_hom"]
uses = ["def-chow-segre", "def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions", "lemma-nagata-projective-space-base-change-proper", "prop-nagata-proj-standard-open"]
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

In particular, the composite of a closed immersion
$X\hookrightarrow\mathbf P^{n}_S\times_S\mathbf P^{m}_S$ with the Segre
embedding is a closed immersion of $X$ into a single projective space, and
$\mathcal O(1)\boxtimes\mathcal O(1)=s^*\mathcal O(1)$ is very ample on
$\mathbf P^{n}_S\times_S\mathbf P^{m}_S$.
