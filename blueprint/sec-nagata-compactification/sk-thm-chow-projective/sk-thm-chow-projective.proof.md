+++
kind  = "proof"
of    = "sk-thm-chow-projective"
uses = ["sk-thm-chow", "sk-prop-nagata-sketch-envelope", "sk-prop-nagata-sketch-approximation", "sk-prop-nagata-sketch-fp-models"]
+++
The version of Chow's lemma in Stacks 0202 gives a proper surjection
$\pi:\widetilde X\to X$ and an immersion $i_S:\widetilde X\to\mathbf P^n_S$
for every separated finite-type $X\to S$ with $S$ qcqs. Here $f\pi$ is
proper. A map from a proper $S$-scheme to a separated $S$-scheme is proper:
its graph is closed and the projection of its product to the target is
proper. Therefore $i_S$ is proper. A proper immersion is a closed immersion.

For the second assertion factor $i_X$ as the graph of $\pi$ followed by the
base change of $i_S$:

$$
\widetilde X\longrightarrow\widetilde X\times_SX
\longrightarrow\mathbf P^n_S\times_SX .
$$

The first arrow is closed because $X\to S$ is separated, and the second is
closed because $i_S$ is. Their composite is $i_X$.

The form of Chow's lemma used here follows from the Noetherian one
([sk-thm-chow]), even when $X\to S$ is not of finite presentation. Embed $X$
as a closed subscheme of a separated finitely presented $X_0$ by Stacks 01ZJ
([sk-prop-nagata-sketch-envelope]). Descend $X_0$ to a Noetherian stage
([sk-prop-nagata-sketch-approximation], [sk-prop-nagata-sketch-fp-models]),
apply the Noetherian form of Chow's lemma there, and base change its proper
surjective cover to $S$. Pull that cover back to the closed subscheme $X$.
The resulting source is closed in the source over $X_0$, so its map to
projective space is still an immersion, and properness and surjectivity of
its map to $X$ follow by base change.

Nagata's theorem and Chow's lemma play different roles. Nagata embeds $X$ as
an open subscheme of a proper scheme, keeping every point of $X$; it supplies
the compactifications and refinements used to define $Rf_!$. Chow replaces a
proper $X$ by a projective scheme mapping properly and surjectively onto it;
it supplies the projective morphisms $\pi$ and $f\pi$ in the reduction of
proper base change.
