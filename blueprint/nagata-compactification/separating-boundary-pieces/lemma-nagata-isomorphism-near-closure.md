+++
id = "lemma-nagata-isomorphism-near-closure"
kind = "lemma"
title = "Property of the isomorphism-near-closure construction, [stacks-project]"
order = 437
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isIso_strictTransformMap_near_closure"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-isomorphism-near-closure", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-proper-open-dense-iso", "lemma-nagata-separate-constructible-closed", "lemma-nagata-spectral-constructible-separation", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent", "prop-nagata-strict-transform-closed-fiber-product"]
+++
If $U\to V$ is an isomorphism over an open neighbourhood of $T$, then
$\mathsf{IsoBl}_{V,T}(q)\to X$ is $V$-admissible and the strict transform
of $q$ is an isomorphism over an open neighbourhood of the closure of $T$
in $\mathsf{IsoBl}_{V,T}(q)$.

## Proof

By [lemma-nagata-maximal-isomorphism-open], the assumed isomorphism
neighbourhood is contained in $\operatorname{IsoOpen}(U\to V)$; hence the
bad locus $E$ is disjoint from $T$. The two separation steps make
$\overline T_c$ and $\overline E_c$
disjoint in $X_1$, so $X_0$ contains an open neighbourhood of
$\overline T_c$, hence of $\overline T$. On
$V\setminus E_c$ the restricted proper map is already an isomorphism.

By [lemma-nagata-elimination-indeterminacy], the strict transform after
the constructed blow-up of $X_0$ is an open immersion. The strict transform
is proper because it is a closed subscheme of the base change of the proper
morphism $q$ (use the closed-chart model in
[prop-nagata-strict-transform-closed-fiber-product]); hence
[lemma-nagata-proper-open-dense-iso] applies once density is checked.
The open $V\setminus E_c$ is scheme-theoretically dense in $X_0$ by the
density-preservation clause for admissible blow-ups, and its pullback is the
preserved isomorphism open by
[lemma-nagata-strict-transform-over-complement]. Thus the strict
transform over $X_0$ is an isomorphism. The extension construction has
unit center on $X_1\setminus X_0$ and restricts canonically to the preceding
blow-up on $X_0$ by
[lemma-nagata-extend-admissible-blowup]; the restriction and inverse
maps therefore transport across the canonical strict-transform comparison.
Since $\overline T\subset X_0$, this transported isomorphism holds on an
open neighbourhood of $\overline T$. Finally
[lemma-nagata-admissible-blowup-comp] identifies the composite with one
$V$-admissible blow-up, giving the asserted construction.
