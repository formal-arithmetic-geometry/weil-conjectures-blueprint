+++
id = "thm-pc-hilb-curves"
kind = "theorem"
title = "Hilbert schemes of smooth projective curves"
order = 4373
lean = ["AlgebraicGeometry.Curve.hilbScheme_isSmoothProperVariety"]
uses = ["def-pc-hilb-functor", "lem-pc-hilb-representable", "def-pc-degree-line-bundle", "lem-pc-degree-base-change", "lem-pc-ample-positive-degree", "lem-pc-hilb-smooth", "def-pc-morphism-conventions", "lem-pc-hilb-addition", "def-pc-curve", "def-pc-base-change", "lem-pc-cartier-criterion", "lem-pc-flat-source-descent"]
+++
(Picard Schemes of Curves, Proposition 44.3.6, [Tag
0B9I](https://stacks.math.columbia.edu/tag/0B9I).) Let $X$ be a
geometrically irreducible smooth proper curve over a field $k$ and let
$d\geq0$. Then:

1. $\operatorname{Hilb}^d_{X/k}$ is representable by a smooth proper variety
   $\underline{\operatorname{Hilb}}^d_{X/k}$ of dimension $d$ over $k$;
2. for a field extension $k'/k$ the $k'$-rational points of
   $\underline{\operatorname{Hilb}}^d_{X/k}$ are in bijection with the
   effective Cartier divisors of degree $d$ on $X_{k'}$;
3. for $d_1,d_2\geq0$ there is a morphism
   $$
   \underline{\operatorname{Hilb}}^{d_1}_{X/k}\times_k\underline{\operatorname{Hilb}}^{d_2}_{X/k}
   \longrightarrow\underline{\operatorname{Hilb}}^{d_1+d_2}_{X/k}
   $$
   which is finite locally free of degree $\binom{d_1+d_2}{d_1}$.

## Proof

*Step 0: the affine-open hypothesis.* We verify the hypothesis of
[lem-pc-hilb-representable]. Given finitely many points
$x_1,\dots,x_d\in X$, choose a closed point $Q$ different from every closed
point in this list. Such a $Q$ exists: the complement of finitely many
closed points is a nonempty open of the one-dimensional integral variety
$X$; a nonempty affine open inside it has a maximal ideal with residue
field finite over $k$ by Zariski's lemma. This point is closed in $X$,
since its residue field is finite over $k$. The divisor $[Q]$ is effective
Cartier on the smooth curve and has positive degree $[\kappa(Q):k]$ by
[lem-pc-degree-base-change]. Therefore $\mathcal O_X(Q)$ is ample by
[lem-pc-ample-positive-degree], and $X\setminus\{Q\}$ is affine (the
complement of an effective ample divisor is affine). It contains all the
prescribed points, including the generic point.

*Step 1: representability and the properties (1).* By
[lem-pc-hilb-representable] the functors $\operatorname{Hilb}^d_{X/k}$ are
representable by schemes $H_d:=\underline{\operatorname{Hilb}}^d_{X/k}$ for
all $d\ge0$. The scheme $H_d$ is smooth of relative dimension $d$ over $k$
by [lem-pc-hilb-smooth].

$H_d$ is separated over $k$: the diagonal
$\Delta:H_d\to H_d\times_kH_d$ is a closed immersion. Let
$Z_1,Z_2\in\operatorname{Hilb}^d_{X/k}(H_d\times_kH_d)$ be the two pullbacks
of the universal object along the projections; a morphism
$T\to H_d\times_kH_d$ factors through $\Delta$ iff $Z_{1,T}=Z_{2,T}$; the
locus $\{T:Z_{1,T}=Z_{2,T}\}$ is closed in $H_d\times H_d$, being the
intersection of the closed loci $\{Z_1\subseteq Z_2\}$ and
$\{Z_2\subseteq Z_1\}$, each closed by the closed-immersion claim in Step 1
of the proof of [lem-pc-hilb-representable].

$H_d$ is proper: by [lem-pc-hilb-addition] the morphism
$H_{d-1}\times_kX\to H_d$ is finite locally free of degree $d$; the
iterated composite
$$
\pi_d:X^d=X\times_k\cdots\times_kX\longrightarrow H_d,\qquad
(x_1,\dots,x_d)\longmapsto x_1+\cdots+x_d
$$
is finite locally free of degree $d!$ (the degrees of composites and
products of finite locally free morphisms multiply, the rank of the finite
locally free module attached to a fibre product being the tensor product of
the modules). The morphism $\pi_d$ is *surjective*: the image
$I:=\pi_d(X^d)$ is closed ($\pi_d$ is finite hence proper, and the image of
a proper morphism is closed); for a closed point $\bar t$ of
$H_d\otimes_k\bar k$ the corresponding closed subscheme
$D_{\bar t}\subseteq X_{\bar k}$ is finite flat of rank $d$ over $\bar k$,
so it is a sum $D_{\bar t}=y_1+\cdots+y_d$ of $\bar k$-points with
multiplicities, hence $\bar t$ lies in the image of
$X^d\otimes_k\bar k\to H_d\otimes_k\bar k$; since $I\otimes_k\bar k$ is
closed and the closed points of a scheme of finite type over an
algebraically closed field are dense,
$I\otimes_k\bar k=H_d\otimes_k\bar k$; as $\bar k/k$ is faithfully flat,
$I=H_d$.

Then $H_d$ is proper: $X^d$ is proper (finite products of proper schemes
over $k$ are proper, and $X\to\operatorname{Spec}k$ is proper by
hypothesis), $\pi_d$ is finite hence proper, so $H_d=\pi_d(X^d)$ is the
image of a proper scheme under a proper morphism, hence proper (Morphisms,
Lemma 29.42.9, [Tag 03GN](https://stacks.math.columbia.edu/tag/03GN)).
Finally $H_d$ is irreducible: $X^d$ is irreducible (products of
geometrically irreducible schemes over $k$ are irreducible: Varieties,
Lemma 33.8.4, [Tag 038F](https://stacks.math.columbia.edu/tag/038F)), and
the image of an irreducible scheme under a continuous surjective map is
irreducible; together with smoothness (hence reducedness) $H_d$ is an
integral separated scheme of finite type over $k$ of dimension $d$, i.e. a
variety over $k$. This proves (1).

*Step 2: the points of $H_d$; part (2).* For a field extension $k'/k$: a
$k'$-rational point of $H_d$ is the same as an element
$Z\in\operatorname{Hilb}^d_{X/k}(k')$, i.e. a closed subscheme
$Z\subset X_{k'}$ ([def-pc-base-change]) finite locally free of degree $d$
over $k'$. Since $X_{k'}\to k'$ is smooth of relative dimension $1$, the
criteria of [lem-pc-cartier-criterion] apply with
$S=\operatorname{Spec}(k')$ and give: $Z\to k'$ is finite locally free iff
$Z$ is a relative effective Cartier divisor on $X_{k'}/k'$, iff $Z$ is an
effective Cartier divisor on $X_{k'}$ (the relative condition being
automatic over a field). Its degree $\deg(\mathcal{O}_{X_{k'}}(D))$
([def-pc-degree-line-bundle] and the divisor-degree formulas of
[lem-pc-degree-base-change](2)) equals the rank $d$ of the finite locally
free $Z\to k'$. This gives the bijection of (2).

*Step 3: the addition morphism; part (3).* For $d_1,d_2\ge0$ and $T$ over
$k$: an element of
$\operatorname{Hilb}^{d_1}_{X/k}(T)\times\operatorname{Hilb}^{d_2}_{X/k}(T)$
is a pair of closed subschemes $D_1,D_2\subseteq X_T$ finite locally free
of degrees $d_1,d_2$ over $T$; by [lem-pc-cartier-criterion]
($(1)\Rightarrow(2)$) both are relative effective Cartier divisors on
$X_T/T$. The sum $D_1+D_2$ (defined locally by the product of the two
defining equations) is an effective Cartier divisor, flat over $T$: the
short exact sequence
$$
0\to\mathcal{O}_{X_T}/(f_1)\to\mathcal{O}_{X_T}/(f_1f_2)\to\mathcal{O}_{X_T}/(f_2)\to0
$$
(exact because $f_1$ is a nonzerodivisor; the two ends flat over $T$) shows
$\mathcal{O}_{D_1+D_2}$ flat over $T$ of rank $d_1+d_2$: it is an element
of $\operatorname{Hilb}^{d_1+d_2}_{X/k}(T)$. The assignment
$(D_1,D_2)\mapsto D_1+D_2$ is natural in $T$, so by representability it is
induced by a morphism
$\alpha:H_{d_1}\times_kH_{d_2}\to H_{d_1+d_2}$.

The map $\alpha$ is proper, since its source is proper over $k$ and its
target is separated over $k$, by part (1). The surjection
$u:=\pi_{d_1}\times\pi_{d_2}$ from $X^{d_1+d_2}$ onto its source is finite
locally free, and $\alpha\circ u=\pi_{d_1+d_2}$ is finite locally free as
well. For every point of the target, the fibre of $\alpha$ is therefore the
surjective image of the finite fibre of $\pi_{d_1+d_2}$, so it has finitely
many points. Thus $\alpha$ is finite (a proper morphism with finite fibres
is finite). It is flat by [lem-pc-flat-source-descent], since $u$ is a flat
surjection and the composite is flat. These are morphisms of finite type
schemes over a field, hence of finite presentation; so $\alpha$ is finite
locally free.

We compute its rank using the commutative diagram
$$
\begin{array}{ccc}
X^{d_1}\times_kX^{d_2}&\stackrel{\sim}{\longrightarrow}&X^{d_1+d_2}\\
\downarrow&&\downarrow\\
H_{d_1}\times_kH_{d_2}&\longrightarrow&H_{d_1+d_2}
\end{array}
$$
(the left vertical arrow is $\pi_{d_1}\times\pi_{d_2}$, the right one
$\pi_{d_1+d_2}$; the diagram commutes by the definition of $\alpha$ and the
additivity of the sums). The left vertical arrow is finite locally free of
degree $d_1!\,d_2!$, the right of degree $(d_1+d_2)!$; with
$\deg(\alpha)=N$ the commutativity and the multiplicativity of degrees give
$d_1!\,d_2!\,N=(d_1+d_2)!$, so $N=\binom{d_1+d_2}{d_1}$. This proves (3).

Unresolved dependencies: def:sc-effective-cartier-divisor, lem:sc-ample-complement-affine, thm:pqf-finite-iff-proper-finite-fibres
