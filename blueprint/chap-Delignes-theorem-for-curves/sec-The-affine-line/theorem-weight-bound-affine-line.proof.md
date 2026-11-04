+++
kind = "proof"
of = "theorem-weight-bound-affine-line"
order = 1293
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "theorem-pro-etale-refinements-weakly-etale", "lemma-boundary-stalk", "lemma-extreme-degrees-affine-curve", "lemma-unramified-at-infinity-no-linear-characters", "corollary-h-1-c-stalk-fourier", "proposition-exactness-fixed-pure-weight"]
+++
We prove the bound for the irreducible factors of $F$ and
pass to $F$ by induction. The irreducible factors are of two kinds:
geometrically constant ones, for which $H^1_c$ vanishes, and the others,
to which Corollary [corollary-h-1-c-stalk-fourier] applies.

Take a finite composition series of the finite-dimensional Weil
representation of $F$. Each irreducible lisse factor is pure of weight
$w$, since its local eigenvalues are eigenvalues of a subquotient. It is
again unramified at infinity, since inertia at infinity acts trivially
on every subquotient of a representation on which it acts trivially.
An irreducible factor that is geometrically constant is a sheaf
$\mathcal B_b$ of Proposition [proposition-weights-under-usual-operations],
because the geometric action is trivial and an invertible linear
operator over $\overline{\mathbf Q}_\ell$ has an eigenline. Its middle extension is
constant on the affine line, and so its $H_c^1$ vanishes by the trivial
case of Lemma [lemma-integral-linear-character]. Every other factor
$F_i$ is irreducible, unramified at infinity and not geometrically
constant, so by Lemma [lemma-unramified-at-infinity-no-linear-characters]
it has no geometric constituent of the form $\mathcal L_{\psi(ax)}$,
and we may apply Corollary [corollary-h-1-c-stalk-fourier] with $M=F_i$.

The induction needs $j_*$ to turn the composition series
into a filtration of $j_*F$ whose quotients are the $j_*F_i$. Since all
factors are pure of the same weight $w$,
Proposition [proposition-exactness-fixed-pure-weight] shows that
the short exact sequences of the series remain exact after applying
$j_*$. Consider a step $0\to F'\to F''\to F_i\to0$ of the series, where
we may assume that the bound holds for $F'$. In the resulting long
exact sequence of compactly supported cohomology, the image of
$H^1_c(\mathbf A^1,j_*F')$ in $H^1_c(\mathbf A^1,j_*F'')$ is a
quotient of the former, and the cokernel embeds in
$H^1_c(\mathbf A^1,j_*F_i)$. Since the bound $w+1$
is preserved under subquotients and extensions, we conclude by
induction that it holds for $F$.
