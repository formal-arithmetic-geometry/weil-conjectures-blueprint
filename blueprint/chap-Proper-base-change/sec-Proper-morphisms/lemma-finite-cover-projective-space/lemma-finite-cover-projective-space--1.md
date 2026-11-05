+++
id = "lemma-finite-cover-projective-space--1"
kind = "lemma"
title = "The recursive symmetric product morphism"
order = 392001
aliases = ["bp-r119-1"]
lean = ["AlgebraicGeometry.ProjectiveSpace.isFinite_symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.projectiveLinePow", "AlgebraicGeometry.ProjectiveSpace.projectiveLinePowProj", "AlgebraicGeometry.ProjectiveSpace.surjective_symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.symmetricProduct_over"]
+++
For a scheme $S$, realize the powers of the projective line as the tower

$$
X_0=S,\qquad X_{k+1}=\mathbf P^1_{X_k},
$$

so that $X_k\simeq(\mathbf P^1_S)^k$, and let $p_k:X_k\to S$ be the
composite of its projections, with $p_0=\operatorname{id}_S$. Let $k\geq0$ and write
$\pi:\mathbf P^k_S\to S$ for the projection.

The symmetric product morphism

$$
\sigma_k:X_k\longrightarrow\mathbf P^k_S,
$$

constructed recursively by multiplying binary linear forms, is finite
and surjective, and satisfies

$$
\pi\circ\sigma_k=p_k.
$$
