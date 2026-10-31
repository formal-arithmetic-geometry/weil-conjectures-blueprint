+++
kind = "proof"
of = "sk-thm-chow-projective"
uses = ["thm-chow-lemma", "sk-thm-nagata-compactification"]
+++
The version of Chow's lemma in [Stacks, Tag 0202](https://stacks.math.columbia.edu/tag/0202) gives a proper
surjection $\pi:\widetilde X\to X$ and an immersion
$i_S:\widetilde X\to\mathbf P^n_S$ for every separated
$X\to S$ of finite type with $S$ qcqs. It is deduced from the Noetherian
case by the approximation argument in the proof of
Theorem [sk-thm-nagata-compactification], using the embedding of $X$ into a
scheme of finite presentation [Stacks, Tag 01ZJ](https://stacks.math.columbia.edu/tag/01ZJ). Here $f\pi$ is proper. Recall that a map from a
proper $S$-scheme to a separated $S$-scheme is proper, because its graph
is closed and the projection of the product to the target is proper.
Therefore $i_S$ is a proper immersion, hence a closed immersion.

For the second assertion, we factor $i_X$ as the graph of $\pi$
followed by the base change of $i_S$:

$$
\widetilde X\longrightarrow\widetilde X\times_SX
\longrightarrow\mathbf P^n_S\times_SX.
$$

The first arrow is closed because $X\to S$ is separated, and the
second is closed because $i_S$ is. Their composite is $i_X$. Hence
$\pi$, which is $i_X$ followed by the projection $\mathbf P^n_X\to X$,
and $f\pi=q_Si_S$ are projective.
