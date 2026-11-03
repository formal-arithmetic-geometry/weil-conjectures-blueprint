+++
kind = "proof"
of = "lem-weil-pbc-constructible-closed-generic-criterion"
uses = ["def-constructible-stratification", "prop-constructible-open-closed", "prop-constructible-pullback"]
+++
Induct on closed subsets $C\subseteq X$ (Noetherian induction: closed subsets satisfy the descending chain condition), proving the strengthened claim that $i^*F$ is constructible for every closed immersion $i:Z\to X$ with image contained in $C$. Such a $Z$ is Noetherian, being a closed subscheme of the Noetherian $X$.

If $Z$ is empty its sheaves are zero, hence constructible. Otherwise choose the dense open $U\subseteq Z$ supplied by the hypothesis; it is nonempty. Let $i':Z'\to Z$ be the reduced closed complement of $U$. The image $C'$ of $i\circ i'$ in $X$ is a proper closed subset of $C$: the image of a point of $U$ lies in $C$ but not in $C'$, $i$ being injective. By the induction hypothesis applied to $i\circ i'$, and compatibility of inverse images with composition, the restriction of $i^*F$ to $Z'$ is constructible.

On $U$ the sheaf $i^*F|_U$ is finite locally constant, hence constructible (one-stratum stratification) [prop-constructible-pullback]. By the open-closed characterization of constructibility [prop-constructible-open-closed], [def-constructible-stratification], $i^*F$ is constructible on $Z$. Finally take $C=X$ and $i=\mathrm{id}_X$, using $\mathrm{id}^*F\cong F$.
