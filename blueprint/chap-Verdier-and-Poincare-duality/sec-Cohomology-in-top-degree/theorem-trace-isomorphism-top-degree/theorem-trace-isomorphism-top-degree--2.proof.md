+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--2"
order = 865005
uses = ["theorem-bounded-below-cohomology-comparison", "definition-cohomological-dimension"]
+++
Since $A$ is discrete, $\mathcal C_A$ is the constant pro-étale sheaf. It is the pullback of the constant étale sheaf, so [theorem-bounded-below-cohomology-comparison] identifies their cohomology. The étale sheaf is torsion, and `AlgebraicGeometry.Scheme.subsingleton_H_of_two_mul_lt_of_isSepClosed` gives its vanishing above $2d$. Transport this vanishing through the comparison isomorphisms.
