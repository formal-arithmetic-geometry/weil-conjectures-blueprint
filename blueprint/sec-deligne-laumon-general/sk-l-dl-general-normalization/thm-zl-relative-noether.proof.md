+++
kind = "proof"
of = "thm-zl-relative-noether"
uses = ["def-sbc-affine-space", "def-weil-pbc-scheme-conventions", "def-zl-localized-coordinates", "lem-zl-affine-partition", "lem-zl-spread-normalization"]
+++
All schemes under consideration are Noetherian. We use induction
on closed subsets of the target, with their reduced structures.
This induction terminates because a Noetherian space has no infinite
strictly descending chain of closed subsets.

For a nonempty reduced target $Y$, take the finitely many
irreducible components. In each component choose a nonempty
affine open avoiding all the other components. These give disjoint
integral affine opens $V_j=\operatorname{Spec}A_j$ of $Y$;
their union contains every generic point of $Y$.
For each $j$, apply [lem-zl-affine-partition] to
$X_0\times_{Y_0}V_j$. The resulting finitely many reduced affine
pieces are $\operatorname{Spec}B_{ji}$, with $B_{ji}$
a finitely generated $A_j$-algebra.

Apply [lem-zl-spread-normalization] to every $A_j\to B_{ji}$.
For fixed $j$, multiply the finitely many nonzero denominators
to obtain $s_j$. Localizing the resulting finite module
generators once more preserves their generation, so all pieces
over $D(s_j)\subset V_j$ simultaneously have finite maps to
relative affine spaces. These maps are the explicit
[def-zl-localized-coordinates] maps.
The open subset $V=\bigcup_jD(s_j)$ still contains every generic
point of $Y$, and its pieces and their inverse images give the
required finite partitions over $V$.

The complement $Y\setminus V$ is a proper closed subset.
Apply the induction hypothesis to the restriction of $f$ over
this complement. Reduced source pieces factor through the reduced
target, since a nilpotent section maps to zero in a reduced ring.
Combining those partitions with the pieces over $V$ gives finite
partitions of source and target by locally closed reduced
subschemes, as in [def-weil-pbc-scheme-conventions].
Finally the standard coordinate projections factor each
$\mathbf A^d_{Y'_0}\to Y'_0$ into the $d$ relative affine-line
projections of [def-sbc-affine-space].
