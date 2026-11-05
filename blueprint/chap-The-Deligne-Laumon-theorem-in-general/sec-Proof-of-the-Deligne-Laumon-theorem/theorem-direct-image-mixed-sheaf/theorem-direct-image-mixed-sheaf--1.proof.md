+++
kind = "proof"
of = "theorem-direct-image-mixed-sheaf--1"
order = 1361002
uses = ["lemma-finite-quasi-finite-direct-images", "lemma-weights-exact-sequence", "lemma-weight-bounds-partitions", "proposition-relative-affine-line", "lemma-relative-noether-normalization-over-stratification", "proposition-composition-base-change-rf-shriek"]
+++
Say that a morphism has the property if it satisfies the asserted bound
for every $w$, every mixed sheaf and every nonnegative degree. Lean
proves the property by Noetherian induction on closed subsets of the
source, using the following generic step.

First, the property is stable under composition
(`AlgebraicGeometry.HasDirectImageWeightBound.comp`). A bound on the
higher direct images of sheaves gives the corresponding bound for
bounded complexes by induction along their truncation triangles.
For composable $h$ and $g$, apply this to $Rh_!F$, and then use the composition isomorphism
$Rg_!Rh_!\simeq R(gh)_!$ of
[proposition-composition-base-change-rf-shriek]. The weight bounds in
the triangles follow from [lemma-weights-exact-sequence]. This is the
truncation argument implemented by
`AlgebraicGeometry.HasDirectImageWeightBound.isMixedOfWeightsAtMost_derivedLowerShriek`.

Let $g:T_0\to Y_0$ be separated of finite type, with nonempty reduced
source. Since $T_0$ is Noetherian, it has a nonempty irreducible open.
Choose a nonempty affine open
$T_1$ inside it which maps into an affine open $W$ of $Y_0$.
Then $T_1$ is integral. Write $W=\Spec A$ and $T_1=\Spec B$, and
factor the ring map as

$$
A\longrightarrow A'=A/\ker(A\to B)\hookrightarrow B.
$$

The ring $A'$ is a domain. The generic normalization construction in
the proof of [lemma-relative-noether-normalization-over-stratification],
formalized as `AlgebraicGeometry.exists_isFinite_toIteratedAffineLine_basicOpen`,
gives a nonzero $s\in A'$ and a finite map

$$
V=\Spec B_s\longrightarrow\mathbf A^d_{D(s)},
\qquad D(s)\subset\Spec A'.
$$

Here $V$ is nonempty because $A'\to B$ is injective and $B$ is a
domain. The map $V\to Y_0$ is the composite of this finite map,
$d$ relative affine-line projections, and the immersion
$D(s)\to\Spec A'\to W\to Y_0$. The finite map and the immersion
have the property by [lemma-finite-quasi-finite-direct-images], and the
projections have it by [proposition-relative-affine-line] and
composition. This proves the affine generic step
`AlgebraicGeometry.exists_hasDirectImageWeightBound_opensι_comp_of_isAffine`.
Viewing $V$ as an open of $T_0$ gives
`AlgebraicGeometry.exists_hasDirectImageWeightBound_opensι_comp`:
the restriction of $g$ to some nonempty open has the property.

Now induct on closed subsets $Z\subset X_0$, proving the property for
$fi:T_0\to Y_0$ whenever $i:T_0\hookrightarrow X_0$ is a reduced
closed subscheme with image contained in $Z$. The empty source is
quasi-finite. Otherwise the generic step gives a nonempty open
$U\subset T_0$ on which the property holds. Give $T_0\setminus U$
its reduced closed subscheme structure. Its image in $X_0$ is a proper
closed subset of $Z$, so the induction hypothesis applies to it.
The source open–closed assertion of [lemma-weight-bounds-partitions](1),
namely `AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed`,
glues the two bounds. Finally apply that assertion to the empty open
of $X_0$ and the closed immersion $(X_0)_{\mathrm{red}}\to X_0$.
This gives the property for $f$ itself.
