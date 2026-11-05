+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--4"
order = 494009
uses = ["lemma-inverse-image-tensor-product--6", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Let $j:U\hookrightarrow X$ be the open complement of $Z$. Since the
underlying space of $X$ is Noetherian, $j$ is quasi-compact.
The counit $\mathbf Li^*\mathbf Ri_*K\to K$ is an isomorphism, by full
faithfulness of closed direct image and its derived functor.

The restriction $\mathbf Lj^*\mathbf Ri_*K$ is zero. Indeed, the
adjunctions $j_!\dashv\mathbf Lj^*$ and
$\mathbf Li^*\dashv\mathbf Ri_*$ identify maps into this restriction
with maps from $\mathbf Li^*j_!$, which vanishes because the two images
are disjoint. Lean records this as
`AlgebraicGeometry.ProEtale.CondensedRing.isZero_leftDerivedUpperStar_obj_rightDerivedLowerStar_obj_of_disjoint`.
Thus the restrictions to $U$ and $Z$ are bounded constructible. Apply
[lemma-inverse-image-tensor-product--6].
