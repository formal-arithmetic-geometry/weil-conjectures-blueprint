+++
kind = "proof"
of = "sk-cor-nagata-sketch-proper-extension"
uses = ["sk-lem-nagata-sketch-elimination", "sk-lem-nagata-boundary-divisor", "sk-lem-nagata-sketch-blowups", "sk-lem-nagata-sketch-closure", "sk-thm-app-nagata-conrad", "sk-def-app-nagata-quasidomination"]
+++
Apply Theorem [sk-thm-app-nagata-conrad], with $V=U$, to the section
$(f,\mathrm{id}):U\to Y\times_SX$ of the proper projection to $X$.
It gives an extension on an open $W\subseteq X'$ whose graph is
closed in $Y\times_SX'$. The inverse image of $U$ is dense in
$X'$, so $W$ is dense. The observation after
Definition [sk-def-app-nagata-quasidomination], applied to the proper
map $Y\to S$, gives $W=X'$.
