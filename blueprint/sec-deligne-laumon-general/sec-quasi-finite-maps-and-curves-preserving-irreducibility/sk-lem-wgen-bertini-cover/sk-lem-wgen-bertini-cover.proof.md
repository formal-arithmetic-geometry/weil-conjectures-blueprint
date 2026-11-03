+++
kind = "proof"
of = "sk-lem-wgen-bertini-cover"
+++
We cut $X$ by a general hypersurface through $S$ and show that it is
smooth and that it and its inverse image in $T$ are connected, and
then we repeat. Embed $X$ in a projective closure $\overline X$. For large
$n$, the sections of $\mathcal O_{\overline X}(n)$ vanishing on $S$
have base locus exactly $S$ on $X$ and define an immersion off $S$
([Stacks, Tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5)). They also surject onto the first-order jets
$\bigoplus_{s\in S}\mathfrak m_s/\mathfrak m_s^2\otimes \mathcal O_{\overline X}(n)$ at $S$. Indeed, if $\mathcal I$ is the
ideal sheaf of $S$, then $H^1(\overline X,\mathcal I^2(n))=0$ for large
$n$ by Serre vanishing ([Stacks, Tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U)). Consequently, the condition that
a section have nonzero derivative at each $s$ is nonempty and open.
The divisors of the sections vanishing on $S$, restricted to
$X\setminus S$, are the pullbacks of hyperplanes under the immersion of
$X\setminus S$ into a projective space that these sections define.
By Bertini's theorem ([Stacks, Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6)), a
general such divisor is smooth on $X\setminus S$, hence smooth
everywhere on $X$.

For connectedness we use Bertini's irreducibility theorem
[Stacks, Tag 0G4F](https://stacks.math.columbia.edu/tag/0G4F): if $Z$ is an irreducible scheme of finite type over an
algebraically closed field and $Z\to\mathbf P^N$ is a morphism whose
image has closure of dimension at least two, then the inverse image of
a general hyperplane is irreducible. We apply it to the immersion of
$X\setminus S$ above and to its composition with the restriction of
$T\to X$ over $X\setminus S$. In both cases the hyperplanes correspond
to the sections vanishing on $S$ and their pullbacks to $T$. Both
sources are smooth and connected, hence irreducible, and both images
have closure of dimension $\dim X\ge2$, because $T\to X$ is finite and
surjective. Hence a general
divisor meets $X\setminus S$ and its inverse image in $T$ in
irreducible schemes. Every component of a divisor has dimension
$\dim X-1\ge1$, so the finitely many points over $S$ are not
components, and the divisor and its inverse image in $T$ are
irreducible. Intersecting these nonempty open conditions in the space
of sections, we obtain a smooth connected affine hypersurface
containing $S$ whose inverse image in $T$ is connected. We repeat this
until the dimension is one. Since the curve
has finitely many equations, their coefficients lie in a finite
extension of $\mathbf F_q$.
