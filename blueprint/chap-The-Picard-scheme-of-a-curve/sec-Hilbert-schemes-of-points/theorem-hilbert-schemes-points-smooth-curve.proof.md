+++
kind = "proof"
of = "theorem-hilbert-schemes-points-smooth-curve"
order = 1538
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
Representability is a general theorem, once we know that finite sets of
points lie in affine opens. We then obtain the geometric properties from the addition map $\operatorname{Hilb}^{d}_{C/k}\times C\to \operatorname{Hilb}^{d+1}_{C/k}$, which we show to be finite
locally free. Starting from $\operatorname{Hilb}^{1}_{C/k}=C$, we get smoothness and the
dimension by induction on $d$, and properness and irreducibility from
the finite surjection $C^d\to \operatorname{Hilb}^{d}_{C/k}$.

Every finite set of points of $C$ lies in an affine open. Indeed, if $Q$
is a closed point outside the set, then $\mathcal O_C(Q)$ has positive
degree, hence is ample by Riemann–Roch, and so $C\setminus\{Q\}$ is
affine. Hence $\operatorname{Hilb}^{d}_{C/k}$ is represented by a scheme, separated and locally
of finite type over $k$ [Stacks, [0B9A](https://stacks.math.columbia.edu/tag/0B9A)]. The universal closed subscheme
is the divisor $D_d$.

Let $T$ be a $k$-scheme and $t\in T$ a point. Since the local rings of
$C_{\kappa(t)}$ at closed points are discrete
valuation rings, every finite closed subscheme of a fibre is an
effective Cartier divisor. By the fibrewise criterion for relative
effective Cartier divisors, every $D\in \operatorname{Hilb}^{d}_{C/k}(T)$ is a relative effective
Cartier divisor on $C_T/T$. This gives the description of $T$-points
and the invertible sheaf $\mathcal O(D_d)$. Multiplying ideals adds
such divisors, and we obtain the addition map

$$
\operatorname{Hilb}^{d}_{C/k}\times C\longrightarrow \operatorname{Hilb}^{d+1}_{C/k},\qquad (D,x)\longmapsto D+\Gamma_x.
$$

It identifies $\operatorname{Hilb}^{d}_{C/k}\times C$ with the universal divisor over
$\operatorname{Hilb}^{d+1}_{C/k}$: if a divisor $E$ contains the graph $\Gamma_x$, then dividing a local
equation of $E$ by one of $\Gamma_x$ gives a relative effective
Cartier divisor $D$ with $E=D+\Gamma_x$, of degree $d$ by the exact
sequence for a sum of divisors. In other words, the addition map is the
projection to $\operatorname{Hilb}^{d+1}_{C/k}$ of the universal divisor
$D_{d+1}\subset C\times \operatorname{Hilb}^{d+1}_{C/k}$. By definition of
the Hilbert functor, $D_{d+1}$ is finite locally free of degree $d+1$ over
$\operatorname{Hilb}^{d+1}_{C/k}$. Hence the addition map is finite
locally free of degree $d+1$ [Stacks, [0B9G](https://stacks.math.columbia.edu/tag/0B9G)], in particular faithfully
flat.

We now argue by induction on $d$, starting from
$\operatorname{Hilb}^{0}_{C/k}=\operatorname{Spec}k$ and
$\operatorname{Hilb}^{1}_{C/k}=C$. The scheme $\operatorname{Hilb}^{d+1}_{C/k}$
is smooth because regularity descends along faithfully flat maps, also
after extending $k$. It has dimension $d+1$ because the addition map is
finite and surjective [Stacks, [0B9H](https://stacks.math.columbia.edu/tag/0B9H)].

Properness comes from the finite surjective map $C^d\to \operatorname{Hilb}^{d}_{C/k}$
given by iterated addition. This map makes $\operatorname{Hilb}^{d}_{C/k}$
quasi-compact. It also makes $\operatorname{Hilb}^{d}_{C/k}$ universally
closed, because $C^d$ is proper and surjectivity is stable under base
change. Since $C^d$ is geometrically integral, $\operatorname{Hilb}^{d}_{C/k}$
is geometrically irreducible. Being smooth, it is then geometrically
integral [Stacks, [0B9I](https://stacks.math.columbia.edu/tag/0B9I)].

For $C=\mathbf P^1$, the map $C^d\to \operatorname{Hilb}^{d}_{C/k}=\mathbf P^d$ sends $d$ points to
the binary form with these zeros, that is, the product of $d$ linear
forms; it is the quotient by the symmetric group, of degree $d!$.
