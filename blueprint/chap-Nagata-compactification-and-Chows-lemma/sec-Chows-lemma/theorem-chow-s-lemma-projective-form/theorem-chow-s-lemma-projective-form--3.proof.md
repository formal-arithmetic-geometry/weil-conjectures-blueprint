+++
kind = "proof"
of = "theorem-chow-s-lemma-projective-form--3"
order = 1468006
uses = ["prose-A-23", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open"]
+++
Embed $X$ as a closed subscheme of a separated scheme $Y$ of finite
presentation over $S$. Apply Noetherian approximation to $S$ and
descend $Y\to S$ to a separated morphism $Y_0\to S_0$ of finite
presentation, as in [prose-A-23]. The Noetherian Chow construction,
using [lemma-schematic-closure-uniqueness] and
[lemma-uniqueness-maps-dense-open], supplies a proper surjection
$Y'_0\to Y_0$ and an immersion into projective space over $S_0$.

Pull back this diagram to $S$ and then to the closed subscheme $X$ of
$Y$. Properness and surjectivity are preserved. The cartesian square
for projective space identifies the base-changed immersion, and its
restriction to the inverse image of $X$ is still an immersion. Its
composite with the projection is $f\pi$.

The Noetherian construction uses a finite set $N$ of homogeneous
coordinates. The linear closed immersion supplied by
`AlgebraicGeometry.ProjectiveSpace.exists_isClosedImmersion_finite_coordinates`
puts this space inside $\mathbf P^n_S$ for some $n\geq 0$.
Composing with it gives the assertion, as in
`AlgebraicGeometry.exists_chow_finite_type`.

If $f$ is proper, then $q_Si_S=f\pi$ is proper. Since $q_S$ is
separated, `AlgebraicGeometry.IsProper.of_comp` makes $i_S$ proper,
and `AlgebraicGeometry.IsClosedImmersion.of_universallyClosed` makes
it closed. This recovers the closed immersion in the human statement
over a general qcqs base; the same two steps occur in
`AlgebraicGeometry.exists_proper_finitePresentation_closedImmersion_envelope`.
