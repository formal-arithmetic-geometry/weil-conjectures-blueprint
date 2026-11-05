+++
kind = "proof"
of = "lemma-reduction-curve-over-normal-base--1"
order = 681002
uses = ["lemma-reduction-field", "lemma-integral-changes-source-base", "lemma-injectivity-base-change-map-degree", "lemma-cohomology-modules-underlying-abelian", "corollary-continuity-cohomology"]
+++
By Lemma [lemma-reduction-field], a failure is witnessed over an affine
base $T=\operatorname{Spec}B$ by a morphism
$\operatorname{Spec}K_0\to T$ and a sheaf of $\Lambda$-modules on
$\operatorname{Spec}K_0$. The hypothesis in all lower degrees is
universal, so it also holds after this change of base.

Let $\Omega$ be an algebraic closure of $K_0$. Form the integral closure
$R$ of the image of $B$ in $\Omega$, and put $S=\operatorname{Spec}R$.
Then $R$ is a normal domain, its fraction field $L$ is algebraically
closed, and $L$ embeds into $\Omega$. The morphism
$\operatorname{Spec}\Omega\to T$ factors through the geometric generic
point of $S$, and $S\to T$ is integral. This is the construction in
`AlgebraicGeometry.Etale.exists_normalization_of_isAlgClosed`.
Lemma [lemma-integral-changes-source-base] shows that the failure
survives both the integral surjective morphism
$\operatorname{Spec}\Omega\to\operatorname{Spec}K_0$ and the replacement
of $T$ by $S$.

Pull back $g$ to $S$ and then to $\operatorname{Spec}\Omega$.
By Lemma [lemma-injectivity-base-change-map-degree], the resulting
degree-$q$ base change map is injective. Since it is not an isomorphism,
its target is nonzero. Thus, if $F$ is the pulled back sheaf on
$\operatorname{Spec}\Omega$ and $e:C_\Omega\to\operatorname{Spec}\Omega$
is the projection, then $R^qh_*e^{-1}F\ne0$.

It remains to reduce the coefficients. The morphism $h$ is affine,
being a base change of a morphism between affine schemes. Also $n\ne0$,
since its image is a unit in $\Omega$. As $\Omega$ is algebraically
closed, $F$ is constant with value a $\Lambda$-module $M$ annihilated by
$n$. By Lemma [lemma-cohomology-modules-underlying-abelian], we may
detect the nonvanishing on underlying abelian sheaves. Express $M$ as
the filtered union of its finite subgroups. Continuity
([corollary-continuity-cohomology]) and dévissage of these finite
groups by short exact sequences detect a prime $\ell\mid n$ for which
$R^qh_*\underline{\mathbf Z/\ell}\ne0$ and $\ell$ is not a unit in
$\Lambda$.

The quotient $\Lambda/\ell\Lambda$ is a nonzero vector space over
$\mathbf F_\ell$. Its vector $1$ spans a copy of $\mathbf F_\ell$ which
is a direct summand of the underlying abelian group. Applying the
constant sheaf functor and the higher direct image preserves this
retraction. Hence $R^qh_*\underline{\Lambda/\ell\Lambda}\ne0$.
This coefficient reduction is
`AlgebraicGeometry.Etale.exists_not_isZero_higherDirectImage_constantModSheaf`.
Taking $m=\ell$ gives the required conclusion.
