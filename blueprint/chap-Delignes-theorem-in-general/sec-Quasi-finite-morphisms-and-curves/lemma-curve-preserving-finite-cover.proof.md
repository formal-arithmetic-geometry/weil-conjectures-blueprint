+++
kind = "proof"
of = "lemma-curve-preserving-finite-cover"
order = 1322
+++
We cut $X$ by a general hypersurface through $S$, show that it is
smooth and that both it and its inverse image in $T$ are connected,
and then repeat.

*The linear system.* Embed $X$ in a projective closure $\overline X$.
For large $n$, the sections of $\mathcal O_{\overline X}(n)$ vanishing on
$S$ have base locus exactly $S$ on $X$ and define an immersion off $S$
([Stacks, [0FD5](https://stacks.math.columbia.edu/tag/0FD5)]). They also surject onto the first-order jets
$\bigoplus_{s\in S}\mathfrak m_s/\mathfrak m_s^2\otimes
\mathcal O_{\overline X}(n)$ at $S$. Indeed, if $\mathcal I$ is the
ideal sheaf of $S$, then $H^1(\overline X,\mathcal I^2(n))=0$ for large
$n$ by Serre vanishing ([Stacks, [0B5U](https://stacks.math.columbia.edu/tag/0B5U)]), and the cohomology sequence of
$0\to\mathcal I^2(n)\to\mathcal I(n)\to(\mathcal I/\mathcal I^2)(n)\to0$
shows that $H^0(\overline X,\mathcal I(n))$ surjects onto the jets.

*Smoothness.* A general divisor of these sections is smooth on $X$.
The immersion off $S$ says nothing about the points of $S$ themselves,
and there smoothness is controlled by the jets. A divisor through $s$ is
smooth at $s$ exactly when its equation has nonzero image in
$\mathfrak m_s/\mathfrak m_s^2$. Since the sections surject onto the
jets, the condition that a section have nonzero derivative at each $s$
is nonempty and open. On $X\setminus S$ the divisors are the pullbacks
of hyperplanes under the immersion of $X\setminus S$ into a projective
space that these sections define. By Bertini's theorem ([Stacks, [0FD6](https://stacks.math.columbia.edu/tag/0FD6)]) a
general one is smooth there.

*Connectedness.* A general divisor and its inverse image in $T$ are
irreducible. We use Bertini's irreducibility theorem
[Stacks, [0G4F](https://stacks.math.columbia.edu/tag/0G4F)]: if $Z$ is an irreducible scheme of finite type over an
algebraically closed field and $Z\to\mathbf P^N$ is a morphism whose
image has closure of dimension at least two, then the inverse image of
a general hyperplane is irreducible. We apply it to the immersion of
$X\setminus S$ above and to its composition with the restriction of
$T\to X$ over $X\setminus S$. In both cases the hyperplanes correspond
to the sections vanishing on $S$ and their pullbacks to $T$. Both
sources are smooth and connected, hence irreducible. Both images have
closure of dimension $\dim X\ge2$, because $T\to X$ is finite and
surjective. So for a general divisor $D$, both $D\cap(X\setminus S)$
and its inverse image in $T$ are irreducible. The finitely many points
over $S$ cannot be components, since every component of a divisor has
dimension $\dim X-1\ge1$, and the claim follows.

*Induction.* Intersecting these nonempty open conditions in the space
of sections, we obtain a smooth connected affine hypersurface $H$
containing $S$ whose inverse image in $T$ is connected. It is smooth,
connected and affine of dimension $\dim X-1$, it contains $S$, and
$T\times_XH\to H$ is a connected finite étale cover. Thus $H$ again
satisfies the hypotheses of the lemma, and we repeat the construction
until the dimension is one.
The curve is defined over a finite field, because it has finitely many
equations, whose coefficients lie in a finite extension of $\mathbf F_q$.
