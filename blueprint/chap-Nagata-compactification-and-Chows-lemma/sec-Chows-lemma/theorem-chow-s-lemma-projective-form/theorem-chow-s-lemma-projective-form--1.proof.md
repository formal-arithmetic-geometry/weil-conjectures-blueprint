+++
kind = "proof"
of = "theorem-chow-s-lemma-projective-form--1"
order = 1468004
uses = ["prose-A-23", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open"]
+++
First embed $X$ as a closed subscheme of a separated scheme $Y$ of
finite presentation over $S$. Write the affine scheme $S$ as a limit
of Noetherian affine schemes with affine transition maps, and descend
$Y\to S$ to a separated morphism $Y_0\to S_0$ of finite presentation.
These are the approximation steps recalled in [prose-A-23].

The Noetherian Chow construction gives a proper surjection
$Y'_0\to Y_0$ and an immersion $Y'_0\to\mathbf P(N;S_0)$ with $N$
finite. In that construction one takes schematic closures of affine
pieces and of their common graph, using
[lemma-schematic-closure-uniqueness], and glues the local maps by
[lemma-uniqueness-maps-dense-open]. Pull back first to $Y$ and then
to the closed subscheme $X$. Properness and surjectivity are preserved,
and base change for projective space gives an immersion
$i_S:\widetilde X\to\mathbf P(N;S)$ over $S$.

The composite $q_Si_S=f\pi$ is proper. Since $q_S$ is separated,
`AlgebraicGeometry.IsProper.of_comp` makes $i_S$ proper. A proper
immersion is a closed immersion by
`AlgebraicGeometry.IsClosedImmersion.of_universallyClosed`.
This is the construction in
`AlgebraicGeometry.ProjectiveDomination.nonempty_of_isAffine`.
