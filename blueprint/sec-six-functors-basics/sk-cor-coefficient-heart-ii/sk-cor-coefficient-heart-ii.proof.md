+++
kind  = "proof"
of    = "sk-cor-coefficient-heart-ii"
+++
Let $K\to K'\to K''\to K[1]$ be a distinguished triangle with $K,K'$ in $\Dbc(X,\Lambda)$. By
the long exact cohomology sequence, each $\mathcal H^q(K'')$ is an extension of
$\ker(\mathcal H^{q+1}K\to\mathcal H^{q+1}K')$ by $\coker(\mathcal H^qK\to\mathcal H^qK')$. Both
are constructible by [sk-lem-coefficient-heart] (1), hence so is $\mathcal H^q(K'')$. Thus
$\Dbc(X,\Lambda)$ is closed under cones, and it is clearly closed under shifts. Details:
[det-cor-coefficient-heart-ii-triangulated].

For the second assertion, induct on the number of nonzero cohomology sheaves of $K$. If $q$
is the largest degree with $\mathcal H^q(K)\ne0$, the truncation triangle
$\tau_{<q}K\to K\to\mathcal H^q(K)[-q]\to$ reduces the claim to a single shifted constructible
sheaf. Its filtration from [sk-lem-coefficient-heart] (3) gives finitely many short exact
sequences, that is, distinguished triangles, with terms $a_!L$. Details:
[det-cor-coefficient-heart-ii-generation].
