+++
kind = "proof"
of = "sk-lem-nagata-sketch-elimination"
uses = ["thm-nagata-conrad-elimination", "sk-thm-app-nagata-conrad"]
+++
This is [Stacks, Tag 081S](https://stacks.math.columbia.edu/tag/081S). The idea is to view the inverse of
$W_U\to U$ as a partial section of $W\to T$ and to extend it by
Theorem [sk-thm-app-nagata-conrad]; the strict transform is then the graph
of the extension.

Choose a finite type ideal $\mathcal I_0$ cutting out $T\setminus U$.
Its blow-up $T_1\to T$ makes $U$ schematically dense by
Lemma [sk-lem-nagata-boundary-divisor]. The base change of $W\to T$ to
$T_1$ is separated and of finite type, and the inverse of
$W_U\to U$ is a section of it over $U$. Theorem [sk-thm-app-nagata-conrad]
over $T_1$, with $V=U$, gives a further blow-up and an extension of
this section, with closed graph, over an open containing the inverse
image of $U$. By Lemma [sk-lem-nagata-sketch-blowups] the
composite is a $U$-admissible blow-up
$\operatorname{Bl}_{\mathcal I}(T)$. Let $b:T'\to T$ be the blow-up of
$\mathcal I\mathcal I_0$, which dominates both. Pulling back, we obtain
an open $W_0\subseteq T'$ containing $b^{-1}(U)$ and a map $W_0\to W$
over $T$ whose graph $\Gamma$ is closed in $W\times_TT'$. The zero set
of $\mathcal I\mathcal I_0$ is exactly $T\setminus U$, so
$b^{-1}(U)$ is schematically dense in $T'$ and hence in $W_0$.

We use the factor $\mathcal I_0$ for the following reason: because the
center of $b$ is exactly $T\setminus U$, the strict transform $W'$ is
the schematic closure of $W_U$ in $W\times_TT'$. A center that merely
avoids $U$ would not identify the strict transform with this closure. Over $U$, the
subscheme $W_U$ is the graph of the original section, so it lies in
$\Gamma$ and $W'\subseteq\Gamma$. Conversely, $\Gamma\simeq W_0$
contains the inverse image of $U$ as a schematically dense open, so
the schematic closure of $W_U$ in $\Gamma$ is $\Gamma$. Hence
$W'=\Gamma\simeq W_0$, and $W'\to T'$ is an open immersion.
