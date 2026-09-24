+++
id = "sec-sf-tor-toolbox-continued"
kind = "section"
title = "The flat model of finite Tor amplitude, and what it settles (continued)"
order = 3714
uses = ["cor-coef-finite-verdier", "cor-coef-verdier-weil-equivariance", "cor-sf-finite-level-comparison-two-cases", "cor-weil-boundary-duality-discharge", "cor-weil-finite-constructible-hom", "def-coef-normalized-dvr-tower", "def-trf-admissibility", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-site-comparison-morphism", "def-weil-site-perfect-complex", "lem-coef-finite-direct-image", "lem-coef-finite-exceptional", "lem-coef-integral-finite-extension", "lem-coef-integral-hom-reduction", "lem-coef-normalized-dvr-effectivity", "lem-coef-rational-operations", "lem-fix-operation-reduction", "lem-fix-weil-operations", "lem-sf-comparison-tor-amplitude", "lem-sf-ext-sheaf-constructible", "lem-sf-finite-level-comparison", "lem-sf-flat-model", "lem-sf-hom-finite-projective", "lem-weil-finite-duality-site-comparison", "prop-coef-integral-exceptional-adjoint", "rem-sf-class-adjoint-residue", "rem-sf-tower-shapes-occurring", "thm-coef-finite-hom", "thm-coef-integral-verdier", "thm-coef-qbar-verdier", "thm-fix-general-biduality", "thm-sf-ambient-adjoint-class", "thm-sf-preservation-class", "thm-sf-uniform-models-constant-tower", "thm-sf-uniform-models-lisse-tower"]
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
