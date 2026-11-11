+++
id = "lemma-naturality-pasting-comparison--3"
kind = "lemma"
title = "Naturality, pasting and comparison (3)"
name_showing = false
order = 324005
aliases = ["bp-r097-3"]
lean = ["AlgebraicGeometry.ProEtale.baseChangeSourceComparisonIso", "AlgebraicGeometry.ProEtale.baseChangeTargetComparisonIso", "AlgebraicGeometry.ProEtale.comparison_derivedBaseChangeMap"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "definition-derived-base-change-map--1", "definition-pro-etale-base-change-map--1"]
+++
Let (4.1) be a cartesian square, let $\Lambda$ be a discrete commutative
ring, and let $K\in D^+(X_{\acute{e}t},\Lambda)$. Suppose that $f$ and
$f'$ are qcqs. The comparison of inverse images and the isomorphisms of
Theorem [theorem-comparison-direct-images] give isomorphisms

$$
\alpha_K:\nu_{Y'}^*g_{\acute{e}t}^*Rf_{\acute{e}t,*}K
\xrightarrow{\sim}
g_{\mathrm{pro}\acute{e}t}^*Rf_{\mathrm{pro}\acute{e}t,*}\nu_X^*K,
$$

$$
\beta_K:\nu_{Y'}^*Rf'_{\acute{e}t,*}g'^*_{\acute{e}t}K
\xrightarrow{\sim}
Rf'_{\mathrm{pro}\acute{e}t,*}g'^*_{\mathrm{pro}\acute{e}t}\nu_X^*K.
$$

Here $\alpha_K$ first commutes $\nu^*$ with $g^*$ and then uses the
direct image comparison for $f$; $\beta_K$ first uses the direct image
comparison for $f'$ and then commutes $\nu^*$ with $g'^*$. All objects
are viewed in $D(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$, and the
pro-étale direct images are the unbounded right derived functors.

Writing $\mathrm{BC}_{\acute{e}t,K}$ and
$\mathrm{BC}_{\mathrm{pro}\acute{e}t,\nu_X^*K}$ for the two base change
maps, one has

$$
\beta_K\circ\nu_{Y'}^*(\mathrm{BC}_{\acute{e}t,K})
=\mathrm{BC}_{\mathrm{pro}\acute{e}t,\nu_X^*K}\circ\alpha_K.
$$

Thus these comparisons identify the pro-étale base change map with the
inverse image of the étale base change map. No torsion or finiteness
hypothesis on $\Lambda$ is needed.
