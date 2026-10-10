+++
kind  = "proof"
of    = "lemma-nagata-isomorphism-near-closure"
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-maximal-isomorphism-open", "def-nagata-proj-closed-center-finite-degree", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-invertible-factor", "lemma-nagata-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-localization-ideal-pow", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-proper-to-separated-target", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-separate-constructible-closed", "lemma-nagata-spectral-constructible-separation-exists", "prop-nagata-affine-blowup-chart", "prop-nagata-rees-graded", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-proper", "thm-nagata-strict-transform-is-blowup"]
+++
We show that $\pi=\mathsf{IsoBl}_{V,T}(q)\to X$ of
[def-nagata-isomorphism-near-closure] has this property; we use the
notation of that construction: $U=q^{-1}(V)$, $E\subseteq V$ the complement
of $\operatorname{IsoOpen}(U\to V)$, the separated pair $(T_c,E_c)$, the
blow-up $X_1$, and $X_0=X_1\setminus\overline E_c$. Its hypotheses hold:
if $N$ is an open neighbourhood of $T$ in $X$ over which $q$ is an
isomorphism, then $U\to V$ is an isomorphism over the open neighbourhood
$N\cap V$ of $T$ in $V$.

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
$V$-admissible blow-up $\pi\colon X'\to X$. As $\pi$ is an isomorphism over
$V\supseteq T$, the closure of $\pi^{-1}(T)$ in $X'$ is the closure of the
copy of $T$ considered above; so the open neighbourhood just obtained is an
open $N'$ containing the closure of $\pi^{-1}(T)$ over which the strict
transform of $q$ along $\pi$ is an isomorphism.
