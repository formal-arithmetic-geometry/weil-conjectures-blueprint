+++
kind = "proof"
of = "lemma-gluing-after-admissible-blow-ups"
order = 1450
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-making-open-schematically-dense", "definition-strict-transform", "lemma-products-composites-u-admissible-blow", "theorem-elimination-indeterminacy"]
+++
We glue the $T_i$ along the closure of $U$ in $T_1\times_ST_2$, after
blow-ups that make this closure open in both. The glued scheme is
separated because the closure is closed in the product.

Let $G$ be the schematic closure of $U$ in $T_1\times_ST_2$.
Theorem [theorem-elimination-indeterminacy], applied to the two
projections, makes the strict transforms of $G$ opens in suitable
blow-ups of the two sides. Blowing up the product of the two
pulled-back centers on $G$ gives a common refinement, and
Lemma [lemma-products-composites-u-admissible-blow] extends these
further centers from the resulting opens to each side, so that the
resulting scheme $G'$ is an open in both $T_i'$.

The map $G'\to T_1'\times_ST_2'$ is a closed immersion. It is an
immersion, and it is proper because $G'\to G$ is proper,
$G\subseteq T_1\times_ST_2$ is closed, and the modified product
is separated over the original product. We glue the two $T_i'$ along
$G'$. The glued scheme $T$ is covered by $T_1'$ and $T_2'$. The
diagonal of $T$ restricted to $T_i'\times_ST_j'$ is the diagonal of
$T_i'$ for $i=j$ and the graph $G'$ for $i\neq j$. Both are closed, so
$T$ is separated. It is of finite type because it has a finite
cover by opens of finite type.

Suppose that $U$ is dense in both $T_i$. The complement of the
exceptional divisor of a blow-up is schematically dense, as in the proof
of Lemma [lemma-making-open-schematically-dense], and it contains
the inverse image of $U$ as a dense open. Hence $U$ is dense in each
$T_i'$, and so in $T$. This construction is [Stacks, [0F3X](https://stacks.math.columbia.edu/tag/0F3X)].
