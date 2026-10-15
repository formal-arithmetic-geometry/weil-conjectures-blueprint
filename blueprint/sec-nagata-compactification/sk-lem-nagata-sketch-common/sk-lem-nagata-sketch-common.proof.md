+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-common"
uses = ["sk-lem-nagata-sketch-blowups", "sk-lem-nagata-sketch-elimination", "sk-lem-nagata-boundary-divisor", "sk-lem-nagata-sketch-closure"]
+++
Take the schematic closure $G$ of $U$ in $T_1\times_ST_2$
([sk-lem-nagata-sketch-closure]). Apply [sk-lem-nagata-sketch-elimination]
to its two projections. The strict transforms then become opens in suitable
blow-ups of the two sides. Their further common refinement is obtained by
blowing up the product of the two pulled-back centers on $G$. Extend these
further centers from the resulting opens to each side using
[sk-lem-nagata-sketch-blowups]. The final comparison scheme $G'$ is now an
open in both $T_i'$.

Its map to $T_1'\times_ST_2'$ is a closed immersion: it is an immersion, and
is proper because $G'\to G$ is proper, $G\subseteq T_1\times_ST_2$ is
closed, and the modified product is separated over the original product.
Glue the two $T_i'$ along $G'$. On products of these two opens the diagonal is
either their own closed diagonal or the just established closed graph $G'$.
Thus the glued scheme is separated. Finite type follows from the finite open
cover. Density follows from density on each side;
[sk-lem-nagata-boundary-divisor] can ensure schematic density before
performing further modifications. This construction is Stacks 0F3X.
