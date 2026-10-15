+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-graph"
uses = ["sk-lem-nagata-sketch-elimination", "sk-lem-nagata-sketch-image-transform", "sk-lem-nagata-sketch-closure"]
+++
Form the schematic closure $G$ of the graph of $V\to M$ in $Y\times_SM$
([sk-lem-nagata-sketch-closure]). Its projection to $Y$ is separated of
finite type and is an isomorphism over $V$. By
[sk-lem-nagata-sketch-elimination] its strict transform is an open
$V'\subseteq Y'$ after an admissible blow-up. Formation of the graph closure
under this modification gives that strict transform: both are the closure of
the same graph outside the exceptional divisor (Stacks 0F3Y;
[sk-lem-nagata-sketch-image-transform]). On the other hand $G'$ is closed in
$Y'\times_SM$, whose projection to $M$ is proper. Thus $V'\simeq G'\to M$ is
proper. Its inverse image of $V$ is the closed graph over $V$, namely $V$
itself. This proves the lemma; it is also Stacks 0F3Z.
