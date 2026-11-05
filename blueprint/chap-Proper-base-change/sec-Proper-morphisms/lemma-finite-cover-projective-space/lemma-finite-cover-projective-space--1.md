+++
id = "lemma-finite-cover-projective-space--1"
kind = "lemma"
title = "The recursive symmetric product morphism"
name_showing = false
order = 392001
aliases = ["bp-r119-1"]
lean = ["AlgebraicGeometry.ProjectiveSpace.projectiveLinePow", "AlgebraicGeometry.ProjectiveSpace.projectiveLinePowProj", "AlgebraicGeometry.ProjectiveSpace.symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.isFinite_symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.surjective_symmetricProduct", "AlgebraicGeometry.ProjectiveSpace.symmetricProduct_over"]
uses = []
+++
For a scheme $S$, realize the powers of the projective line as the tower

$$
X_0=S,\qquad X_{k+1}=\mathbf P^1_{X_k},
$$

and let $p_k:X_k\to S$ be the composite of its projections, with
$p_0=\id_S$. Let $k\geq0$ and let $I$ be an index set equipped with a
bijection $e:I\xrightarrow{\sim}\{0,\ldots,k\}$. Write $\mathbf P(I;S)$
for projective space with homogeneous coordinates indexed by $I$, and
$\pi_I:\mathbf P(I;S)\to S$ for its projection.

The symmetric product morphism

$$
\sigma_{k,e}:X_k\longrightarrow\mathbf P(I;S),
$$

constructed recursively by multiplying binary linear forms, is finite
and surjective, and satisfies

$$
\pi_I\circ\sigma_{k,e}=p_k.
$$
