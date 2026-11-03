+++
kind  = "proof"
of    = "lem-weil-pbc-irreducible-lisse-strata"
+++
Start with the finite lisse partition supplied by constructibility. A part $S$
is Noetherian, so [lem-weil-pbc-noetherian-finite-components] lists its
irreducible components as $C_1,\ldots,C_r$. Put

$$
 S_i=C_i\setminus\bigcup_{j<i}C_j.
$$

Each $S_i$ is open in $C_i$, and contains its generic point: an irreducible
component is not contained in the union of the other finitely many
components. Thus $S_i$ is nonempty and irreducible. These sets are disjoint
and cover $S$; they are locally closed in $S$, hence in $X$. Give them their
reduced locally closed scheme structures. Restriction of an etale
trivialization shows that $F|_{S_i}$ is still locally constant with finite
stalks. Performing this construction for the finitely many original parts
gives the required partition.
