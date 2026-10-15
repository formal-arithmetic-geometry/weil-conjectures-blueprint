+++
kind = "proof"
of = "sk-lem-uniform-constructible-ext"
uses = ["sk-lem-coefficient-heart", "sk-lem-formal-closed-support", "sk-lem-formal-closed-support-ii", "sk-lem-stratified-lattice", "sk-lem-constructible-ext-continuity", "sk-lem-coefficient-finite-descent", "sk-lem-base-field-cd", "sk-def-cd"]
+++
By the long exact Ext sequences, a bound that holds for every subquotient of a finite filtration of
the source holds for the source (take the maximum), and a bound that holds for every subquotient of a
finite filtration of the target holds for the target, with the same value. By part (3) of
[sk-lem-coefficient-heart] we may therefore assume $C=a_!L$, with
$a=i\circ u\colon S\hookrightarrow Z\hookrightarrow X$ as in [sk-lem-formal-closed-support] and $L$
lisse, and it suffices to prove

$$
\Ext^q(a_!L,b_!M)=0\qquad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2)
$$

for all locally closed $b\colon T\hookrightarrow X$ and lisse $M$ on $T$, where
$j\colon X\setminus Z\hookrightarrow X$ is the open complement of $Z$ ([det-uniform-constructible-ext-devissage]).
Both cohomological dimensions are finite by Stacks, Tag 0F10 and [sk-lem-base-field-cd], and the bound
depends only on $a$.

*Lattices.* Take first $\Lambda=E$. After refining the stratifications ([sk-lem-stratified-lattice])
and enlarging $E$, $L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$ and $M_0$. Enlarging $E$ is
harmless: if $E'/E$ is finite, then $E'_X$ is finite free over $E_X$, so $\Ext^q_{E'}$ of the extended
sheaves is a finite direct sum of copies of $\Ext^q_E$, and a bound over $E'$ gives the same bound over
$E$. The functor $b_!$ is the composite of an extension by zero, which is exact and preserves limits
(Stacks, Tag 09BP), and a closed direct image, which is exact (Stacks, Tag 09BM) and preserves limits as a
right adjoint. Hence $b_!M_0$ is a $\pi_E$-torsion free, derived complete sheaf, and its reductions are

$$
b_!M_0\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathcal O_{E,X}/\pi_E^n=b_!(M_0/\pi_E^n).
$$

These are constructible torsion sheaves pulled back from $X_{\mathrm{ét}}$: lisse torsion sheaves descend
(Stacks, Tag 099Y), and extension by zero and closed direct image commute with this pullback
(Stacks, Tags 09AF, 09A6).

*Torsion targets.* By Stacks, Tag 09A6, $Rj_*$ in $\D(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$ of a sheaf
pulled back from the étale site is the pullback of its direct image in
$\D(X_{\mathrm{ét}},\mathcal O_E/\pi_E^n)$, so $Rj_*j^*b_!(M_0/\pi_E^n)$ has cohomology in degrees
$0,\dots,\operatorname{cd}_\ell(j)$. The fiber formula of part (1) of [sk-lem-formal-closed-support]
then gives

$$
R\underline\Gamma_Z\,b_!(M_0/\pi_E^n)\in\D^{[0,\operatorname{cd}_\ell(j)+1]}(Z_{\mathrm{proét}},\mathcal O_E/\pi_E^n),
$$

with cohomology sheaves that are torsion sheaves pulled back from the étale site, though not
necessarily constructible. Tensoring with the lisse $L_0^\vee/\pi_E^n$ and using the hypercohomology
spectral sequence on $S$ gives the torsion stratum bound

$$
H^q R\Gamma\bigl(S,(L_0^\vee/\pi_E^n)\otimes u^*R\underline\Gamma_Z\,b_!(M_0/\pi_E^n)\bigr)=0
\quad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+1),
$$

for every $n$, $b$ and $M_0$ ([det-uniform-constructible-ext-torsion]).

*Integral targets.* Write $F=L_0^\vee\otimes u^*R\underline\Gamma_Z\,b_!M_0$. By
[sk-lem-formal-closed-support-ii] the functors forming $F$ commute with derived inverse limits of
sequences; they also commute with reduction modulo $\pi_E^n$, which is the cone of multiplication by
$\pi_E^n$. Since $b_!M_0$ is derived complete, so is $F$, and the reductions of $F$ are the complexes in
the torsion stratum bound. Derived global sections preserve products and cones, hence derived inverse
limits. Using part (2) of [sk-lem-formal-closed-support] with $\mathcal O_E$ coefficients, that is, for
$R\operatorname{Hom}$ in $\D(X_{\mathrm{proét}},\mathcal O_E)$,

$$
R\operatorname{Hom}_X(a_!L_0,b_!M_0)=R\Gamma(S,F)
=R\varprojlim_n R\Gamma\bigl(S,F\otimes^{\mathbf L}\mathcal O_E/\pi_E^n\bigr).
$$

A derived inverse limit of a sequence raises an upper bound on cohomology by at most one: it is the
fiber of $1-\mathrm{shift}$ on the product, and products of abelian groups are exact (this is the
Milnor sequence, Stacks, Tag 08TB). Therefore

$$
\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)=0\quad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2)
$$

([det-uniform-constructible-ext-integral]).

*Inverting $\pi_E$.* We have $a_!L=a_!L_0[1/\pi_E]$ and
$b_!M=(b_!M_0)[1/\pi_E]=\varinjlim(b_!M_0\xrightarrow{\pi_E}b_!M_0\xrightarrow{\pi_E}\cdots)$. The
adjunction between extension and restriction of scalars gives

$$
R\operatorname{Hom}_E\bigl(a_!L,b_!M\bigr)=R\operatorname{Hom}_{\mathcal O_E}\bigl(a_!L_0,(b_!M_0)[1/\pi_E]\bigr),
$$

and by part (2) of [sk-lem-constructible-ext-continuity] the cohomology of the right side is the
colimit of the groups $\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)$. So the integral bound gives the bound for
$E$.

*The case $\Lambda=\Qlb$.* By [sk-lem-coefficient-finite-descent], $a_!L$ and $b_!M$ are extensions of
scalars of sheaves defined over a common finite $E$. Since $\overline{\mathbf Q}_{\ell,X}=\varinjlim_{E'}E'_X$
is flat over $E_X$, extension and restriction of scalars and [sk-lem-constructible-ext-continuity]
identify $\Ext^q_{\Qlb}(a_!L,b_!M)$ with the colimit of the corresponding groups over finite
extensions $E'$ of $E$, which vanish in the same range ([det-uniform-constructible-ext-rational]).
