+++
kind = "proof"
of = "theorem-elimination-indeterminacy"
order = 1444
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-making-open-schematically-dense", "lemma-products-composites-u-admissible-blow", "theorem-extension-partial-section"]
+++
This is [Stacks, [081S](https://stacks.math.columbia.edu/tag/081S)]. The idea is to view the inverse of
$W_U\to U$ as a partial section of $W\to T$ and to extend it by
Theorem [theorem-extension-partial-section]; the strict transform is then the graph
of the extension.

Choose a finite type ideal $\mathcal I_0$ cutting out $T\setminus U$.
Its blow-up $T_1\to T$ makes $U$ schematically dense by
Lemma [lemma-making-open-schematically-dense]. Over $T_1$, the base change of $W\to T$ to
$T_1$ is separated and of finite type, and the inverse of
$W_U\to U$ is a section of it over $U$. We may therefore apply Theorem [theorem-extension-partial-section] over $T_1$, with $V=U$, which gives a further blow-up and an extension of
this section, with closed graph, over an open containing the inverse
image of $U$. By Lemma [lemma-products-composites-u-admissible-blow] the
composite is a $U$-admissible blow-up
$\operatorname{Bl}_{\mathcal I}(T)$. Let $b:T'\to T$ be the blow-up of
$\mathcal I\mathcal I_0$, which dominates both. Pulling back to $T'$ gives
an open $W_0\subseteq T'$ containing $b^{-1}(U)$ and a map $W_0\to W$
over $T$ whose graph $\Gamma$ is closed in $W\times_TT'$. As the zero set
of $\mathcal I\mathcal I_0$ is exactly $T\setminus U$,
$b^{-1}(U)$ is schematically dense in $T'$, hence in $W_0$.

We included the factor $\mathcal I_0$ so that the center of $b$ is
exactly $T\setminus U$. Then the strict transform $W'$ is the schematic
closure of $W_U$ in $W\times_TT'$. Over $U$, the
subscheme $W_U$ is the graph of the original section, so it lies in
$\Gamma$ and $W'\subseteq\Gamma$. Conversely, $\Gamma\simeq W_0$
contains the inverse image of $U$ as a schematically dense open. Hence
the schematic closure of $W_U$ in $\Gamma$ is $\Gamma$. We conclude that
$W'=\Gamma\simeq W_0$, and $W'\to T'$ is an open immersion.
