+++
id = "sbc-thm-cohomological-dimension-of-an-affine-curve"
kind = "theorem"
title = "Affine-curve cohomological dimension"
order = 5138
lean = ["AlgebraicGeometry.Curve.etaleCohomology_affine_vanishing"]
+++
Let $k$ be algebraically closed, let $C$ be a smooth affine curve over $k$,
and let $d\geq1$ be prime to $\operatorname{char}k$. Then
$$
H^q(C_{\Et},\mathbf Z/d\mathbf Z)=0\qquad(q>1)
$$
with $H^0(C_{\Et},\mathbf Z/d\mathbf Z)=\mathbf Z/d\mathbf Z$.

(*The Jacobian chapter's Kummer computation on an affine curve; Stacks
Project, Theorem 59.83.10, [Tag
03SC](https://stacks.math.columbia.edu/tag/03SC), (2).*)

## Proof

The étale cohomology groups of the constant sheaf $\mathbf Z/d\mathbf Z$ are
computed in the Kummer computation on an affine curve of the Jacobian
chapter (with $n=d$), where the vanishing for $q>1$ is displayed under the
identifications of the Kummer sequence; this is the claim.

Unresolved dependencies: thm:sc-affine-cohomology, def:weil-pbc-scheme-conventions, def:weil-pbc-etale-cohomology
