+++
kind  = "proof"
of    = "sk-lem-wgen-bertini-cover"
+++
Embed $X$ in a projective closure $\overline X$. For large $n$, the
sections of $\mathcal O_{\overline X}(n)$ vanishing on $S$ have base
locus exactly $S$ on $X$ and define an immersion off $S$
([Stacks, Tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5)). They
also surject onto the first-order jets
$\bigoplus_{s\in S}\mathfrak m_s/\mathfrak m_s^2$, twisted by the
corresponding line-bundle factors; this follows from Serre vanishing
for the ideal of the first infinitesimal neighbourhoods
([Stacks, Tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U)).
Consequently, the condition that a section have nonzero derivative at
each $s$ is nonempty and open. Together with
[Stacks, Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6) off $S$,
it shows that a general divisor is smooth everywhere on $X$.

Next we apply the geometric irreducibility criterion
[Stacks, Tag 0G4F](https://stacks.math.columbia.edu/tag/0G4F) to
this linear system on $X$ and to its pullback on $T$. Both schemes are
smooth and connected, hence irreducible, and their finite base loci
have codimension at least two. For the remaining hypothesis, choose
$x\notin S$, two sections vanishing at $x$ with independent
differentials, and a third section not vanishing at $x$. The divisors
of the first two have a component of codimension two through $x$ that
is not contained in the divisor of the third, and the same holds above
$x$ because $T\to X$ is étale. Hence a general divisor cuts both
schemes in irreducible schemes. Intersecting these nonempty open
conditions in the space of sections, we obtain a smooth connected
affine hypersurface containing $S$ whose inverse image in $T$ is
connected. We repeat this until the dimension is one. Finally, the
finitely many equations of the curve have coefficients in a finite
extension of $\mathbf F_q$.
