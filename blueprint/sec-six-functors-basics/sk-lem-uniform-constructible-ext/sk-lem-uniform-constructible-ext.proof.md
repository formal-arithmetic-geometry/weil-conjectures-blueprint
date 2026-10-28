+++
kind = "proof"
of = "sk-lem-uniform-constructible-ext"
uses = ["sk-lem-coefficient-heart", "sk-lem-formal-closed-support", "sk-lem-base-field-cd", "sk-lem-stratified-lattice", "sk-lem-integral-models", "sk-lem-formal-closed-support-ii", "sk-lem-constructible-ext-continuity", "sk-lem-lisse-finite-descent", "sk-thm-sfb-qlbar-two-colimit"]
+++
By the long exact Ext sequences, a bound that holds for every subquotient of a finite filtration of
the source holds for the source (take the maximum). Likewise, a bound that holds for every subquotient
of a finite filtration of the target holds for the target, with the same value. Hence, by part (3) of
[sk-lem-coefficient-heart], we may assume $C=a_!L$, with
$a=i\circ u\colon S\hookrightarrow Z\hookrightarrow X$ as in [sk-lem-formal-closed-support] and $L$
lisse, and it suffices to find an integer $d$, depending only on $a$ and $L$, with
$\Ext^q(a_!L,b_!M)=0$ for $q>d$, for all locally closed $b\colon T\hookrightarrow X$ and lisse $M$ on
$T$ ([det-uniform-constructible-ext-devissage]). Let $j\colon X\setminus Z\hookrightarrow X$ be the open
complement of $Z$. When $L$ contains a lisse $\mathcal O_E$-lattice, we show that
$d=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ works. Both cohomological dimensions are
finite by [Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10) and [sk-lem-base-field-cd].

*Lattices.* First take $\Lambda=E$. After refining the stratifications ([sk-lem-stratified-lattice]),
$L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$ and $M_0$. The refinement of the source stratum
depends only on $L$, and that of the target only on $M$, so the bound obtained for the refined source
strata is still independent of $N$.

By parts (3) and (4) of [sk-lem-integral-models], $b_!M_0$ lies in $\Dbc(X,\mathcal O_E)$, so it is
derived complete, and its reductions

$$
b_!M_0\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathcal O_{E,X}/\pi_E^n=b_!(M_0/\pi_E^n)
$$

are constructible torsion sheaves, pulled back from $X_{\mathrm{ét}}$ because extension by zero and closed
direct image commute with this pullback ([Stacks, Tag 09AF](https://stacks.math.columbia.edu/tag/09AF),
[Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6)). The equality holds because $b_!$ is
exact and $M_0$ is $\pi_E$-torsion free.

*Torsion targets.* By [Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6), $Rj_*$ in
$\D(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$ of a sheaf pulled back from the étale site is the pullback of
its direct image in $\D(X_{\mathrm{ét}},\mathcal O_E/\pi_E^n)$. Hence $Rj_*j^*b_!(M_0/\pi_E^n)$ has
cohomology in degrees $[0,\operatorname{cd}_\ell(j)]$, and the fibre formula of part (1) of
[sk-lem-formal-closed-support] shows that

$$
R\underline\Gamma_Z\,b_!(M_0/\pi_E^n)\in\D^{[0,\operatorname{cd}_\ell(j)+1]}(Z_{\mathrm{proét}},\mathcal O_E/\pi_E^n),
$$

with cohomology sheaves that are torsion sheaves pulled back from the étale site, though not
necessarily constructible. Tensoring with the lisse $L_0^\vee/\pi_E^n$ and using the hypercohomology
spectral sequence on $S$, we find that

$$
H^q R\Gamma\bigl(S,(L_0^\vee/\pi_E^n)\otimes u^*R\underline\Gamma_Z\,b_!(M_0/\pi_E^n)\bigr)=0
\quad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+1),
\tag{T}
$$

for every $n$, $b$ and $M_0$ ([det-uniform-constructible-ext-torsion]).

*Integral targets.* Consider the complex $L_0^\vee\otimes u^*R\underline\Gamma_Z\,b_!M_0$. By
[sk-lem-formal-closed-support-ii], the functors that form it commute with derived inverse limits of
sequences. They also commute with reduction modulo $\pi_E^n$, which is the cone of multiplication by
$\pi_E^n$. Since $b_!M_0$ is derived complete, so is this complex, and its reductions are the complexes
in (T). Derived global sections preserve products and cones, and hence derived inverse limits. Using
the formula of part (2) of [sk-lem-formal-closed-support] with $\mathcal O_E$ coefficients, that is,
for $\RHom$ in $\D(X_{\mathrm{proét}},\mathcal O_E)$, we get

$$
\RHom_X(a_!L_0,b_!M_0)
=R\Gamma\bigl(S,L_0^\vee\otimes u^*R\underline\Gamma_Z\,b_!M_0\bigr)
=R\varprojlim_n R\Gamma\bigl(S,(L_0^\vee\otimes u^*R\underline\Gamma_Z\,b_!M_0)\otimes^{\mathbf L}\mathcal O_E/\pi_E^n\bigr).
$$

A derived inverse limit of a sequence raises an upper bound on cohomology by at most one, since it is the
fibre of the difference of the identity and the transition maps on the product, and products of abelian
groups are exact (this is the Milnor sequence,
[Stacks, Tag 08TB](https://stacks.math.columbia.edu/tag/08TB)). It follows that

$$
\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)=0\quad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2)
\tag{I}
$$

([det-uniform-constructible-ext-integral]).

*Inverting $\pi_E$.* We have $a_!L=a_!L_0[1/\pi_E]$ and
$b_!M=(b_!M_0)[1/\pi_E]=\varinjlim(b_!M_0\xrightarrow{\pi_E}b_!M_0\xrightarrow{\pi_E}\cdots)$. By the
adjunction between extension and restriction of scalars,

$$
\RHom_E\bigl(a_!L,b_!M\bigr)=\RHom_{\mathcal O_E}\bigl(a_!L_0,(b_!M_0)[1/\pi_E]\bigr),
$$

and by part (2) of [sk-lem-constructible-ext-continuity] the cohomology of the right side is the
colimit of the groups $\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)$. Hence (I) implies the bound for $E$.

*The case $\Lambda=\Qlb$.* By [sk-lem-lisse-finite-descent], there are a finite $E$ and lisse
$E$-sheaves $L'$, $M'$ with $L=L'_{\Qlb}$ and $M=M'_{\Qlb}$, so that $a_!L=(a_!L')_{\Qlb}$ and
$b_!M=(b_!M')_{\Qlb}$. By part (1) of [sk-thm-sfb-qlbar-two-colimit],

$$
\Ext^q_{\Qlb}(a_!L,b_!M)=\varinjlim_{E'\supset E}\Ext^q_{E'}\bigl((a_!L')_{E'},(b_!M')_{E'}\bigr),
$$

and the groups on the right vanish for $q$ above a bound independent of $E'$. Indeed, after refining
the strata, $L'$ contains a lisse $\mathcal O_E$-lattice $L'_0$, and $L'_0\otimes_{\mathcal O_E}\mathcal O_{E'}$
is a lisse $\mathcal O_{E'}$-lattice in $(L')_{E'}$ on the same strata. The case $\Lambda=E'$ therefore
gives the bound $\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ for each refined stratum $S$,
which does not depend on $E'$ ([det-uniform-constructible-ext-rational]).
