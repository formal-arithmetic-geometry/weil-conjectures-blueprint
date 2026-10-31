+++
id = "sk-thm-dnc"
kind = "lemma"
title = "A section and its normal bundle"
order = 449
lean = ["AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone"]
uses = ["sk-prop-cohsm", "sk-lem-geometry", "sk-prop-a1-inv", "sk-prop-an", "sk-thm-existence"]
tags = ["sketch"]
+++
There is a canonical isomorphism

$$
s^{*}\omega_{g}\xrightarrow{\sim}z^{*}\omega_{\pi}.
\tag{10.12}
$$

It is obtained by restricting to $t=0$ the unique isomorphism
$\widetilde s^{*}\omega_{\widetilde g}\to a^{*}s^{*}\omega_{g}$ that is the identity at $t=1$, and inverting. Here
$a:\mathbf A^1_S\to S$ is the projection.
