+++
kind = "proof"
of = "theorem-riemann-roch-coherent-serre-duality--1"
order = 1525001
uses = []
+++
Quasi-coherent cohomology on $C$ vanishes above degree one: choose a
finite map $C\to\mathbf P^1_k$, use affine pushforward to identify
cohomology, and use the two standard affine opens of $\mathbf P^1_k$.
In particular,

$$
\chi(C,\mathcal O_C)=h^0(C,\mathcal O_C)-h^1(C,\mathcal O_C)=1-g.
$$

Substituting this into the definition of $\deg\mathcal M$ proves the
identity for every $\mathcal M$.

For the interpretation for invertible sheaves, an effective Cartier
divisor $D$ satisfies
$\deg\mathcal O_C(D)=\dim_k\Gamma(D,\mathcal O_D)$, by the exact
sequence for restriction to $D$. Every invertible sheaf is of the form
$\mathcal O_C(D_1)\otimes\mathcal O_C(D_2)^{-1}$ with $D_1,D_2$
effective. Additivity of degree under tensor product then identifies
the cohomological degree with the divisor degree.
