+++
kind  = "proof"
of    = "sk-thm-chow-projective"
uses = ["thm-chow-lemma", "sk-thm-nagata-compactification"]
+++
The version of Chow's lemma in Stacks 0202 gives a proper surjection
$\pi:\widetilde X\to X$ and an immersion $i_S:\widetilde X\to\mathbf P^n_S$
over $S$ for every separated $X\to S$ of finite type with $S$ qcqs. Here
$f\pi$ is proper. A map from a proper $S$-scheme to a separated $S$-scheme is
proper, because its graph is closed and the projection of the product to the
target is proper. Therefore $i_S$ is a proper immersion, hence a closed
immersion.

For the second assertion, factor $i_X$ as the graph of $\pi$ followed by the
base change of $i_S$:

$$
\widetilde X\longrightarrow\widetilde X\times_SX\longrightarrow
\mathbf P^n_S\times_SX.
$$

The first arrow is closed because $X\to S$ is separated, and the second is
closed because $i_S$ is. Their composite is $i_X$. Hence $\pi$, which is $i_X$
followed by the projection $\mathbf P^n_X\to X$, and $f\pi=q_Si_S$ are
projective.

The form of Chow's lemma used here, for separated $X\to S$ of finite type over
a qcqs base, follows from the Noetherian one ([thm-chow-lemma]). Embed $X$ by
Stacks 01ZJ as a closed subscheme of some $X_0$ that is separated and of finite
presentation over $S$ ([prop-nagata-finite-type-closed-in-fp]), descend $X_0$ to a
Noetherian stage ([prop-nagata-noetherian-inverse-system], [lemma-nagata-separated-eventually]), apply the Noetherian
form of Chow's lemma there, and base change the resulting proper surjective
cover to $S$. Pulling this cover back to the closed subscheme $X$ gives a
source that is closed in the source of the cover of $X_0$, so its map to
projective space is still an immersion; its map to $X$ is proper and
surjective by base change.
