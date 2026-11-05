+++
kind = "proof"
of = "corollary-coefficient-heart-b"
order = 274
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves", "lemma-acyclic-resolutions"]
+++
The first assertion is closure under cones, which we check on cohomology sheaves.
Let $K\to K'\to K''\to K[1]$ be a distinguished triangle with $K,K'$ in
$\Dbc(X,\Lambda)$. By the long exact cohomology sequence, each
$\mathcal H^i(K'')$ is an extension of
$\ker(\mathcal H^{i+1}K\to\mathcal H^{i+1}K')$ by
$\coker(\mathcal H^iK\to\mathcal H^iK')$. Both are constructible by
Lemma [lemma-constructible-sheaves](1), and hence so is $\mathcal H^i(K'')$.
Closure under shifts is clear, since shifts only renumber the cohomology sheaves.

For the second assertion, we argue by induction on the number of nonzero
cohomology sheaves of $K$. If $i$ is the largest degree with $\mathcal H^i(K)\ne0$,
the truncation triangle $\tau_{<i}K\to K\to\mathcal H^i(K)[-i]\to$
exhibits $K$ as the cone of a map
$\mathcal H^i(K)[-i-1]\to\tau_{<i}K$, and $\tau_{<i}K$ has fewer nonzero
cohomology sheaves. This reduces
the claim to a single shifted constructible sheaf, and for it the filtration
from Lemma [lemma-constructible-sheaves](3) yields finitely many short
exact sequences, that is, distinguished triangles, with terms $a_!L$.
