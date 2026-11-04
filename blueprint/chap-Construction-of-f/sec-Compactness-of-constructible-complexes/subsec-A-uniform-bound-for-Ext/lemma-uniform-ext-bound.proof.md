+++
kind = "proof"
of = "lemma-uniform-ext-bound"
order = 443
uses = ["definition-constructible-sheaves", "lemma-ext-bound-lattices"]
+++
We reduce to extensions by zero of lisse sheaves on strata, prove the bound
for $\Lambda=E$ by choosing lattices, applying
Lemma [lemma-ext-bound-lattices] and inverting $\pi_E$, and reduce
$\Lambda=\overline{\mathbf Q}_\ell$ to finite extensions of $E$.

*Reduction to strata.* Bounds pass to extensions in either variable.
Indeed, if $0\to C'\to C\to C''\to0$ is exact, then in the long exact
sequence $\Ext^q(C'',N)\to\Ext^q(C,N)\to\Ext^q(C',N)$ the outer groups
vanish above the larger of the two bounds for $C'$ and $C''$, and so the
middle one does too. Hence a bound that holds for every subquotient of a finite
filtration of the source holds for the source, if we take the maximum.
The same sequence in the second variable shows that a bound that holds
for every subquotient of a finite filtration of the target holds for the
target, with the same value.
In view of Lemma [lemma-constructible-sheaves](3), we may therefore assume
$C=a_!L$, with $a=i\circ u:S\hookrightarrow Z\hookrightarrow X$ as in
Lemma [lemma-sections-support-closed-subscheme] and $L$ lisse. It suffices
to find an integer $d$, depending only on $a$ and $L$, with
$\Ext^q(a_!L,b_!M)=0$ for $q>d$, for all locally closed
$b:T\hookrightarrow X$ and lisse $M$ on $T$. Let
$j:X\setminus Z\hookrightarrow X$ be the open complement of $Z$. When $L$
contains a lisse $\mathcal O_E$-lattice, we show that
$d=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ works.

*Lattices.* First take $\Lambda=E$. Since torsion arguments need
integral structures, we choose lattices. After refining the
stratifications (Lemma [lemma-lattices-after-finite-stratification]),
$L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$ and $M_0$.
The refinement replaces $a_!L$ and $b_!M$ by
finite extensions of sheaves of the same form, which the first step allows.
The refinement of the source stratum depends only on $L$, and that of the
target only on $M$. So the bound obtained for the refined source strata
is still independent of $N$.

The lattices are locally free of finite rank over $\mathcal O_E$. Indeed,
being lisse, they are locally of the form
$\mathcal O_{E,U}\otimes_{\mathcal O_E}P$ with $P$ finitely generated
(Definition [definition-lisse-sheaves]). As subsheaves of $E$-modules
they are torsion free, so $P$ is free. Lemma [lemma-ext-bound-lattices]
now gives $\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)=0$ for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$.

*Inverting $\pi_E$.* Inverting $\pi_E$ is a filtered colimit. By
continuity of Ext out of $a_!L_0$, the Ext groups over $E$ are therefore
colimits of groups that all vanish in the same range. In detail, we have
$a_!L=a_!L_0[1/\pi_E]$ and
$b_!M=(b_!M_0)[1/\pi_E]=\varinjlim(b_!M_0\xrightarrow{\pi_E}b_!M_0\xrightarrow{\pi_E}\cdots)$.
The adjunction between extension and restriction of scalars gives

$$
R\!\operatorname{Hom}_E\bigl(a_!L,b_!M\bigr)
=R\!\operatorname{Hom}_{\mathcal O_E}\bigl(a_!L_0,(b_!M_0)[1/\pi_E]\bigr).
$$

By Lemma [lemma-continuity-ext-out-constructible-complex](2) the cohomology of
the right side is the colimit of the groups
$\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)$. Hence
(5.1) implies the bound for $E$.

*The case $\Lambda=\overline{\mathbf Q}_\ell$.* The bound for $E$ depends only on the
strata and on $\operatorname{cd}_\ell$, not on $E$, so it passes to the
colimit over finite extensions. By
Lemma [lemma-descent-lisse-qbar-sheaves-finite], there are a finite $E$ and
lisse $E$-sheaves $L'$, $M'$ with $L=L'_{\overline{\mathbf Q}_\ell}$ and $M=M'_{\overline{\mathbf Q}_\ell}$. Then
$a_!L=(a_!L')_{\overline{\mathbf Q}_\ell}$ and $b_!M=(b_!M')_{\overline{\mathbf Q}_\ell}$, and by Lemma [lemma-descent-finite-coefficient-field](1),

$$
\Ext^q_{\overline{\mathbf Q}_\ell}(a_!L,b_!M)
=\varinjlim_{E'\supset E}\Ext^q_{E'}\bigl((a_!L')_{E'},(b_!M')_{E'}\bigr),
$$

and the groups on the right vanish for $q$ above a bound independent of
$E'$. Indeed, after refining the strata, $L'$ contains a lisse
$\mathcal O_E$-lattice $L'_0$, and $L'_0\otimes_{\mathcal O_E}\mathcal O_{E'}$
is a lisse $\mathcal O_{E'}$-lattice in $(L')_{E'}$ on the same strata. The
case $\Lambda=E'$ therefore gives the bound
$\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ for each refined
stratum $S$, which does not depend on $E'$.
