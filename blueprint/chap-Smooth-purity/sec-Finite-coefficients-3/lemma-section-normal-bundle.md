+++
id = "lemma-section-normal-bundle"
kind = "lemma"
title = "A section and its normal bundle"
order = 742
lean = ["AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone"]
uses = ["proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-deformation-normal-bundle", "definition-compactification-refinement"]
+++
There is a canonical isomorphism

$$
s^{*}\omega_{g}\xrightarrow{\sim}z^{*}\omega_{\pi}.
\tag{9.13}
$$

It is obtained by restricting to $t=0$ the unique isomorphism
$\widetilde s^{*}\omega_{\widetilde g}\to a^{*}s^{*}\omega_{g}$ that is the identity at $t=1$, and inverting. Here
$a:\mathbf A^1_S\to S$ is the projection.
