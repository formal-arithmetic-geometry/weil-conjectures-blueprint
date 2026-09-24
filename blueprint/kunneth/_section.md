+++
id = "kunneth"
kind = "section"
title = "Künneth formula"
order = 2954
uses = ["def-compact-support-direct-image-detailed", "def-kun-cd", "def-kun-separably-closed", "def-sbc-smooth-morphisms", "def-sp-truncation-couple", "def-weil-extension-by-zero", "def-weil-pbc-cartesian-square", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "def-weil-pbc-underived-exchange", "fin4-thm-finite-morphisms-constructible", "lem-chow-closed-model", "lem-kun-03qu-sep-closed", "lem-kun-cd-sep-closed-point", "lem-sp-finite-filtration-induction", "lem-sp-long-exact-of-triangle", "lem-weil-pbc-closed-immersion-proper", "lem-weil-pbc-exchange-identity-pasting", "lem-weil-pbc-grothendieck-spectral-sequence", "lem-weil-pbc-proper-base-change", "lem-weil-pbc-proper-composition", "lemma-weil-pbc-constructible-finite-pushforward", "lemma-weil-pbc-derived-exchange-replacement", "lemma-weil-pbc-direct-image-filtered-colimit", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative", "lemma-weil-pbc-hypercohomology-convergence", "lemma-weil-pbc-torsion-filtered-union", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-kinjective-resolutions-exist", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-def-coefficient-conventions", "sbc-lem-higher-direct-image-limit", "sbc-thm-smooth-base-change", "thm-constructible-serre", "thm-weil-pbc-bounded-below", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
**Status.** Chapter status. The final Kunneth theorem
([thm-kun-0f1p]) and its proof were decomposed first; the
displayed order was then normalized so that every dependency precedes
its use, and so is the order maintained below. Each statement and
each proof is marked decomposed independently. Every theorem
labelled ``source'' in a *Source:* note is an input from the
Stacks Project: its statement is fully decomposed (each concept used
in the statement is hyperlinked and its dependencies are listed) but
its proof is intentionally omitted, in accordance with the opt-in
rule for proof decomposition. Claims that are basic commutative or
homological algebra are used directly, e.g. exactness of filtered
colimits, the five lemma, or Zariski's lemma.

The torsion cohomological dimension and its vanishing at a separably closed
point ([def-kun-cd], [lem-kun-cd-sep-closed-point], with [def-kun-separably-closed]
and [lem-kun-03qu-sep-closed]) are general and are cited by
[cohomological-dimension] and [direct-image-finiteness]; they are in
[direct-and-inverse-image-and-the-exchange-morphism] of [foundations].
