+++
id = "def-nagata-relative-finite-affine-presentation"
kind = "definition"
title = "Selected finite relative affine presentation"
order = 56
lean = ["AlgebraicGeometry.RelativeAffinePresentation", "AlgebraicGeometry.relativeAffinePresentation", "AlgebraicGeometry.RelativeAffinePresentation.glueData"]
+++
Let $(S_\lambda)$ be a nonempty cofiltered inverse system of schemes with
limit $S$, and let $X\to S$ be a morphism from a quasi-compact scheme. A
*finite relative affine presentation* of $X$ over $S$ consists of an index
$\lambda_0$, finitely many affine opens $V_a\subseteq S_{\lambda_0}$, and
affine opens $W_a\subseteq X$ covering $X$ such that $W_a$ maps into $V_a$
under $X\to S\to S_{\lambda_0}$. The overlaps $W_a\cap W_b$, regarded as
opens of $W_a$, together with both directions of the overlap
identifications $W_a\cap W_b\cong W_b\cap W_a$, form gluing data along
opens, with their identity, inverse, and cocycle equations. Select such a
presentation and call it $\mathsf R_X$.
