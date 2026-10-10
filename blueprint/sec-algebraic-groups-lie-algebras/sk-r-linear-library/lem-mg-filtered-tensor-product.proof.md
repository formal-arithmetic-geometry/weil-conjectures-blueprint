+++
kind  = "proof"
of    = "lem-mg-filtered-tensor-product"
+++
First filter $V\otimes W$ by the subspaces $V_i\otimes W$. Tensoring
vector spaces over a field is exact, so

$$
(V_i\otimes W)/(V_{i-1}\otimes W)\simeq A_i\otimes W.
$$

Inside this quotient use the filtration
$A_i\otimes W_0\subseteq\cdots\subseteq A_i\otimes W_u$, whose
successive quotients are $A_i\otimes B_j$. Pull these subspaces back to
$V_i\otimes W$, and do this successively for $i=1,\ldots,t$. All
maps are Weil-equivariant because both series in
[def-mg-weil-composition-series] consist of Weil-stable subspaces.
The resulting concatenated filtration has precisely the asserted
quotients.
