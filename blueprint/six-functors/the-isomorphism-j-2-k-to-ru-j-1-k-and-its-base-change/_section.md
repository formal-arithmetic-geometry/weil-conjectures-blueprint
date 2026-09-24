+++
id = "the-isomorphism-j-2-k-to-ru-j-1-k-and-its-base-change"
kind = "section"
title = "The isomorphism $j_{2!}K\\to Ru_*j_{1!}K$ and its base change"
order = 2030
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-exchange-projection", "def-weil-compact-support-candidate", "def-weil-compactifications-refinements", "def-weil-derived-direct-image", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-proper-base-change", "prop-compactification-refinement", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-inverse-image-exact", "prop-weil-pbc-kinjective-resolutions-exist", "thm-weil-pbc-site-comparison"]
+++
This section is chapter 10 of `weil_conjectures_detailed.tex`: the comparison that makes
$Rf_!$ independent of the compactification. For two compactifications related
by a refinement $u$, the comparison $j_{2!}K\to Ru_*j_{1!}K$ of
[def-weil-pbc-proper-open-comparison] is an isomorphism
[lem-weil-pbc-proper-open-comparison-iso], is compatible with composition
[lem-weil-pbc-proper-open-comparison-composition], and transports to the
pro-etale site [lem-weil-pbc-proper-open-comparison-proetale]. The section
ends with [prop-compactification-coherence-detailed]: the comparison maps
satisfy the identity and cocycle conditions, so $Rf_!$ is well defined.

The isomorphism is proved on geometric fibres, through
[cor-weil-pbc-geometric-fiber-finite]; that is why this section comes after
[chap-proper-base-change].

The coherence statement is the one the rest of the source cites: the
definition of $Rf_!$ and the exchange-projection map in [foundations], and
later the compact-support base change, the six-functor interfaces,
Poincare duality and the trace formula. Its id carries the suffix
`-detailed` because a coarser sketch-level object once held the plain id.

The two foundations objects, [def-compact-support-direct-image-detailed] and
[def-exchange-projection], keep `prop:compactification-coherence` as an
unresolved dependency rather than a `uses` edge: [foundations] is cited by
[chap-proper-base-change], so an edge from it into this part would close a
cycle. The source defines $Rf_!$ in its first chapter with a forward reference
to this one; resolving that properly means splitting the definition of $Rf_!$
out of [foundations] into this part, which is left for when the
compact-support chapters are imported.
