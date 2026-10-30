+++
kind = "proof"
of = "sk-lem-proper-heart-bound"
uses = ["sk-lem-coefficient-heart", "sk-lem-lisse-finite-descent", "sk-lem-stratified-lattice", "sk-prop-pe-milnor", "sk-lem-proper-heart-continuity", "sk-thm-sfb-proper-base-change"]
+++
*Reduction to a lattice.* If $R^qp_*$ vanishes for $q>2d+1$ on two
sheaves, it vanishes on every extension of one by the other. By Lemma [sk-lem-coefficient-heart](3), every
$M\in\Cons(X,\Lambda)$ is a finite extension of sheaves $a_!L$, with
$a:S\hookrightarrow X$ a locally closed immersion and $L$ lisse. For
$\Lambda=\overline{\mathbf Q}_\ell$, $L$ is the scalar extension $\QbarX\otimes_{E}L_E$ of a
lisse $E_S$-module $L_E$ for some finite $E/\Ql$
(Lemma [sk-lem-lisse-finite-descent]). For $\Lambda=E$, we put
$L_E=L$. By Lemma [sk-lem-stratified-lattice], after refining $S$ by a
finite stratification (which replaces $a_!L$ by a finite extension of
sheaves of the same form), $L_E$ contains a lisse finite free
$\mathcal O_{E,S}$-lattice $L_0$ with $L_0[1/\ell]=L_E$. Hence it is
enough to prove the bound for $a_!L_0$, and then to pass to
$a_!L_E=(a_!L_0)[1/\ell]$ and, if $\Lambda=\overline{\mathbf Q}_\ell$, to its scalar
extension $a_!L$.

In the passage to the limit below we use that the sheaf $a_!L_0$ is
derived $\pi_E$-complete. To see this, note that $a$ is a closed
immersion composed with a quasi-compact open immersion. Closed pushforward
is exact and preserves products [Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM), and extension by zero is
exact and preserves limits [Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP). Therefore both functors preserve
the derived inverse limit that expresses the completeness of $L_0$.

*The torsion bound.* Fix an affine weakly contractible $V\to Y$ and
let $p_V:X_V\to V$ be the base change of $p$, which is proper with the same
bound $d$. Since $L_0$ is flat, $a_!L_0\otimes^{\mathbf L}_{\mathcal O_E} \mathcal O_E/\pi_E^n$ is the sheaf $a_!(L_0/\pi_E^n)$, which is the pullback
to the pro-étale site of a classical constructible étale sheaf of
$\mathcal O_E/\pi_E^n$-modules. The scheme $V$ is not Noetherian, so we use
the proper vanishing theorem in the generality of [Stacks, Tag 095U](https://stacks.math.columbia.edu/tag/095U): if a
proper morphism has geometric fibres of dimension at most $d$, then its
higher direct images of torsion sheaves vanish in degrees $q>2d$.
Combining this theorem for $p_V$ with the comparison
[Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6) of étale and pro-étale direct images, we see that
$R^qp_{V,*}$ of this sheaf vanishes for $q>2d$. Since $V$ is weakly
contractible, $\Gamma(V,-)$ is exact on all pro-étale sheaves
[Stacks, Tag 0991](https://stacks.math.columbia.edu/tag/0991). Hence $H^q(X_V,-)=\Gamma(V,R^qp_{V,*}(-))$ and

$$
H^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)=0\quad(q>2d).
$$

*The limit.* Restriction to $X_V$ is exact and commutes with
products, hence with derived inverse limits. By completeness, it follows that
$(a_!L_0)|_{X_V}\simeq R\varprojlim_n a_!(L_0/\pi_E^n)|_{X_V}$.
Derived global sections also commute with derived inverse limits, since a
product of K-injective complexes is K-injective and sections preserve
products. The Milnor exact sequence (Proposition [sk-prop-pe-milnor])

$$
0\to{\textstyle\varprojlim^1_n}H^{q-1}\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)
\to H^q(X_V,a_!L_0)
\to\varprojlim_nH^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to0
$$

then shows that $H^q(X_V,a_!L_0)=0$ for $q>2d+1$, since for such $q$ both
outer terms vanish by the torsion bound.

*Back to $\Lambda$.* The sheaf $(a_!L_0)[1/\ell]$ is the filtered
colimit of $a_!L_0$ along multiplication by $\ell$, and so
Lemma [sk-lem-proper-heart-continuity] implies the same vanishing for
it. For $\Lambda=\overline{\mathbf Q}_\ell$, scalar extension from $E$ to $\overline{\mathbf Q}_\ell$ is the
filtered colimit of the extensions to finite $E'\supset E$. Each of these
is, as a sheaf of abelian groups, a finite direct sum of copies of the
original sheaf, because $E'$ is finite free over $E$, and the continuity
lemma again implies the bound. Since this holds for every affine weakly
contractible $V$, the formula $(R^qp_*M)(V)=H^q(X_V,M|_{X_V})$ from the
proof of Lemma [sk-lem-proper-heart-continuity] shows that
$R^qp_*(a_!L)=0$ for $q>2d+1$. By the first step, $R^qp_*M=0$ for $q>2d+1$
and every $M\in\Cons(X,\Lambda)$.

*Passage to $\IndCons(X,\Lambda)$.* By
Proposition [sk-thm-sfb-proper-base-change], $Rp_*$ maps
$\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$, and hence $R^qp_*M\in\Cons(Y,\Lambda)$
for constructible $M$. Every object of $\IndCons(X,\Lambda)$ is a filtered
colimit of constructible sheaves, and $R^qp_*$ commutes with filtered
colimits and direct sums by Lemma [sk-lem-proper-heart-continuity].
This proves all three assertions.
