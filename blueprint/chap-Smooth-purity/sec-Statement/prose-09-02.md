+++
id = "prose-09-02"
kind = "hidden"
title = "Statement (1)"
order = 726
+++
Smooth purity is stated for six kinds of coefficients at once, because the
proof moves between them: the geometry is done with finite rings, the
case $\mathcal O_E$ is a limit of finite levels, and the fields are
obtained by inverting $\ell$. Throughout this section $\Lambda$ is an
admissible coefficient ring, that is, a finite commutative ring killed by a
power of $\ell$, $\mathcal O_E$, $E$ or $\overline{\mathbf Q}_\ell$ (the rings $\mathbf Z_\ell$ and $\mathbf Q_\ell$
being the cases $E=\mathbf Q_\ell$), and Tate twists are those
of Definition [definition-tate-twists].

The theorem asserts one isomorphism on all of $X$, whereas on a chart an
isomorphism of this shape is already given by
Proposition [proposition-exceptional-inverse-image-smooth-morphism] with finite coefficients.
A bare isomorphism for each $f$ separately, however, would not be enough for
what follows, and the theorem therefore also lists three properties that the
later chapters use. Property (2), compatibility with base change, restricts
$\gamma_f$ to the fibres of $f$, and it is what makes $\gamma_f$ commute with
Frobenius, because the Frobenius square is a base change
(Proposition [proposition-purity-trace-commute-frobenius]). Property (3),
compatibility with composition, gives the transitivity of the trace map
(Proposition [proposition-transitivity-trace-map]), the analogue
of integrating over the fibres of a composite in two steps. Property (4),
compatibility with change of coefficients, lets us construct $\gamma_f$ with
finite coefficients and pass to $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$, and it also
makes Poincaré duality compatible with change of coefficients
(Theorem [theorem-poincare-duality]). Properties (1)
and (2) involve maps that we define now, for every admissible
$\Lambda$; the functors are those of
Theorem [theorem-exceptional-inverse-image], restricted to $D^b_{\mathrm{ctf}}$.

The first map compares $f^!$ before and after a change of base. Let
$f:X\to Y$ and $g:Y'\to Y$ be morphisms of separated schemes of finite type
over $k$, let $X'=X\times_YY'$, and let $f':X'\to Y'$ and $g':X'\to X$ be the
projections. Write $\varepsilon_f(K):Rf_!f^!K\to K$ for the counit of
$Rf_!\dashv f^!$.
