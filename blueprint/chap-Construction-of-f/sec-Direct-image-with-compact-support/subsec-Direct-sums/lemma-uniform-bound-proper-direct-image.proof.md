+++
kind = "proof"
of = "lemma-uniform-bound-proper-direct-image"
order = 485
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "definition-ind-constructible-sheaves", "proposition-ind-constructible-sheaves", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
*Reduction to a lattice.* The vanishing statement is stable under
extensions: if $R^qp_*$ vanishes for $q>2d+1$ on two
sheaves, it vanishes on every extension of one by the other. By Lemma [lemma-constructible-sheaves](3), every
$M\in\Cons(X,\Lambda)$ is a finite extension of sheaves $a_!L$, with
$a:S\hookrightarrow X$ a locally closed immersion and $L$ lisse. Moreover, for $\Lambda=\overline{\mathbf Q}_\ell$, $L$ is the scalar extension $\QbarX\otimes_{E}L_E$ of a
lisse $E_S$-module $L_E$ for some finite $E/\mathbf Q_\ell$
(Lemma [lemma-descent-lisse-qbar-sheaves-finite]). For $\Lambda=E$, we simply put $L_E=L$. In both cases we may refine $S$ by a finite stratification, since this
replaces $a_!L$ by a finite extension of sheaves of the same form. By
Lemma [lemma-lattices-after-finite-stratification], after such a
refinement $L_E$ contains a lattice $L_0$,
locally free of finite rank over $\mathcal O_{E,S}$, with $L_0[1/\ell]=L_E$. Hence it is
enough to prove the bound for $a_!L_0$, and then to pass to
$a_!L_E=(a_!L_0)[1/\ell]$ and, if $\Lambda=\overline{\mathbf Q}_\ell$, to its scalar
extension $a_!L$.

In the passage to the limit below we use that the sheaf $a_!L_0$ is
derived $\pi_E$-complete. To see this, note that $a$ is a closed
immersion composed with a quasi-compact open immersion. Closed pushforward
is exact and preserves products [Stacks, [09BM](https://stacks.math.columbia.edu/tag/09BM)], and extension by zero is
exact and preserves limits [Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)]. Therefore both functors preserve
the derived inverse limit that expresses the completeness of $L_0$.

*The torsion bound.* Over the objects $V$ that compute $R^qp_*$,
the reductions $a_!(L_0/\pi_E^n)$ have cohomology only up to degree $2d$. Fix an affine weakly contractible $V\to Y$ and
let $p_V:X_V\to V$ be the base change of $p$, which is proper with the same
bound $d$. Since $L_0$ is flat, $a_!L_0\otimes^{\mathbf L}_{\mathcal O_E}
\mathcal O_E/\pi_E^n$ is the sheaf $a_!(L_0/\pi_E^n)$, which is the pullback
to the pro-étale site of a classical constructible étale sheaf of
$\mathcal O_E/\pi_E^n$-modules. Since the scheme $V$ is not Noetherian, we use the proper vanishing theorem in the generality of [Stacks, [095U](https://stacks.math.columbia.edu/tag/095U)]: if a
proper morphism has geometric fibres of dimension at most $d$, then its
higher direct images of torsion sheaves vanish in degrees $q>2d$.
With the comparison [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)] of étale and pro-étale direct
images, this theorem for $p_V$ says that $R^qp_{V,*}$ of this sheaf
vanishes for $q>2d$. As $V$ is weakly contractible, $\Gamma(V,-)$ is
exact on all pro-étale sheaves [Stacks, [0991](https://stacks.math.columbia.edu/tag/0991)]. Hence
$H^q(X_V,-)=\Gamma(V,R^qp_{V,*}(-))$, and

$$
H^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)=0\quad(q>2d).
$$

*The limit.* Derived completeness lets us pass from the reductions
to $a_!L_0$. Since restriction to $X_V$ is exact and commutes with products, hence with derived inverse limits, completeness gives
$(a_!L_0)|_{X_V}\simeq R\varprojlim_n a_!(L_0/\pi_E^n)|_{X_V}$.
Derived global sections, too, commute with derived inverse limits, since a
product of K-injective complexes is K-injective and sections preserve
products. The Milnor exact sequence of Proposition [proposition-milnor-sequence]

$$
0\to{\textstyle\varprojlim^1_n}H^{q-1}\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)
\to H^q(X_V,a_!L_0)
\to\varprojlim_nH^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to0
$$

then shows that $H^q(X_V,a_!L_0)=0$ for $q>2d+1$, since for such $q$ both
outer terms vanish by the torsion bound.

*Back to $\Lambda$.* The remaining passages are filtered colimits.
By Corollary [corollary-continuity-cohomology], cohomology on the
quasi-compact and quasi-separated scheme $X_V$ commutes with them. For instance, the sheaf $(a_!L_0)[1/\ell]$ is the filtered colimit of $a_!L_0$ along multiplication
by $\ell$, and so it has the same vanishing. For $\Lambda=\overline{\mathbf Q}_\ell$, scalar extension from $E$ to $\overline{\mathbf Q}_\ell$ is the
filtered colimit of the extensions to finite $E'\supset E$. Since $E'$ is
finite free over $E$, each of these
is, as a sheaf of abelian groups, a finite direct sum of copies of the
original sheaf. Hence the continuity lemma again gives the bound. As $V$ was an
arbitrary affine weakly contractible object, formula
(5.5) shows that
$R^qp_*(a_!L)=0$ for $q>2d+1$. By the first step, $R^qp_*M=0$ for $q>2d+1$
and every $M\in\Cons(X,\Lambda)$.

*Passage to $\IndCons(X,\Lambda)$.* For constructible $M$ we have
$R^qp_*M\in\Cons(Y,\Lambda)$, because $Rp_*$ maps
$\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$ by
Proposition [proposition-proper-direct-image-constructible-complexes].
Moreover, every object of $\IndCons(X,\Lambda)$ is a filtered colimit of
constructible sheaves, and $R^qp_*$ commutes with filtered colimits and
direct sums by Corollary [corollary-continuity-cohomology]. All three assertions for $\IndCons(X,\Lambda)$ therefore follow.
