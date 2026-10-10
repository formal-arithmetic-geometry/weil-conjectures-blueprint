+++
kind  = "proof"
of    = "fin2-lem-lisse-dense-open"
+++
If $X$ is empty, take $U=X$.
Otherwise let $C_1,\ldots,C_t$ be all its irreducible components,
using [lem-weil-pbc-noetherian-finite-components].
For each component of maximal dimension, first remove all other
components. This gives an irreducible open $O_i$ of $X$
containing its generic point $\eta_i$. By the finite partition
in [def-weil-pbc-constructible-complexes], the stratum containing
$\eta_i$ contains a nonempty open $V_i\subset O_i$.
The restriction to $V_i$ is finite locally constant.
The $V_i$ are disjoint opens of $X$, so their finite union $U$
is open and $F|_U$ is finite locally constant.
The closed complement meets every maximal-dimensional component in
a proper closed subset. For finite-type schemes over a field such
a subset has strictly smaller dimension, by the dimension formula
for finitely generated algebras. The other components already have
smaller dimension. Hence $\dim(X\setminus U)<\dim X$.
