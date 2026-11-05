+++
id = "lem-wf-boundary-stalk-invariants"
kind = "lemma"
title = "Boundary stalk as inertia invariants"
lean = ["AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_middleExtension", "AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_middleExtension_of_smooth", "AlgebraicGeometry.Etale.boundarySpecialization", "AlgebraicGeometry.Etale.injective_boundarySpecialization", "AlgebraicGeometry.Etale.boundaryStalkMap_comp_boundarySpecialization", "AlgebraicGeometry.Etale.galoisStalkMap_boundarySpecialization", "AlgebraicGeometry.Etale.exists_boundarySpecialization_eq", "AlgebraicGeometry.Etale.range_boundarySpecialization", "AlgebraicGeometry.Etale.boundaryStalkLinearEquiv", "AlgebraicGeometry.WeilGroup.BoundaryChart.boundaryStalkEquiv", "AlgebraicGeometry.WeilGroup.BoundaryChart.boundaryStalkEquiv_boundaryStalkMap", "AlgebraicGeometry.WeilGroup.BoundaryChart.boundaryStalkEquivInvariants", "AlgebraicGeometry.WeilGroup.BoundaryChart.boundaryStalkEquivInvariants_boundaryStalkMap"]
order = 4106
uses = ["d-real-boundary", "def-wf-fundamental-representation", "def-wf-middle-extension", "p-real-integral", "prop-weil-pbc-strict-henselization-stalk-formula", "sk-lem-coefficient-heart", "sk-lem-integral-models", "sk-prop-integral-criterion", "sk-prop-pe-milnor", "sk-prop-scalar-six", "det-prop-sfb-finite-extension-compatibility", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open immersion of smooth
curves over $k_0$, let $\mathcal F$ be lisse on $U_0$, and let
$x\in C_0\setminus U_0$ be a closed boundary point with local residue
field $\kappa(x)$ and inertia group $I_x$ of [d-real-boundary] inside the local
fundamental group of the
fundamental representation.
Then the boundary stalk of the
middle extension is

$$
(j_*\mathcal F)_{\bar x}\simeq\mathcal F_{\bar\eta}^{I_x},
$$

where $\mathcal F_{\bar\eta}$ is the
geometric generic stalk of
$\mathcal F$ at $x$ and the invariants are formed for the inertia
action. The identification is equivariant for Frobenius: the geometric
Frobenius of $\kappa(x)$ acting on the stalk of the Weil sheaf
$j_*\mathcal F$ at $\bar x$ corresponds to the action of a residue
Frobenius lift on $\mathcal F_{\bar\eta}^{I_x}$ of [d-real-boundary]
(which is independent of the lift).
