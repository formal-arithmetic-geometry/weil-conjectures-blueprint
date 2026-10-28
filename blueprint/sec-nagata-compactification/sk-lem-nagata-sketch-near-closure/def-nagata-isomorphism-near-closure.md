+++
id = "def-nagata-isomorphism-near-closure"
kind = "definition"
title = "Modification making a proper map an isomorphism near a closure"
lean = ["AlgebraicGeometry.isoNearClosureSeparation", "AlgebraicGeometry.isoNearClosureSeparationBlowup", "AlgebraicGeometry.isoNearClosureNbhd", "AlgebraicGeometry.isoNearClosureLift", "AlgebraicGeometry.isoNearClosureElimination", "AlgebraicGeometry.isoNearClosureExtendedCentre", "AlgebraicGeometry.isoNearClosureCentre", "AlgebraicGeometry.isoNearClosureBlowup"]
order = 263
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-admissible-blowup", "def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-invertible-ideal", "def-nagata-elimination-indeterminacy", "def-nagata-extended-admissible-blowup", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-maximal-isomorphism-open", "def-nagata-proj-closed-center-finite-degree", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-separate-constructible-closed", "def-nagata-spectral-constructible-separation", "def-nagata-strict-transform", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-invertible-factor", "thm-nagata-global-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-localization-ideal-pow", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-proper-to-separated-target", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-separate-constructible-closed", "lemma-nagata-spectral-constructible-separation-exists", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-strict-transform-is-blowup"]
+++
Let $X$ be qcqs, let $q\colon Z\to X$ be proper, let $V\subseteq X$ be a
quasi-compact open, and let $T\subseteq V$ be closed in $V$. Assume $q$ is an
isomorphism over an open neighbourhood of $T$ in $X$. Let
$E=V\setminus\operatorname{IsoOpen}(q)$, with $\operatorname{IsoOpen}(q)$ from
[def-nagata-maximal-isomorphism-open]; it is closed in $V$ and disjoint
from $T$. Define $\mathsf{IsoBl}_{V,T}(q)\to X$ by the following steps.

1. Apply [def-nagata-spectral-constructible-separation] to $(T,E)$ in $V$
   and denote the output by $(T_c,E_c)$. Put $V_2=V\setminus E_c$, a
   quasi-compact open containing $T$ over which $q$ is an isomorphism.
2. Perform the explicitly constructed $V$-admissible separation blow-up
   $$
   \pi_1\colon X_1=\mathsf{CSepBl}_V(T_c,E_c)\longrightarrow X,
   $$
   in which the closures of $\pi_1^{-1}(T_c)$ and $\pi_1^{-1}(E_c)$ are
   disjoint.
3. Apply [def-nagata-spectral-constructible-separation] in $X_1$ to these
   two closures, and let $A\subseteq X_1$ be the complement of the second
   output: a quasi-compact open containing
   $\overline{\pi_1^{-1}(T_c)}$ and disjoint from
   $\overline{\pi_1^{-1}(E_c)}$.
4. Let $\lambda_1\colon Z_1\to X_1$ be the strict transform of $q$ along
   $\pi_1$, i.e. the canonical lift of $q$ from the blow-up $Z_1$ of $Z$ along
   the pulled-back centre; it is proper and an isomorphism over
   $\pi_1^{-1}(V_2)$.
5. Form the elimination blow-up
   $X_1^{\mathrm{el}}(\lambda_1,\pi_1^{-1}(V_2))$ of
   [def-nagata-elimination-indeterminacy], a
   $\pi_1^{-1}(V_2)$-admissible blow-up of $X_1$.
6. Restrict its centre to $A$ and extend this restriction by
   [def-nagata-extended-admissible-blowup] to a finite-type centre $D$ on
   $X_1$ whose support is disjoint from $\pi_1^{-1}(V)$.
7. Let $K$ be the centre on $X$ representing the composite of $\pi_1$ and
   $\operatorname{Bl}_D(X_1)\to X_1$ as one blow-up by the composition
   construction.

Define $\mathsf{IsoBl}_{V,T}(q)=\operatorname{Bl}_K(X)\to X$; it is a
$V$-admissible blow-up.
