+++
kind = "proof"
of = "sk-lem-tf-transverse-boundary"
uses = ["sk-prop-curve-affine-kummer"]
+++
For the assertion at $z$, pass to the strict localization $S$ of
$Z$ at $z$ and write $X_S,Y_S$ for the two transverse divisors.
The stalk formula for an open direct image
([Stacks, Tag 03Q7](https://stacks.math.columbia.edu/tag/03Q7)) and
localization give

$$
 M_z=R\Gamma(S-Y_S,i_!E).
$$

To prove that this object is zero we may forget the $A$-action,
since the exact forgetful functor is conservative and cohomology of
module sheaves agrees with the underlying abelian-sheaf cohomology
([Stacks, Tag 03FD](https://stacks.math.columbia.edu/tag/03FD)). A finite abelian $\ell$-group with an action of a
finite $\ell$-group has a finite filtration with trivial
$\mathbf F_\ell$ quotients: first filter by powers of $\ell$, then use
nilpotence of the augmentation ideal of the group algebra over
$\mathbf F_\ell$. Since $i_!$ is exact, truncation and these
composition series reduce the assertion to $E=\mathbf F_\ell$ on
$S-(X_S\cup Y_S)$.

For these constant coefficients, the open–closed sequence on
$S-Y_S$ identifies the desired zero object with the cone of

$$
 R\Gamma(S-Y_S,\mathbf F_\ell)
 \longrightarrow R\Gamma(X_S-z,\mathbf F_\ell).
$$

Both complexes have cohomology $\mathbf F_\ell$ in degree zero,
$\mathbf F_\ell(-1)$ in degree one, and zero in all other degrees.
For the surface this follows from localization, acyclicity of the
strictly local schemes $S,Y_S$, and
$i_{Y_S}^!\mathbf F_\ell=\mathbf F_\ell(-1)[-2]$; this purity
identity follows by transitivity from the smooth dualizing complexes
of $S$ and $Y_S$. For the punctured trait, vanishing in degrees
$\geq2$ follows from Proposition [sk-prop-curve-affine-kummer] by
passing to the filtered limit of punctured curve neighbourhoods.
Its Kummer sequence gives
$H^1(-,\mu_\ell)=K^*/K^{*\ell}\simeq\mathbf Z/\ell$, where $K$ is the
fraction field: the units of the strictly henselian trait are
$\ell$-divisible, and a uniformizer has residue one, the valuation
residue of the curve appendix. The restriction is the identity in
degree zero. A local equation of $Y_S$ restricts to a uniformizer on
$X_S$, so its Kummer residue is one on both sides and restriction is
an isomorphism in degree one as well. Hence the cone is zero, and
$M_z=0$ in $D(A)$ by conservativity.

Away from $z$ only the divisor $Y$ remains. Abhyankar's lemma along
the regular divisor $Y$
([Stacks, Tag 0EYG](https://stacks.math.columbia.edu/tag/0EYG)) says that, étale locally on $Y$, a finite
tame local system is trivialized by a Kummer cover of a local
parameter of $Y$ and an unramified cover. Our finite $\ell$-group
monodromy is tame, because wild inertia is pro-$p$. Consequently the
stalks of $Rj_*E$ are the continuous cohomology of the same tame
inertia representation, and their specialization maps along $Y-z$
are isomorphisms. Explicitly, the pro-$\ell$ part of tame inertia is
$\mathbf Z_\ell(1)$; its cohomology on a finite $\ell$-primary
module is computed by the two-term complex of a topological
generator minus one, and the other prime-to-$p$ factors have exact
invariants on these coefficients. Since the parameter and the
unramified cover can be chosen on an étale neighbourhood, this
description, including the specialization maps, is locally constant.
Applying the argument to the cohomology sheaves of $E$ and using the
bounded spectral sequence proves the assertion for $E$.

For the last assertion, choose a geometric generic point $\bar\eta$
of the connected regular curve $Y$. Choose also specialization maps
from $\bar\eta$ to $z$ and to $s$. Naturality of restriction gives the
commutative square in $D(A)$

$$
\begin{CD}
 R\Gamma(Y,M|_Y) @>>> M_s\\
 @VVV @VV{\sim}V\\
 M_z=0 @>>> M_{\bar\eta}.
\end{CD}
$$

The right arrow is an isomorphism by the local constancy just
proved, so the upper arrow is zero as a morphism in $D(A)$.
