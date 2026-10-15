+++
kind  = "proof"
of    = "det-cor-coefficient-heart-ii-triangulated"
+++
$0$, isomorphisms and shifts are clear: $\mathcal H^q(K[n])=\mathcal H^{q+n}(K)$.

Let $K\to K'\to K''\to K[1]$ be distinguished with $K,K'\in\Dbc(X,\Lambda)$ (by rotation, any
two vertices may be put in these positions, using closure under shifts). The long exact
sequence
$$
\mathcal H^qK\to\mathcal H^qK'\to\mathcal H^qK''\to\mathcal H^{q+1}K\to\mathcal H^{q+1}K'
$$
shows that $\mathcal H^qK''=0$ unless $\mathcal H^qK'\ne0$ or $\mathcal H^{q+1}K\ne0$, so
$K''$ is bounded, and gives a short exact sequence
$$
0\to\coker(\mathcal H^qK\to\mathcal H^qK')\to\mathcal H^qK''\to\ker(\mathcal H^{q+1}K\to\mathcal H^{q+1}K')\to0 .
$$
The outer terms are constructible because $\Cons(X,\Lambda)$ is closed under kernels and
cokernels, and then the middle term is constructible because it is closed under extensions
([det-lem-coefficient-heart-closure]).

Thickness: if $K_1\oplus K_2\in\Dbc$, then $\mathcal H^q(K_1)$ is a direct summand of a
constructible sheaf, i.e. the kernel of an idempotent endomorphism, hence constructible.
