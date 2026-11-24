+++
id = "proposition-purity-vector-bundles"
kind = "proposition"
title = "Purity for vector bundles"
order = 741
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpace"]
uses = ["definition-constructible-sheaves", "proposition-composition-open-restriction-compactifications-f", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
Let $\pi:V\to S$ be a vector bundle of rank $d$.
For $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{S_{\mathrm{pro}\acute{e}t}},\mathbf Z/\ell^n\mathbf Z)$, the trace map induces an
isomorphism

$$
\pi^{*}\href{@definition-tate-twists}{K(d)}[2d]\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{\pi^{!}K}.
$$
