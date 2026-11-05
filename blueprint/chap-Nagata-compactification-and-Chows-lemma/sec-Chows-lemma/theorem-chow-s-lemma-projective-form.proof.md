+++
kind = "proof"
of = "theorem-chow-s-lemma-projective-form"
order = 1472
+++
We take the immersion into projective space given by the Stacks
Project and show that properness of $X$ makes it closed. The second
assertion then follows by writing $i_X$ as a graph followed by a base
change of $i_S$.

The version of Chow's lemma in [Stacks, [0202](https://stacks.math.columbia.edu/tag/0202)] gives a proper
surjection $\pi:\widetilde X\to X$ and an immersion
$i_S:\widetilde X\to\mathbf P^n_S$ for every separated
$X\to S$ of finite type with $S$ qcqs. It is deduced from the Noetherian
case by the approximation argument in the proof of
Theorem [theorem-nagata-s-compactification-theorem], using the embedding of $X$ into a
scheme of finite presentation [Stacks, [01ZJ](https://stacks.math.columbia.edu/tag/01ZJ)]. In our situation, moreover, $f$ and $\pi$ are proper, so $\widetilde X$
is proper over $S$. Now a map from a proper $S$-scheme to a separated
$S$-scheme is proper, because its graph is closed and the projection of
the product to the target is proper. Hence $i_S$ is a proper immersion. Its image is therefore closed, and
$i_S$ is a closed immersion.

For the second assertion, we factor $i_X$ as the graph of $\pi$
followed by the base change of $i_S$:

$$
\widetilde X\longrightarrow\widetilde X\times_SX
\longrightarrow\mathbf P^n_S\times_SX.
$$

The first arrow is closed because $X\to S$ is separated, and the
second is closed because $i_S$ is. Their composite is $i_X$. Since
$\pi$ is $i_X$ followed by the projection $\mathbf P^n_X\to X$, it is
projective, and so is $f\pi=q_Si_S$.
