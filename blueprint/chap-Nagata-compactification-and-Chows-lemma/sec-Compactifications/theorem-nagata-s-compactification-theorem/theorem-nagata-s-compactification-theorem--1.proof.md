+++
kind = "proof"
of = "theorem-nagata-s-compactification-theorem--1"
order = 1404002
uses = ["lemma-affine-covers-dense-intersection", "proposition-compactifying-union-two-opens", "lemma-schematic-closure-uniqueness"]
+++
First construct a compactification without the density condition. Over
a Noetherian base, choose a finite affine cover with dense total
intersection as in [lemma-affine-covers-dense-intersection]. The empty
union is compactifiable, and each affine member is compactifiable.
Inductively apply [proposition-compactifying-union-two-opens] to the
nonempty partial union and the next member: their overlap contains the
dense total intersection. This gives
`AlgebraicGeometry.nagataCompactification_of_isNoetherian`.

For a separated morphism of finite presentation over a qcqs base, write
$S$ as a cofiltered limit of Noetherian schemes with affine transition
maps. Descend the morphism, including its separatedness, to one stage,
compactify there, and pull back to $S$. Open immersions and proper
morphisms are preserved by base change, so this gives
`AlgebraicGeometry.nagataCompactification_of_locallyOfFinitePresentation`.
The base change step is `AlgebraicGeometry.HasCompactification.of_isPullback`.

For the given finite type morphism, choose a closed immersion
$X\hookrightarrow X_0$ over $S$ with $X_0\to S$ separated and of finite
presentation, using `AlgebraicGeometry.Scheme.Hom.exists_fpEnvelope`.
Compactify $X_0$ by the preceding step and take the scheme-theoretic
image of $X$ in its compactification. By
[lemma-schematic-closure-uniqueness], $X$ is open in this image, which
is proper over $S$ since it is closed in a proper $S$-scheme. This
constructs a compactification of $f$, from which
`AlgebraicGeometry.NagataCompactification` chooses one.

Finally, replace this chosen compactification by the scheme-theoretic
image of its open immersion. This is
`AlgebraicGeometry.Compactification.denseRefinement`: the image factor
is an open immersion and is scheme-theoretically dominant, while the
map to $S$ remains proper. Its density is
`AlgebraicGeometry.Compactification.isDense_denseRefinement`, and this
is the witness used by `AlgebraicGeometry.exists_isDense_compactification`.
The open immersion is quasi-compact because its composite with the
proper morphism is the quasi-compact morphism $f$, as expressed by
`AlgebraicGeometry.Compactification.quasiCompact_openImmersion`.
