+++
kind = "proof"
of = "corollary-extension-proper-target"
order = 1435
uses = ["lemma-making-open-schematically-dense", "definition-quasi-domination", "theorem-extension-partial-section"]
+++
A map $U\to Y$ is the same as a section over $U$ of the projection
$Y\times_SX\to X$. The theorem extends this section to an open of a
blow-up, and properness of $Y$ forces this open to be everything.

Apply Theorem [theorem-extension-partial-section], with $T=X$ and $V=U$, to the section
$(f,\mathrm{id}):U\to Y\times_SX$ of the proper projection to $X$.
This gives an extension on an open $W\subseteq X'$ whose graph is
closed in $Y\times_SX'$. The open $W$ is dense, because it contains the
inverse image of $U$, which is dense in $X'$. Since $Y\to S$ is
proper, the observation after
Definition [definition-quasi-domination] shows that $W=X'$.
