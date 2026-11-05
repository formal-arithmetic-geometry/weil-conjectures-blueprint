+++
kind  = "proof"
of    = "lemma-weil-pbc-etale-degree-zero"
+++
Naturality in $F$ holds because $i^\sharp$ is the unit $F\to i_*i^{-1}F$
evaluated on $Y$ [def-weil-pbc-finite-section-pullback]. Whether $i^\sharp$ is
bijective only depends on the underlying abelian sheaves, so we may assume that
$F$ is an abelian sheaf. Put $S=\operatorname{Spec}A$. Two facts are used
throughout. *(a)* For every finite $h:Y'\to Y$ the composite $Y'\to S$ is proper
(finite morphisms are proper, [lem-weil-pbc-finite-proper]), so by
[lemma-weil-pbc-stein-connectedness] the space $Y'$ is spectral, its closed fibre
$Y'_0=Y'\times_SS_0$ is closed, and every irreducible closed subset of $Y'$ meets
$Y'_0$ in a nonempty connected subset. *(b)* In particular every nonempty closed
subset of $Y'$ meets $Y'_0$, since the image in $S$ of a nonempty closed subset
is closed, hence contains a maximal ideal, which contains $I$ because $I$ lies in
the Jacobson radical.

*Injectivity.* Let $s\in\Gamma(Y',F')$, for $Y'$ finite over $Y$ and $F'$ an
abelian sheaf on $Y'$, with $i'^\sharp s=0$ on $Y'_0$. By the definition of
inverse image and sheafification, every point of $Y'_0$ has an etale
neighbourhood in $Y'$ on which $s$ restricts to zero; the images of these etale
neighbourhoods form an open subset $V\supseteq Y'_0$ of $Y'$ on which the germs
of $s$ vanish. The complement of $V$ is closed and does not meet $Y'_0$, hence is
empty by (b). So $s=0$ by the sheaf property. This applies in particular to $Y$
itself and to the finite $Y$-schemes used below.

*Surjectivity.* Let $t\in\Gamma(Y_0,i^{-1}F)$. Every point of $Y_0$ has an etale
$U_k\to Y$ whose image contains it, with a section $g_k\in F(U_k)$ whose
restriction to $U_k\times_YY_0$ is the restriction of $t$; as $Y_0$ is
quasi-compact, finitely many $U_k$ suffice. The morphism
$\coprod_kU_k\amalg(Y\setminus Y_0)\to Y$ is etale and surjective, and $Y$ is
quasi-compact and quasi-separated, so
[lemma-weil-pbc-finite-refinement-etale-cover] gives a finite surjective
$r:Y'\to Y$ and a finite open covering $Y'=\bigcup_aW_a$ with $Y$-maps from
$W_a$ to the members of this cover. The opens $W_a$ mapping to some $U_k$ carry
the pulled-back sections $r^{-1}g_k$, and their restrictions to $W_a\cap Y'_0$
are the pullback $r_0^\sharp t$ of $t$ along $r_0:Y'_0\to Y_0$, by the
composition law of pullbacks [lemma-weil-pbc-finite-pullback-composition]; the
opens mapping to $Y\setminus Y_0$ do not meet $Y'_0$. Two of these local sections
therefore agree on an open subset of the overlap containing its trace on
$Y'_0$. By (a), the shrinking argument of the proof of
[lemma-weil-pbc-spectral-restriction] applies to the spectral space $Y'$ and the
closed subset $Y'_0$: the opens $W_a$ can be shrunk to opens which still cover
$Y'$, still contain $W_a\cap Y'_0$, and on whose overlaps the local sections
agree. The shrunk sections glue to $\sigma'\in\Gamma(Y',r^{-1}F)$ with
$\sigma'|_{Y'_0}=r_0^\sharp t$.

The two pullbacks of $\sigma'$ to $Y''=Y'\times_YY'$ have the same restriction
to the closed fibre $Y''_0$, namely the pullback of $t$; as $Y''\to Y$ is finite,
injectivity shows that they are equal. Since $r$ is finite and surjective,
$\sigma'$ descends: there is $s\in\Gamma(Y,F)$ with $r^\sharp s=\sigma'$ (descent
of sections along a finite surjective morphism, Stacks Project, Tag 09Z3).
Finally the pullback of $i^\sharp s-t$ along $r_0$ vanishes. Since $r_0$ is
surjective and the stalk of $r_0^{-1}G$ at a geometric point of $Y'_0$ is the
stalk of $G$ at its image in $Y_0$, every geometric stalk of $i^\sharp s-t$
vanishes, so $i^\sharp s=t$.
