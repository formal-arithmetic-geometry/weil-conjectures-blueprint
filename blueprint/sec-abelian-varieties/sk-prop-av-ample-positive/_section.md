+++
id = "sk-prop-av-ample-positive"
kind = "section"
title = "Ample modules on proper curves have positive degree"
lean = ["AlgebraicGeometry.Scheme.Hom.degree_pos_of_isAmple"]
order = 549
uses = ["sk-def-av-ample-degree"]
+++
*Proposition (sketch).*

Let $k$ be algebraically closed, $C$ a proper curve over $k$ of
dimension one (possibly disconnected) and $\cL$ an ample invertible
$\cO_C$-module. Then $\deg\cL>0$.

## Proof

On a proper curve an ample invertible module has positive degree, the
degree being the coefficient of the leading term of the Hilbert
polynomial ([sk-def-av-ample-degree]); for disconnected $C$, $\chi$ is
additive over the connected components, each zero-dimensional one
contributes a constant and each one-dimensional one a positive leading
coefficient. Dimension one is needed: for $C=\Spec k$ every invertible
module is trivial and $\chi(\cL^{\otimes m})=1$, so the degree is $0$.

Uses: [sk-def-av-ample-degree]
