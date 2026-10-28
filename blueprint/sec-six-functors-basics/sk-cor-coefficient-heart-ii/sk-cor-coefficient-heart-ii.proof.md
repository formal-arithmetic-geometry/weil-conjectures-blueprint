+++
kind  = "proof"
of    = "sk-cor-coefficient-heart-ii"
uses = ["sk-lem-coefficient-heart"]
+++
Let $K\to K'\to K''\to K[1]$ be a distinguished triangle with $K,K'$ in $\Dbc(X,\Lambda)$. By
the long exact cohomology sequence, each $\mathcal H^i(K'')$ is an extension of
$\ker(\mathcal H^{i+1}K\to\mathcal H^{i+1}K')$ by $\coker(\mathcal H^iK\to\mathcal H^iK')$. Both
are constructible by [sk-lem-coefficient-heart] (1), and hence so is $\mathcal H^i(K'')$. This
shows that $\Dbc(X,\Lambda)$ is closed under cones. It is also closed under shifts, which only
renumber the cohomology sheaves. Details: [det-cor-coefficient-heart-ii-triangulated].

For the second assertion, we argue by induction on the number of nonzero cohomology sheaves
of $K$. If $i$ is the largest degree with $\mathcal H^i(K)\ne0$, the truncation triangle
$\tau_{<i}K\to K\to\mathcal H^i(K)[-i]\to$ exhibits $K$ as the cone of a map
$\mathcal H^i(K)[-i-1]\to\tau_{<i}K$, and $\tau_{<i}K$ has fewer nonzero cohomology sheaves.
This reduces the claim to a single shifted constructible sheaf. The filtration of this sheaf
from [sk-lem-coefficient-heart] (3) yields finitely many short exact sequences, that is,
distinguished triangles, with terms $a_!L$. Details: [det-cor-coefficient-heart-ii-generation].
