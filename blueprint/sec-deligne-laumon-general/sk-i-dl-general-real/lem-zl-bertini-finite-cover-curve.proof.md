+++
kind  = "proof"
of    = "lem-zl-bertini-finite-cover-curve"
+++
We spell out the geometric input. We use the ordinary Bertini lemmas
[Stacks Project, Tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5)
(sections vanishing on a prescribed closed subscheme),
[Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6)
(smoothness), and
[Tag 0G4F](https://stacks.math.columbia.edu/tag/0G4F)
(geometric irreducibility of a linear system).
These are statements about schemes and linear systems, with no weight
or monodromy hypothesis.

Since $X_0$ is smooth, geometrically connected and affine of relative
dimension $d$, the base change $X$ is a smooth connected affine
$k$-scheme of dimension $d$. Embed $X$ in projective space and let $\overline X$ be its
projective closure. For a sufficiently large $n$, let $V$ be
the space of sections of $\mathcal O_{\overline X}(n)$ vanishing
on the reduced finite subscheme $S$. Tag 0FD5 makes its base locus
on $X$ exactly $S$, and makes its associated map an immersion on
$X\setminus S$. Increasing $n$ if necessary makes

$$
V\longrightarrow\bigoplus_{s\in S}
(\mathfrak m_s/\mathfrak m_s^2)\otimes
\mathcal O_{\overline X}(n)|_s
$$

surjective. Indeed, apply the usual eventual vanishing of coherent
$H^1$ for an ample twist to the ideal of the union of the first
infinitesimal neighborhoods of these finitely many points. Thus
nonzero first derivative at each $s$ is a nonempty open condition
on $V$. Tag 0FD6 on $X\setminus S$, together with these finitely
many derivative conditions, makes a general member smooth everywhere
on $X$.

For completeness, the hypotheses of Tag 0G4F hold both on $X$ and
for the pulled-back linear system on $T$. Both schemes are smooth
and connected over $k$, hence irreducible. The respective base
loci are $S$ and its finite inverse image, of codimension at least
two. Choose $x\in X\setminus S$. Since the linear system induces
an immersion there, choose two sections vanishing at $x$ with
independent differentials, and a third section nonzero at $x$.
The common zero locus of the first two has a codimension-two component
through $x$ not contained in the third divisor. At any point of
$T$ above $x$, etaleness gives the same assertion for the
pulled-back sections. These verify the remaining hypothesis of
Tag 0G4F. A general member therefore cuts both $X$ and $T$
in irreducible subschemes. Intersect the finitely many nonempty open
conditions on the irreducible parameter space $V$, and choose a
$k$-point in their intersection.

The resulting $X_1$ is a smooth connected closed affine subscheme
of dimension $d-1$, contains $S$, and its inverse image $T_1$
is connected and finite etale over it. Repeat this construction until
dimension one. In dimension two the same argument applies, since
the finite base locus still has codimension two. This proves the
claim about $C$. All the finitely many defining equations and
morphisms involve only finitely many coefficients of $k$, so they
descend to one finite constant-field extension $\mathbf F_{q^m}$:
$C=C_m\times_{\mathbf F_{q^m}}k$ for a closed subscheme $C_m$ of
$X_0\times_{k_0}\mathbf F_{q^m}$. Then $\varphi=\mathrm{id}_{C_m}\times\sigma^m$
is an automorphism of $C$ with $i\circ\varphi=(\mathrm{id}_{X_0}\times\sigma)^m\circ i$.
Geometric smoothness and connectedness are the properties just proved
after base change to $k$.
