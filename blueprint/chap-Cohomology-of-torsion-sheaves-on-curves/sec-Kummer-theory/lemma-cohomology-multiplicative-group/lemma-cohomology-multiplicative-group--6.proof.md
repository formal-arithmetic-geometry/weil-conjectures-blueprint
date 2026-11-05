+++
kind = "proof"
of = "lemma-cohomology-multiplicative-group--6"
uses = ["lemma-cohomology-multiplicative-group--7", "lemma-cohomology-multiplicative-group--8", "lemma-finite-morphisms"]
+++
First suppose $C$ is connected. Smoothness makes $C$ regular and reduced;
a connected regular noetherian scheme is irreducible, so $C$ is integral.
By [lemma-cohomology-multiplicative-group--7], the cohomological Brauer
group of $k(C)$ vanishes. The map in
[lemma-cohomology-multiplicative-group--8] is injective, and
`AlgebraicGeometry.Scheme.isIso_upperStarGmSheafToGmSheaf_fromSpecFunctionField`
identifies its coefficient sheaf with $\mathbf G_m$ on the generic point.
Thus $H^2(C_{\acute{e}t},\mathbf G_m)=0$. This is
`AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_of_connectedSpace`.

In general $C$ is noetherian, so its finitely many connected components
are open and closed. Each is again a smooth curve. Apply the connected
case on every component and then
`AlgebraicGeometry.Etale.subsingleton_H_of_isClopen`, which detects
vanishing of cohomology on such a decomposition.
The inclusions of the components are finite, so their direct images
are exact by [lemma-finite-morphisms].
