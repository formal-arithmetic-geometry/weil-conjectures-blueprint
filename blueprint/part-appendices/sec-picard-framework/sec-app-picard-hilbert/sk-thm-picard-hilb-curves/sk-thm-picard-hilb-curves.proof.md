+++
kind = "proof"
of = "sk-thm-picard-hilb-curves"
uses = ["sk-thm-picard-rr"]
+++
Every finite set of points of $C$ lies in an affine open: if $Q$ is a
closed point outside the set, then $\mathcal O_C(Q)$ has positive
degree, hence is ample by Riemann–Roch, and $C\setminus\{Q\}$ is
affine. Hence $H_d$ is represented by a scheme, separated and locally
of finite type over $k$ [Stacks, Tag 0B9A](https://stacks.math.columbia.edu/tag/0B9A). The universal closed subscheme
is the divisor $D_d$.

Let $T$ be a $k$-scheme and $t\in T$ a point. Since the local rings of
$C_{\kappa(t)}$ at closed points are discrete
valuation rings, every finite closed subscheme of a fibre is an
effective Cartier divisor. By the fibrewise criterion for relative
effective Cartier divisors, every $D\in H_d(T)$ is a relative effective
Cartier divisor on $C_T/T$; this gives the description of $T$-points
and the invertible sheaf $\mathcal O(D_d)$. Multiplying ideals adds
such divisors, and we obtain the addition map

$$
H_d\times C\longrightarrow H_{d+1},\qquad (D,x)\longmapsto D+\Gamma_x.
$$

It identifies $H_d\times C$ with the universal divisor over $H_{d+1}$:
if a divisor $E$ contains the graph $\Gamma_x$, then dividing a local
equation of $E$ by one of $\Gamma_x$ gives a relative effective
Cartier divisor $D$ with $E=D+\Gamma_x$, of degree $d$ by the exact
sequence for a sum of divisors. Hence the addition map is finite
locally free of degree $d+1$ [Stacks, Tag 0B9G](https://stacks.math.columbia.edu/tag/0B9G), in particular faithfully
flat. Starting from $H_0=\operatorname{Spec}k$ and $H_1=C$, induction
on $d$ shows that $H_d$ is smooth, because regularity descends along
faithfully flat maps (also after extending $k$), and that
$\dim H_d=d$, because the addition map is finite and surjective
[Stacks, Tag 0B9H](https://stacks.math.columbia.edu/tag/0B9H).

Iterating addition gives a finite surjective map $C^d\to H_d$. Thus
$H_d$ is quasi-compact, and it is universally closed because $C^d$ is
proper and surjectivity is stable under base change; so $H_d$ is
proper. Since $C^d$ is geometrically integral, $H_d$ is geometrically
irreducible, and being smooth it is geometrically integral
[Stacks, Tag 0B9I](https://stacks.math.columbia.edu/tag/0B9I).
