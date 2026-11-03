+++
id = "def-sc-function-field"
kind = "definition"
title = "The function field of a curve"
order = 498
lean = ["AlgebraicGeometry.Scheme.functionFieldOfComponents", "AlgebraicGeometry.Scheme.functionField", "AlgebraicGeometry.functionField_isFractionRing_of_isAffineOpen", "AlgebraicGeometry.Scheme.rationalFunctionRing"]
uses = ["def-sc-curves"]
+++
Let $C$ be a scheme, for instance a curve over $k$. The
*function field* $k(C)$ is the product of the stalks of the
structure sheaf at the generic points of the irreducible components
of $C$. The *ring of rational functions* on $C$ is the colimit of the
rings $\mathcal O_C(U)$ over the dense open subsets $U\subseteq C$, with
the restriction maps. For an integral scheme $C$ (for instance an
integral curve) there is a single component, $k(C)=\mathcal O_{C,\eta}$ is
the stalk at the generic point $\eta$, and it is the field of fractions of
$\mathcal O_C(U)$ for any nonempty affine open $U\subseteq C$.
