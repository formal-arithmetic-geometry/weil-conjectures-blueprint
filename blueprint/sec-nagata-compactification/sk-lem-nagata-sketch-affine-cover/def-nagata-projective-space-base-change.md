+++
id = "def-nagata-projective-space-base-change"
kind = "definition"
title = "Projective space over a base scheme, by base change"
order = 406
lean = ["AlgebraicGeometry.ProjectiveSpace"]
uses = ["def-nagata-affine-proj"]
+++
Let $n$ be an index set and $S$ a scheme. Put

$$
\mathbf P^n_{\mathbf Z}
=\operatorname{Proj}\bigl(\mathbf Z[T_i:i\in n]\bigr),
\qquad
\mathbf P(n;S)
=S\times_{\operatorname{Spec}\mathbf Z}\mathbf P^n_{\mathbf Z},
$$

where the polynomial ring carries its total-degree grading, and take for the
structural morphism $\mathbf P(n;S)\to S$ the first projection. Here $n$
indexes the *homogeneous* coordinates, so the classical
$\mathbf P^r_S$ is $\mathbf P(\{0,\dots,r\};S)$.
