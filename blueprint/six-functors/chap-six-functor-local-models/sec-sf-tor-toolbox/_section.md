+++
id = "sec-sf-tor-toolbox"
kind = "section"
title = "The flat model of finite Tor amplitude, and what it settles"
order = 3416
uses = ["def-exchange-projection", "def-sc-etale-torsion-cd", "def-weil-algebraically-closed-coefficients", "def-weil-derived-cohomology-sheaves", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-full-cohomological-dimension", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-constructible-complexes", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "def-weil-site-perfect-complex", "def-weil-small-proetale-site-detailed", "fin4-lem-fibrewise-cohomological-dimension", "lem-cbc-proetale-stalk-conservative", "lem-exc-comparison-tor-interval", "lem-exc-constant-inverse-image-flat", "lem-exc-field-discrete-modules", "lem-exc-residue-tor-test", "lem-kun-dimension-formula", "lem-sf-hom-finite-projective", "lem-weil-pbc-comparison-pullback", "lem-weil-pbc-constructible-serre", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-pullback-preserves-bounded-constructible", "lem-weil-pbc-qcqs-higher-direct-image", "lem-weil-pbc-reconstruction-uniform-tower", "prop-sf-dualizable", "prop-sf-dualizable-hom", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-kinjective-resolutions-exist", "prop-weil-pbc-proetale-constant-ring-map", "sbc-def-coefficient-conventions", "thm-dg-finite-type-constructibility", "thm-sc-finite-type-torsion-cd", "thm-sp-grothendieck", "thm-sp-truncation-e2", "thm-weil-pbc-site-comparison"]
+++
The cells of [rem-sf-preservation-matrix] that concern the finite-Tor
subcategories are settled here by a single tool: a flat model of an object
of finite Tor amplitude. This is the criterion that the arguments of the
exceptional-inverse-image chapter invoke as ``the usual flat-resolution
criterion'' and that the trace-formula chapter invokes in the form
``inverse image along any morphism preserves finite Tor amplitude''; it is
recorded here as a statement with a proof, so that no proof of this
blueprint uses it without a reference. Every statement of this section is
made at the finite coefficient stages $A=A_{E,n}$ on the
small pro-étale sites; the
comparison of the four coefficient stages is
[rem-sf-tor-toolbox-stages].

The two cells of [rem-sf-preservation-matrix] that the tools above do
not by themselves settle — the direct image on the finite-Tor subcategory
for a non-proper morphism, and the derived internal Hom of two arbitrary
finite-Tor objects — are proved at the end of this section on the small
étale site, where the residue test [lem-exc-residue-tor-test] and the
torsion cohomological-dimension bound of chap:jacobian
are available: the direct image is
[cor-sf-direct-image-ctf-nonproper], with the uniform vanishing input
of [lem-sf-etale-direct-image-vanishing], and the internal Hom is
[thm-sf-hom-ctf]. Their transport to the small pro-étale site, and
the exact residue of the pro-étale gap, are recorded in
[cor-sf-direct-image-ctf-etale-origin] and
[open-sf-preservation-gaps].

The two cells of [rem-sf-preservation-matrix] that the tools above
reach only for the objects of étale origin are transported to the small
pro-étale site here. The transport rests on one input about the
comparison morphism — that the intrinsically constructible pro-étale
coefficients are exactly the pulled-back étale ones,
[lem-sf-proetale-constructible-origin] — and on the two transfer
statements [lem-sf-comparison-tor-amplitude] and
[lem-sf-proetale-residue-tor-test], which make the finite-Tor
condition and the residue test readable on the pro-étale site. The
statements [thm-sf-fullcd-etale-origin],
[lem-sf-proetale-vanishing-detection] and
[lem-sf-reduction-flat-model], [lem-sf-reduction-residue-test] record what
the same devices give for the full-cohomological-dimension interface and
for the finite-reduction coherence of clause (vii).
