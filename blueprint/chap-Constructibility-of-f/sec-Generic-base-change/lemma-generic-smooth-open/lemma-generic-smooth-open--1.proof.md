+++
kind = "proof"
of = "lemma-generic-smooth-open--1"
order = 580002
uses = []
+++
Put $K=k(S)$. By
`AlgebraicGeometry.exists_isPurelyInseparable_dense_isClosedImmersion_smooth`,
there is a finite purely inseparable extension $L/K$ for which
$X_K\times_K L$ has a dense open $W$ admitting a surjective closed
immersion $Z\to W$, with $Z$ smooth over $L$.

Choose an affine neighbourhood $\operatorname{Spec}R$ of the generic
point of $S$. The theorem
`AlgebraicGeometry.exists_finite_isUniversalHomeomorphism_isFractionRing`
gives a nonzero $c\in R$ and a domain $B$, finite over $R[1/c]$, with
fraction field $L$, such that
$\operatorname{Spec}B\to\operatorname{Spec}R[1/c]$ is a universal
homeomorphism compatible with the extension $L/K$.

Apply `AlgebraicGeometry.exists_isImmersion_smooth_of_isFractionRing`
to spread out $Z\to W$. After localizing $B$ at a nonzero element,
there are an immersion with open image, smooth over the localized
base, and a nonempty open of that base over which every point of the
base change of $X$ is a specialization of a point in the image.
Take $U\subset S$ to be the image of this open and $S'$ to be the open
itself. The map $S'\to U$ is the restriction of the finite universal
homeomorphism above. Restricting the immersion gives
$v_0:V_0\to X'$ with open image, smooth over $S'$, such that every
point of $X'$ is a specialization of a point of $v_0(V_0)$. The scheme
$S'$ is integral, and $V_0$ is reduced since it is smooth over this
reduced Noetherian base.

The sheaf $(p\circ v_0)^*F$ is constructible by
`AlgebraicGeometry.Scheme.IsConstructibleSheaf.upperStar`. Apply
`AlgebraicGeometry.Scheme.IsConstructibleSheaf.exists_dense_open` to
choose a dense open $V\subset V_0$ on which it is finite locally
constant. Restrict $v_0$ to $v:V\to X'$. Its image is open and it
remains smooth over $S'$.

To check density after this restriction, let $x\in X'$ and choose
$w\in V_0$ such that $x\in\overline{\{v_0(w)\}}$. The scheme $V_0$
is Noetherian. Choose the generic point $w'$ of an irreducible
component containing $w$; density and openness of $V$ imply $w'\in V$.
Then $y=v_0(w')$ belongs to $v(V)$ and $x\in\overline{\{y\}}$.
Thus $v(V)$ is dense. If $f'(x)=\eta'$, continuity shows that $f'(y)$
generalizes $\eta'$, hence equals $\eta'$. If in addition
$x\notin v(V)$, then $y\ne x$, which proves the last assertion.
