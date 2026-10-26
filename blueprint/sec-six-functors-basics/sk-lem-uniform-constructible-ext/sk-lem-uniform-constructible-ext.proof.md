+++
kind = "proof"
of = "sk-lem-uniform-constructible-ext"
uses = ["sk-lem-coefficient-heart", "sk-lem-formal-closed-support", "sk-lem-formal-closed-support-ii", "sk-lem-stratified-lattice", "sk-lem-integral-models", "sk-lem-constructible-ext-continuity", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-base-field-cd", "sk-def-cd"]
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

*Lattices.* Take first $\Lambda=E$. After refining the stratifications ([sk-lem-stratified-lattice]),
$L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$ and $M_0$. The refinement of the source stratum
depends only on $L$, and that of the target only on $M$, so the bound obtained for the refined source
strata is still independent of $N$.

By parts (3) and (4) of [sk-lem-integral-models], $b_!M_0$ lies in $\Dbc(X,\mathcal O_E)$, so it is
derived complete, and its reductions

$$
b_!M_0\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathcal O_{E,X}/\pi_E^n=b_!(M_0/\pi_E^n)
$$

are constructible torsion sheaves, pulled back from $X_{\mathrm{ét}}$ because extension by zero and closed
direct image commute with this pullback (Stacks, Tags 09AF, 09A6). The equality holds because $b_!$ is
exact and $M_0$ is $\pi_E$-torsion free.

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

*The case $\Lambda=\Qlb$.* By [sk-thm-sfb-qlbar-two-colimit], there are a finite $E$ and lisse
$E$-sheaves $L'$, $M'$ with $L=L'_{\Qlb}$ and $M=M'_{\Qlb}$, so that $a_!L=(a_!L')_{\Qlb}$ and
$b_!M=(b_!M')_{\Qlb}$, and

$$
\Ext^q_{\Qlb}(a_!L,b_!M)=\varinjlim_{E'\supset E}\Ext^q_{E'}\bigl((a_!L')_{E'},(b_!M')_{E'}\bigr).
$$

The groups on the right vanish for $q$ above a bound independent of $E'$. Indeed, after refining the
strata, $L'$ contains a lisse $\mathcal O_E$-lattice $L'_0$, and $L'_0\otimes_{\mathcal O_E}\mathcal O_{E'}$
is a lisse $\mathcal O_{E'}$-lattice in $(L')_{E'}$ on the same strata. The case $\Lambda=E'$ therefore
gives the bound $\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ for each refined stratum $S$,
which does not depend on $E'$ ([det-uniform-constructible-ext-rational]).
