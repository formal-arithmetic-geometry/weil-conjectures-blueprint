+++
kind = "proof"
of = "lem-weil-pbc-flat-colimit-presentation-same-universe"
+++
A module $M$ is flat if and only if $M\otimes_R-$ preserves exactness of short complexes. Let $C:X_1\to X_2\to X_3$ be an exact short complex of $R$-modules. Tensoring with the diagram $(M_j)_j$ gives a short complex of $J$-indexed diagrams $M_j\otimes_RX_1\to M_j\otimes_RX_2\to M_j\otimes_RX_3$, which is exact at each $j$ by flatness of $M_j$, hence exact as a complex of diagrams. Tensor products commute with colimits, so the colimit of this complex is $M\otimes_RX_1\to M\otimes_RX_2\to M\otimes_RX_3$. Filtered colimits of modules are exact, so this complex is exact. Hence $M$ is flat.
