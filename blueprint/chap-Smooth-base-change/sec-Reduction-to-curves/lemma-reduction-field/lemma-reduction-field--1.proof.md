+++
kind = "proof"
of = "lemma-reduction-field--1"
order = 675002
uses = ["lemma-identity-pasting", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "lemma-injectivity-base-change-map-degree", "lemma-schematic-closure-uniqueness"]
+++
By étale locality, a failure remains after restricting $Y$ to an affine
open $T$ (`AlgebraicGeometry.Etale.exists_isAffineOpen_not_baseChangeProperty`).
The lower-degree hypotheses remain valid after this restriction. Choose
a failing qcqs direct image $f:Z\to T$ and a coefficient sheaf $M$; the
scheme $Z$ is then qcqs. Lemma
[lemma-injectivity-base-change-map-degree] makes the degree-$q$ map
injective. Since geometric stalks detect isomorphisms, some geometric
stalk of its target contains an element $\xi$ outside its image.

For a qcqs scheme $Z_1$ over $Z$, let $P(Z_1)$ mean that the image of
$\xi$ under the transition map is still outside the image of the base
change map for $Z_1\to T$ and the pullback of $M$. This is
`AlgebraicGeometry.Etale.SurvivesBaseChange`. Identity and pasting
[lemma-identity-pasting] give $P(Z)$ and compatibility of the transition
maps. Topological invariance makes $P$ invariant under thickenings, and
continuity of higher direct images makes it pass to cofiltered limits
with affine transition maps. It fails for the empty scheme, whose
target sheaf is zero.

If $V\subset Z_1$ is a quasi-compact open with closed complement $W$,
write $j:V\to Z_1$ and $i:W\to Z_1$. Embed the restriction of the
coefficient sheaf $M_1$ to $V$ into an injective sheaf $J$. The map

$$
M_1\longrightarrow j_*J\oplus i_*i^{-1}M_1
$$

is injective, and so is its map on base change cokernels by
[lemma-injectivity-base-change-map-degree]. Thus a surviving class is
detected in one of the two summands. For the closed summand, exactness
and base change for finite direct images [lemma-finite-morphisms]
give $P(W)$. For the open summand, injective acyclicity
[lemma-acyclic-resolutions] identifies $j_*J[0]$ with $Rj_*J$.
The lower-degree isomorphisms and degree-$q$ injectivity make the derived
comparison on the targets injective in degree $q$. Naturality with
respect to $j^{-1}M_1\to J$ then gives $P(V)$. These verifications are
assembled in `AlgebraicGeometry.Etale.isQcqsLocalProperty_survivesBaseChange`.

Apply `AlgebraicGeometry.exists_spec_field_of_isQcqsLocalProperty`.
Its proof uses Zorn's lemma on ideal sheaves to obtain a minimal closed
subscheme carrying $P$, using affine limits for intersections of chains.
Closed subschemes are compared through their scheme-theoretic images
[lemma-schematic-closure-uniqueness]. Every nonempty quasi-compact open
of the minimal subscheme has $P$. Choose a nonempty affine open
$\operatorname{Spec}A$ and a minimal prime $\mathfrak p$ of $A$.
The scheme $\operatorname{Spec}A_{\mathfrak p}$ is a cofiltered limit of
nonempty basic opens, so it has $P$. Its residue field $\Omega$ gives a
surjective closed immersion
$\operatorname{Spec}\Omega\to\operatorname{Spec}A_{\mathfrak p}$, and
invariance under thickenings gives $P(\operatorname{Spec}\Omega)$.
The pulled back sheaf and the composite
$\operatorname{Spec}\Omega\to Z\to T$ therefore give the required
failure, recorded by `AlgebraicGeometry.Etale.FieldFailure`.
