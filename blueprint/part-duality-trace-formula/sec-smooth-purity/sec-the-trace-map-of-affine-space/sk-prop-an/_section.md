+++
id = "sk-prop-an"
kind = "proposition"
title = "Purity for vector bundles"
order = 443
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpaceZero"]
uses = ["sk-prop-cohsm", "sk-lem-sf-mate", "sk-prop-a1-inv", "sk-thm-curveestimate", "sk-prop-sf-open-closed-triangle", "sk-thm-properbasechange", "sk-prop-geo-p1-adjunction", "sk-lem-sp-finite-existence", "sk-thm-existence", "sk-prop-sf-existence", "sk-lem-geo-cartier", "sk-lem-geo-p1-cohomology", "sk-lem-geo-smooth-generic", "sk-thm-sbc-coefficients", "sk-prop-sf-comp-coherence"]
tags = ["sketch"]
+++
Let $\pi:V\to S$ be a vector bundle of rank $d$.
For $K\in D^b_{\mathrm{ctf}}(S_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$, the trace map induces an
isomorphism

$$
\pi^{*}K(d)[2d]\xrightarrow{\sim}\pi^{!}K.
$$
