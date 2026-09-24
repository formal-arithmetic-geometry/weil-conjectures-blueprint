+++
id = "lemma-nagata-key-boundary-disjointness"
kind = "lemma"
title = "Prepared boundaries, the comparison boundary, and key disjointness"
order = 545
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint", "AlgebraicGeometry.TwoOpenSide.admissibleBlowup", "AlgebraicGeometry.TwoOpenSide.isProper_comparisonFst", "AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide", "AlgebraicGeometry.exists_prepared_twoOpenSide"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-graph-extension", "def-nagata-isomorphism-near-closure", "def-nagata-maximal-isomorphism-open", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-separate-constructible-closed", "def-nagata-strict-transform", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "def-nagata-two-open-dense-compactifications", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-blowup-proper", "lemma-nagata-boundary-disjoint-persists", "lemma-nagata-boundary-loci", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-graph-extension", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-isomorphism-near-closure", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-restrict-open", "lemma-nagata-scheme-image-strict-transform", "lemma-nagata-scheme-image-universal", "lemma-nagata-separate-constructible-closed", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-two-open-dense-compactifications", "prop-nagata-global-blowup-cover-independent", "thm-nagata-global-blowup-proper"]
+++
Inside $X_1\times_SX_2$ one has

$$
X_{12}\cap
(\overline Z_{1,2}\times_S\overline Z_{2,1})
=\varnothing.
$$

## Proof

Put $C=p_1^{-1}(\overline Z_{1,2})$. By
[lemma-nagata-key-boundary-disjointness], $Z_{12,2}$ is dense in
$C$. The definition of the comparison boundary and
[lemma-nagata-key-boundary-disjointness] give

$$
p_2(Z_{12,2})\subseteq Z_{2,2}\subseteq\overline Z_{2,2}.
$$

Equivalently, $Z_{12,2}$ is contained in the closed inverse image
$p_2^{-1}(\overline Z_{2,2})$. Because it is dense in $C$, this closed
inverse image also contains $C$. Thus
$p_2(C)\subseteq\overline Z_{2,2}$.
The two closed subschemes $\overline Z_{2,2}$ and
$\overline Z_{2,1}$ are disjoint by
[lemma-nagata-key-boundary-disjointness]. Thus no point of $C$ can map into
$\overline Z_{2,1}$, which is precisely the asserted empty intersection.

## Properties of the chosen graph extensions

Each replacement $X_i\to X_i^{\mathrm{old}}$ is $U_i$-admissible;
the resulting structural morphism $X_i\to S$ is proper;
$\psi_i$ is proper, extends the inclusion $U_i\hookrightarrow U$, satisfies
$\psi_i^{-1}(U_i)=U_i$, and is an isomorphism over $U_i$.

*Proof.*
For each $i$, [lemma-nagata-graph-extension] says that the selected
replacement $X_i\to X_i^{\mathrm{old}}$ is $U_i$-admissible and that its
associated map $\psi_i$ is proper, extends $U_i\hookrightarrow U$, has
inverse image $\psi_i^{-1}(U_i)=U_i$, and is an isomorphism there. The
old structural map $X_i^{\mathrm{old}}\to S$ is proper by the selected
compactification, while an admissible blow-up is proper. Their composite,
which is the structural map of the replacement, is therefore proper.

## Properties of the prepared boundary closures

The constructed replacement $X_i^{\mathrm{prep}}\to X_i^{\mathrm{old}}$
is $V_i$-admissible, the closures
$\overline Z_{i,i}$ and $\overline Z_{i,j}$ are disjoint, and the open
$V_i$ together with the proper map $\psi_i$ is unchanged. The new
structural morphism $X_i^{\mathrm{prep}}\to S$ is proper.

*Proof.*
By [lemma-nagata-boundary-loci], the subsets $Z_{i,i}$ and
$Z_{i,j}$ are disjoint constructible subsets closed in $V_i$. Apply the
property of the explicitly constructed separation blow-up. It is
$V_i$-admissible, so the selected isomorphism over $V_i$ transports
$\psi_i$ without changing it. The conclusion of
[lemma-nagata-separate-constructible-closed] is exactly the
disjointness of the two closures. The separation blow-up is proper by
[lemma-nagata-blowup-proper]; composing it with the original proper
morphism $X_i^{\mathrm{old}}\to S$ proves that
$X_i^{\mathrm{prep}}\to S$ is proper.

## Properness of the comparison projections

Both projections $p_i\colon X_{12}\to X_i$ are proper.

*Proof.*
Apply [lemma-nagata-scheme-image-universal] to
$V_{12}\to X_1\times_SX_2$. It gives the canonical closed immersion
$\iota_{12}\colon X_{12}\hookrightarrow X_1\times_SX_2$ occurring in
[def-nagata-two-open-comparison-space]. For
$\{i,j\}=\{1,2\}$, the morphism $X_j\to S$ is proper by
[lemma-nagata-key-boundary-disjointness]; hence the projection
$\pi_i\colon X_1\times_SX_2\to X_i$ is its proper base change. The
equality $p_i=\pi_i\circ\iota_{12}$ expresses $p_i$ as a composite of
proper morphisms, so $p_i$ is proper.

## Distinguished comparison boundary

Define

$$
Z_{12,2}=(p_1|_{V_{12}})^{-1}(Z_{1,2}).
$$

## Improved first comparison projection

Let $N_2=\operatorname{IsoOpen}(\psi_2)\subseteq U$. Apply
$\mathsf{IsoBl}_{V_1,Z_{1,2}}(p_1)$ to the proper projection
$p_1\colon X_{12}\to X_1$. Define $X_1^{\mathrm{cmp}}$ to be this
constructed blow-up and define $X_{12}^{\mathrm{cmp}}$ to be the strict
transform of $X_{12}$. Transport $V_1$, all four boundary loci, and the
projection maps along the selected isomorphism over $V_1$, and thereafter
retain the notation $X_1,X_{12},p_i$ for the transported data.

## The two descriptions of the comparison boundary agree

Inside $V_{12}$ one has

$$
Z_{12,2}=(p_2|_{V_{12}})^{-1}(Z_{2,2}).
$$

*Proof.*
Let $z=(v_1,v_2)$ be a point of $V_{12}=V_1\times_UV_2$. The fibre-product
equality gives $\psi_1(v_1)=\psi_2(v_2)=u\in U$. Since
$Z_{1,2}=V_1\times_UZ_2$ and $Z_{2,2}=V_2\times_UZ_2$, membership in either
inverse image is equivalent to $u\in Z_2$. Scheme-theoretically, both
sides are the pullback of the closed subscheme $Z_2\hookrightarrow U$ along
the equal composites $V_{12}\rightrightarrows U$. The canonical
associativity isomorphisms for fibre products therefore identify the two
closed subschemes.

## Restriction of the comparison image over the proper-extension open

For $\{i,j\}=\{1,2\}$, the canonical morphism

$$
V_{12}=V_1\times_UV_2\longrightarrow p_i^{-1}(V_i)
$$

is an isomorphism. Under this identification,
$p_i^{-1}(V_i)\to V_i$ is the base change of
$\psi_j\colon V_j\to U$ along $\psi_i\colon V_i\to U$.

*Proof.*
Restrict the scheme-theoretic image defining $X_{12}$ to the open target
$V_i\times_SX_j\subseteq X_i\times_SX_j$. The inverse image of this
open in $V_{12}$ is all of $V_{12}$, so
[lemma-nagata-scheme-image-restrict-open] identifies
$p_i^{-1}(V_i)$ with the scheme-theoretic image of

$$
V_{12}\longrightarrow V_i\times_SX_j.
$$

The map $V_{12}\to V_i\times_SV_j$ is the pullback of the diagonal
$U\to U\times_SU$; it is therefore a closed immersion because
$U\to S$ is separated. Composing with the open immersion
$V_i\times_SV_j\to V_i\times_SX_j$ shows that the displayed map is an
immersion. It is also proper: its composite to $V_i$ is the base change
of the proper morphism $\psi_j$, while
$V_i\times_SX_j\to V_i$ is separated; apply
[lemma-nagata-proper-to-separated-target]. A proper immersion is a
closed immersion, so
[lemma-nagata-scheme-image-of-closed-immersion] identifies its
scheme-theoretic image with $V_{12}$ itself.
The first projection of the fibre square is the displayed map to $V_i$,
and its second component is the map to $V_j$. The universal property of
the fibre product gives the inverse identification with the base change of
$\psi_j$ along $\psi_i$, so the description of the projection is exactly
the one asserted.

## Properties of the improved first comparison projection

The constructed map $X_1^{\mathrm{cmp}}\to X_1^{\mathrm{old}}$ is
$V_1$-admissible, the transported $p_1$ is an isomorphism over an open
neighbourhood of $\overline Z_{1,2}$, and all previously established
boundary-disjointness relations still hold.

*Proof.*
By [lemma-nagata-key-boundary-disjointness], the restriction of
$p_1$ over $V_1$ is the base change
$V_1\times_UV_2\to V_1$ of $\psi_2$. The maximal isomorphism open $N_2$
contains $Z_2$ by [lemma-nagata-boundary-loci] and
[lemma-nagata-maximal-isomorphism-open]; hence $p_1$ is an
isomorphism over $\psi_1^{-1}(N_2)$, an open containing $Z_{1,2}$.

The subset $Z_{1,2}$ is closed in $V_1$, and $p_1$ is proper by
[lemma-nagata-key-boundary-disjointness]. Therefore the property
of $\mathsf{IsoBl}_{V_1,Z_{1,2}}(p_1)$ gives the asserted isomorphism near
the closure. The new comparison scheme is the strict transform by
[lemma-nagata-scheme-image-strict-transform]. Finally
[lemma-nagata-boundary-disjoint-persists] preserves every earlier
disjointness relation under this further $V_1$-admissible blow-up.

## Density over the prepared boundary

The subset $Z_{12,2}$ is dense in
$p_1^{-1}(\overline Z_{1,2})$.

*Proof.*
Choose an open neighbourhood $N\subseteq X_1$ of
$\overline Z_{1,2}$ over which $p_1$ is an isomorphism, as supplied by
[lemma-nagata-key-boundary-disjointness]. Then
$p_1^{-1}(\overline Z_{1,2})$ lies in $p_1^{-1}(N)$, and the restriction

$$
p_1^{-1}(\overline Z_{1,2})\longrightarrow\overline Z_{1,2}
$$

is an isomorphism. By the definition of $Z_{12,2}$, its inverse image under
this isomorphism is $Z_{1,2}$. Since $Z_{1,2}$ is dense in its closure
$\overline Z_{1,2}$, the inverse image $Z_{12,2}$ is dense in
$p_1^{-1}(\overline Z_{1,2})$.
