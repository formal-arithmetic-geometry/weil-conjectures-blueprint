+++
kind = "proof"
of = "lemma-uniform-bound-proper-direct-image--1"
order = 483002
uses = ["proposition-pro-etale-affines-form-basis", "definition-lisse-sheaves", "lemma-descent-finite-coefficient-field", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-torsion-sheaves", "proposition-dctf-x-qbar-2-colimit", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "definition-derived-adic-completeness--1", "lemma-reduction-derived-nakayama--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--4", "definition-constructible-sheaves--6", "proposition-integral-constructibility-criterion--1", "lemma-constructible-sheaves--8", "lemma-descent-finite-coefficient-field--3", "lemma-descent-finite-coefficient-field--2", "lemma-lattices-after-finite-stratification--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "proposition-proper-base-change-complete-integral--1", "proposition-comparison-etale-derived-category--5", "lemma-structure-integral-constructible-complexes--3", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
*Reduction to a lattice.* The vanishing statement is stable under
extensions: if $R^qp_*$ vanishes for $q>2d+1$ on two
sheaves, it vanishes on every extension of one by the other. By Lemma [lemma-constructible-sheaves](3), every
$M\in\Cons(X,\Lambda)$ is a finite extension of sheaves $a_!L$, with
$a:S\hookrightarrow X$ a locally closed immersion and $L$ lisse. For
$\Lambda=\overline{\mathbf Q}_\ell$, $L$ is the scalar extension $\QbarX\otimes_{E}L_E$ of a
lisse $E_S$-module $L_E$ for some finite $E/\mathbf Q_\ell$
(Lemma [lemma-descent-lisse-qbar-sheaves-finite]). For $\Lambda=E$, we put
$L_E=L$. We may refine $S$ by a finite stratification, since this
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
$\mathcal O_E/\pi_E^n$-modules. The scheme $V$ is not Noetherian, so we use
the proper vanishing theorem in the generality of [Stacks, [095U](https://stacks.math.columbia.edu/tag/095U)]: if a
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
to $a_!L_0$. Restriction to $X_V$ is exact and commutes with
products, hence with derived inverse limits. Completeness therefore gives
$(a_!L_0)|_{X_V}\simeq R\varprojlim_n a_!(L_0/\pi_E^n)|_{X_V}$.
Derived global sections also commute with derived inverse limits, since a
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
quasi-compact and quasi-separated scheme $X_V$ commutes with them. The sheaf
$(a_!L_0)[1/\ell]$ is the filtered colimit of $a_!L_0$ along multiplication
by $\ell$, and so it has the same vanishing. For $\Lambda=\overline{\mathbf Q}_\ell$, scalar extension from $E$ to $\overline{\mathbf Q}_\ell$ is the
filtered colimit of the extensions to finite $E'\supset E$. Since $E'$ is
finite free over $E$, each of these
is, as a sheaf of abelian groups, a finite direct sum of copies of the
original sheaf. The continuity lemma again gives the bound. As $V$ was an
arbitrary affine weakly contractible object, formula
(5.5) shows that
$R^qp_*(a_!L)=0$ for $q>2d+1$. By the first step, $R^qp_*M=0$ for $q>2d+1$
and every $M\in\Cons(X,\Lambda)$.

*Passage to $\IndCons(X,\Lambda)$.* For constructible $M$ we have
$R^qp_*M\in\Cons(Y,\Lambda)$, because $Rp_*$ maps
$\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$ by
Proposition [proposition-proper-direct-image-constructible-complexes].
Every object of $\IndCons(X,\Lambda)$ is a filtered colimit of
constructible sheaves, and $R^qp_*$ commutes with filtered colimits and
direct sums by Corollary [corollary-continuity-cohomology]. All three
assertions for $\IndCons(X,\Lambda)$ follow.

*Source:* the proof of Lemma [lemma-uniform-bound-proper-direct-image].
