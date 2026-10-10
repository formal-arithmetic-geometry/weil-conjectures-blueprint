+++
id = "lemma-nagata-key-boundary-disjointness"
kind = "lemma"
title = "Prepared boundaries, the comparison boundary, and key disjointness"
order = 272
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint", "AlgebraicGeometry.TwoOpenSide.admissibleBlowup", "AlgebraicGeometry.TwoOpenSide.isIso_comparisonFst_restrict_isoOpen", "AlgebraicGeometry.TwoOpenSide.isProper_comparisonFst", "AlgebraicGeometry.TwoOpenSide.isProper_comparisonSnd", "AlgebraicGeometry.exists_admissibleBlowup_comparisonBoundary_subset_selfBoundary", "AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide", "AlgebraicGeometry.exists_prepared_twoOpenSide"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-isomorphism-near-closure", "def-nagata-maximal-isomorphism-open", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-separate-constructible-closed", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "def-nagata-two-open-dense-compactifications", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-boundary-loci", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-restrict-open", "lemma-nagata-scheme-image-strict-transform", "lemma-nagata-scheme-image-universal"]
+++
Let $S$ be Noetherian, let $U\to S$ be separated and of finite type, and
let $U=U_1\cup U_2$ be an open cover such that each $U_i\to S$ is
compactifiable. Let $X_1,X_2$ be the prepared ambient schemes of
[def-nagata-two-open-prepared-boundaries], with the opens
$U_i\subseteq V_i\subseteq X_i$, the maps $\psi_i\colon V_i\to U$, the
boundary loci $Z_{i,k}$ of [def-nagata-two-open-boundary-loci] and their
closures $\overline Z_{i,k}\subseteq X_i$. Let $V_{12}$, $X_{12}$ and
$p_i\colon X_{12}\to X_i$ be as in
[def-nagata-two-open-comparison-space]. Then, for $\{i,j\}=\{1,2\}$:

1. *(Prepared sides.)* The structural morphism $X_i\to S$ is proper; the
   map $\psi_i$ is proper, extends the inclusion $U_i\hookrightarrow U$,
   satisfies $\psi_i^{-1}(U_i)=U_i$ and is an isomorphism over $U_i$; and
   $\overline Z_{i,1}\cap\overline Z_{i,2}=\varnothing$. All of this
   remains true after any further $V_i$-admissible blow-up of $X_i$, with
   $V_i,U_i,\psi_i,Z_{i,k}$ transported along the isomorphism over $V_i$
   and $\overline Z_{i,k}$ replaced by the closures in the new scheme.
2. *(Comparison projections.)* Both projections $p_i$ are proper. The
   canonical morphism $V_{12}\to p_i^{-1}(V_i)$ is an isomorphism, and
   under it $p_i^{-1}(V_i)\to V_i$ is the base change of
   $\psi_j\colon V_j\to U$ along $\psi_i\colon V_i\to U$. In particular
   $p_1$ is an isomorphism over the open $\psi_1^{-1}(U_2)\subseteq V_1$,
   which contains $Z_{1,2}$.
3. *(Improved comparison.)* Let

   $$
   X_1^{\mathrm{cmp}}\longrightarrow X_1
   $$

   be a $V_1$-admissible blow-up as provided by
   [lemma-nagata-isomorphism-near-closure] for the proper map $p_1$, the
   open $V_1$ and the closed subset $Z_{1,2}\subseteq V_1$ (for instance
   $\mathsf{IsoBl}_{V_1,Z_{1,2}}(p_1)$ of
   [def-nagata-isomorphism-near-closure]).
   Replace $X_1$ by $X_1^{\mathrm{cmp}}$ (transporting
   $V_1,U_1,\psi_1,Z_{1,k}$, and taking the closures $\overline Z_{1,k}$ in
   $X_1^{\mathrm{cmp}}$), and replace $X_{12}$ and $p_1,p_2$ by the
   comparison space and projections of
   [def-nagata-two-open-comparison-space] formed with $X_1^{\mathrm{cmp}}$;
   this new $X_{12}$ is the strict transform of the old one. For the new
   data, (1) and (2) still hold, and moreover $p_1$ is an isomorphism over
   an open neighbourhood of $\overline Z_{1,2}$ in $X_1$.
4. *(Key disjointness.)* For the improved data of (3), the projection
   $p_2$ maps $p_1^{-1}(\overline Z_{1,2})$ into $\overline Z_{2,2}$.
   Consequently, inside $X_1\times_SX_2$ one has

   $$
   X_{12}\cap
   (\overline Z_{1,2}\times_S\overline Z_{2,1})
   =\varnothing.
   $$

From now on $X_1$, $X_{12}$ and $p_1,p_2$ always denote the improved data
of (3).
