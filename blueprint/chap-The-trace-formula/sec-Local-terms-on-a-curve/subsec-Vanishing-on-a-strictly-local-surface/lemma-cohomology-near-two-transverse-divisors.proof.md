+++
kind = "proof"
of = "lemma-cohomology-near-two-transverse-divisors"
order = 973
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "lemma-punctured-surface-punctured-curve", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The idea is that, since the monodromy is an $\ell$-group, we may filter
the coefficients until they become the constant sheaf $\mathbf F_\ell$.
For constant coefficients, $M_z=0$ is a statement on the strict localization
of $X$ at $z$: restriction from the complement of $D_2$ to the punctured
curve $D_1-z$ is an isomorphism on cohomology. This holds because a
local equation of $D_2$ gives the generator of $H^1$ on both sides. Once we
know that $M$ is locally constant along $D_2-z$, the vanishing of the
restriction map follows from $M_z=0$ by specialization along $D_2$.

For the assertion at $z$, pass to the strict localization $S$ of
$X$ at $z$ and write $D_{1,S},D_{2,S}$ for the two transverse divisors.
By the formula for stalks of a direct image along an open immersion
[Stacks, [03Q7](https://stacks.math.columbia.edu/tag/03Q7)] and localization we have

$$
M_z=R\Gamma(S-D_{2,S},j'_!N).
$$

To prove that this object is zero we may forget the $A$-action,
since the exact forgetful functor is conservative and the cohomology of
sheaves of modules agrees with the cohomology of the underlying abelian sheaves
[Stacks, [03FD](https://stacks.math.columbia.edu/tag/03FD)]. A finite abelian $\ell$-group with an action of a
finite $\ell$-group has a finite filtration whose quotients are
$\mathbf F_\ell$ with trivial action. To see this, filter by powers of
$\ell$ and use the nilpotence of the augmentation ideal of the group algebra over
$\mathbf F_\ell$. Since $j'_!$ and $R\Gamma(S-D_{2,S},-)$ are exact, the
class of $N$ for which $R\Gamma(S-D_{2,S},j'_!N)=0$ is closed under
extensions. Using truncations and these composition series we reduce
the assertion to $N=\mathbf F_\ell$ on $S-(D_{1,S}\cup D_{2,S})$.

By Lemma [lemma-punctured-surface-punctured-curve], applied to $S$ with the
divisors $D_{1,S},D_{2,S}$, the restriction map
$R\Gamma(S-D_{2,S},\mathbf F_\ell)\to R\Gamma(D_{1,S}-z,\mathbf F_\ell)$ is an
isomorphism. The localization sequence for $D_{1,S}-z$ and its complement
in $S-D_{2,S}$ identifies $R\Gamma(S-D_{2,S},j'_!\mathbf F_\ell)$ with the cone
of this map, shifted by $-1$. Hence this complex is zero, and $M_z=0$ in $D(A)$ by
conservativity.

We turn to the local constancy of $M$ along $D_2-z$, where only the
divisor $D_2$ remains. Since $D_1$ meets $D_2$ only at
$z$, we have $j'_!N=N$ near $D_2-z$, so $M=Rj_*N$ there. To compute $Rj_*N$ we use Abhyankar's lemma along the regular divisor $D_2$ [Stacks, [0EYG](https://stacks.math.columbia.edu/tag/0EYG)]: étale locally on $D_2$, a finite
tame local system is trivialized by a Kummer cover of a local
parameter of $D_2$ and an unramified cover. The lemma applies here because our finite $\ell$-group monodromy is tame, wild inertia being pro-$p$. Consequently, the
stalks of $Rj_*N$ are the continuous cohomology of the same
representation of tame inertia, and their specialization maps along $D_2-z$
are isomorphisms. Explicitly, the pro-$\ell$ part of tame inertia is
$\mathbf Z_\ell(1)$. Its cohomology with coefficients in a finite $\ell$-primary
module is computed by the two-term complex given by a topological
generator minus one. On the other hand, the finite quotients of the remaining factors of tame inertia have order prime to $\ell$, so taking invariants under them is exact
on these coefficients. Finally, we may choose the parameter and the unramified cover on an étale neighbourhood. Hence this
description, including the specialization maps, is locally constant.
Applying the argument to the cohomology sheaves of $N$ and using the
bounded spectral sequence proves the assertion for $N$.

The last assertion combines the two facts just proved. A global
section of $M|_{D_2}$ specializes to every stalk. Its image at $z$ is zero,
and along $D_2-z$ specialization is an isomorphism on stalks. To make
this precise, choose a geometric generic point $\bar\eta$
of the connected regular curve $D_2$, together with specialization maps
from $\bar\eta$ to $z$ and to $w$. By naturality of restriction we get a
commutative square

$$
\begin{CD}
R\Gamma(D_2,M|_{D_2}) @>>> M_w\\
@VVV @VV{\sim}V\\
M_z=0 @>>> M_{\bar\eta}.
\end{CD}
$$

The right arrow is an isomorphism by the local constancy just
proved, so the upper arrow is zero.
