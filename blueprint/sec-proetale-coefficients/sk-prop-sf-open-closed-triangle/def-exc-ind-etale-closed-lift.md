+++
id = "def-exc-ind-etale-closed-lift"
kind = "definition"
title = "The ind-etale lift along a closed subscheme"
lean = ["Algebra.ClosedLift.Index", "Algebra.ClosedLift", "Algebra.ClosedLift.toAlgHom", "Algebra.ClosedLift.map", "Algebra.ClosedLift.reduction"]
order = 1128
uses = ["def-weil-pbc-ind-etale-algebra"]
+++
For a ring $A$ and an $A$-algebra $\overline C$, let
$\mathcal N_A(\overline C)$ have objects factorizations
$A\to B\to\overline C$, with $B/A$ etale of finite presentation, and
morphisms the compatible $A$-algebra maps. Define the $A$-algebra
$$
 H_A(\overline C)=\varinjlim_{\mathcal N_A(\overline C)}B
$$
and retain its map $H_A(\overline C)\to\overline C$. An $A$-algebra map
$\overline C\to\overline C'$ acts by postcomposition on the indexing
categories, and hence defines a map $H_A(\overline C)\to H_A(\overline C')$;
these maps preserve identities and composition. If $I\subset A$ is an ideal
and $\overline C$ is an $A/I$-algebra (in the applications an ind-etale one),
the retained map kills $IH_A(\overline C)$ and so induces the reduction
$$
 H_A(\overline C)/IH_A(\overline C)\longrightarrow\overline C .
$$
