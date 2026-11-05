+++
kind = "proof"
of = "proposition-comparison-etale-derived-category--4"
order = 474009
uses = ["theorem-comparison-direct-images"]
+++
This is [theorem-comparison-direct-images]. The underived comparison
$\nu_Y^*g_{\acute{e}t,*}\to g_{\mathrm{pro}\acute{e}t,*}\nu_X^*$ is invertible
for a quasi-compact and quasi-separated $g$. Moreover, $\nu_X^*$ sends injective
étale sheaves to sheaves acyclic for $g_{\mathrm{pro}\acute{e}t,*}$, by
`AlgebraicGeometry.ProEtale.rightAcyclic_lowerStar_comparisonUpperStar_obj_of_injective`.
Apply the comparison to a bounded below injective resolution of $K$.
Exactness of $\nu^*$ and this acyclicity identify its two images with the two
derived direct images. The resulting isomorphism is the canonical derived
comparison map, as in
`CategoryTheory.Functor.isIso_rightDerivedFunctorPlusBaseChange_of_rightAcyclic`.
