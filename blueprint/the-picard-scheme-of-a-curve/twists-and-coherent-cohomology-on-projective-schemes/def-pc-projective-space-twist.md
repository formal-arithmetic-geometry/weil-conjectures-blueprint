+++
id = "def-pc-projective-space-twist"
kind = "definition"
title = "Twists on projective space over a ring"
order = 4316
lean = ["AlgebraicGeometry.ProjectiveSpace.twist"]
uses = ["def-pc-proj", "lem-pc-twist-cocycle"]
+++
For a commutative ring $A$ and $n\ge0$, put
$P=\operatorname{Proj}(A[x_0,\ldots,x_n])$, using the projective spectrum
construction [def-pc-proj]. Write $U_i=D_+(x_i)$ for its standard affine
opens. For $d\in\mathbf Z$, the invertible module $\mathcal O_P(d)$ is
obtained by gluing free rank-one modules on the $U_i$ with bases
$e_i^{(d)}$ and transition rule $e_i^{(d)}=(x_i/x_j)^d e_j^{(d)}$; the
well-definedness of this gluing, i.e. the cocycle rule for these units on
triple intersections, is [lem-pc-twist-cocycle].

The section denoted $x_i$ of $\mathcal O_P(1)$ has coefficient $x_i/x_j$ on
$U_j$. For a quasi-coherent module $\mathcal F$, write
$\mathcal F(d)=\mathcal F\otimes\mathcal O_P(d)$. For $A=k$ and $n=1$ this
is the convention of the projective-line calculation of the divisors
chapter.

*Import note.* The source's sentence breaks off at the semicolon and the
definition then closes; the remaining clauses above are the ones the source
states in its pointer remark [rem-ptr-pc-projective-space-twist-17], copied
back here.

Unresolved dependencies: def:sc-invertible-module, pqf-def-coherent, def:sc-p1-standard
