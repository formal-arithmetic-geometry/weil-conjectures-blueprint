+++
kind = "proof"
of = "sk-lem-nagata-sketch-common"
uses = ["sk-lem-nagata-sketch-blowups", "sk-lem-nagata-sketch-elimination", "sk-lem-nagata-boundary-divisor", "sk-lem-nagata-sketch-closure"]
+++
Let $G$ be the schematic closure of $U$ in $T_1\times_ST_2$.
Applying Theorem [sk-lem-nagata-sketch-elimination] to the two
projections, we see that the strict transforms of $G$ become opens in
suitable blow-ups of the two sides. We get a common refinement of these
by blowing up the product of the two pulled-back centers on $G$, and we
extend these further centers from the resulting opens to each side
using Lemma [sk-lem-nagata-sketch-blowups]. The resulting scheme
$G'$ is then an open in both $T_i'$.

We claim that the map $G'\to T_1'\times_ST_2'$ is a closed immersion.
Indeed, it is an immersion, and it is proper because $G'\to G$ is proper,
$G\subseteq T_1\times_ST_2$ is closed, and the modified product
is separated over the original product. Now we glue the two $T_i'$ along
$G'$. The glued scheme $T$ is covered by $T_1'$ and $T_2'$, and the
diagonal of $T$ restricted to $T_i'\times_ST_j'$ is the diagonal of
$T_i'$ for $i=j$ and the graph $G'$ for $i\neq j$. Both are closed, and
hence $T$ is separated. It is of finite type because it has a finite
cover by opens of finite type. If $U$ is dense in both $T_i$, it is
dense in each $T_i'$, and hence dense in $T$. Indeed, the complement
of the exceptional divisor of a blow-up is schematically dense, as in
the proof of Lemma [sk-lem-nagata-boundary-divisor], and it contains
the inverse image of $U$ as a dense open. This construction is [Stacks, Tag 0F3X](https://stacks.math.columbia.edu/tag/0F3X).
