+++
kind = "proof"
of = "sk-lem-nagata-sketch-graph"
uses = ["sk-lem-nagata-sketch-elimination", "lemma-nagata-scheme-image-strict-transform", "sk-lem-nagata-sketch-closure"]
+++
Let $G$ be the schematic closure of the graph of $V\to M$ in
$Y\times_SM$. Its projection to $Y$ is separated of finite type,
and it is an isomorphism over $V$. By
Theorem [sk-lem-nagata-sketch-elimination], after a $V$-admissible blow-up
$Y'\to Y$ its strict transform $G'$ is an open $V'\subseteq Y'$.
This strict transform is the closure of the graph of $V\to M$ in
$Y'\times_SM$, since both are the closure of the same graph outside
the exceptional divisor [Stacks, Tag 0F3Y](https://stacks.math.columbia.edu/tag/0F3Y). Hence $G'$ is closed in
$Y'\times_SM$, whose projection to $M$ is proper, and so
$V'\simeq G'\to M$ is proper. Over $V\subseteq M$, the graph of the
inclusion $V\to Y'$ is already closed in $Y'\times_SV$, because $Y'$ is
separated over $S$. Hence the inverse image of $V$ under $\psi$ is this
graph, that is, $V$ itself. See also [Stacks, Tag 0F3Z](https://stacks.math.columbia.edu/tag/0F3Z).
