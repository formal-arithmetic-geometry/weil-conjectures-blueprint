+++
kind = "proof"
of = "det-uniform-constructible-ext-rational"
+++
*Coefficients $E$.* By [sk-lem-stratified-lattice], after refining the strata (which replaces
$a_!L$, $b_!M$ by finite extensions of sheaves of the same form, harmless by
[det-uniform-constructible-ext-devissage]), $L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$,
$M_0$ with $L_0[1/\pi_E]=L$, $M_0[1/\pi_E]=M$. The refinement of $S$ depends only on $L$ and that of
$T$ only on $M$.

Now $a_!L=(a_!L_0)\otimes_{\mathcal O_E}E$ and

$$
b_!M=(b_!M_0)[1/\pi_E]=\varinjlim\bigl(b_!M_0\xrightarrow{\pi_E}b_!M_0\xrightarrow{\pi_E}\cdots\bigr).
$$

Extension of scalars $\mathcal O_E\to E$ is left adjoint to restriction of scalars, so

$$
R\operatorname{Hom}_E(a_!L,b_!M)=R\operatorname{Hom}_{\mathcal O_E}\bigl(a_!L_0,(b_!M_0)[1/\pi_E]\bigr).
$$

The target is a filtered colimit of sheaves in degree $0$, and $a_!L_0$ satisfies the hypothesis of
part (2) of [sk-lem-constructible-ext-continuity], so

$$
\Ext^q_E(a_!L,b_!M)=\varinjlim\bigl(\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)\xrightarrow{\pi_E}\cdots\bigr),
$$

which vanishes for $q>c_{a,L}$: by [det-uniform-constructible-ext-integral] applied to each refined
stratum $a_k$ (bound $\operatorname{cd}_\ell(j_k)+\operatorname{cd}_\ell(S_k)+2$) and dévissage along the
refinement. The refinement of $T$ does not change these bounds.

*Coefficients $\Qlb$.* By [sk-lem-lisse-finite-descent], there is a finite $E$ and constructible
$E$-sheaves $C_E$, $N_E$ (of the same form $a_!L_E$, $b_!M_E$) with $a_!L=(C_E)_{\Qlb}$ and
$b_!M=(N_E)_{\Qlb}$. Since $\overline{\mathbf Q}_{\ell,X}=\varinjlim_{E'}E'_X$ (filtered over finite
$E'\supset E$) is flat over $E_X$, adjunction gives

$$
R\operatorname{Hom}_{\Qlb}((C_E)_{\Qlb},(N_E)_{\Qlb})=R\operatorname{Hom}_E\bigl(C_E,\varinjlim_{E'}(N_E)_{E'}\bigr),
$$

and [sk-lem-constructible-ext-continuity] identifies its $H^q$ with
$\varinjlim_{E'}\Ext^q_E(C_E,(N_E)_{E'})=\varinjlim_{E'}\Ext^q_{E'}((C_E)_{E'},(N_E)_{E'})$. After
refining the strata, $L_E$ contains a lisse $\mathcal O_E$-lattice $L_{E,0}$, and
$L_{E,0}\otimes_{\mathcal O_E}\mathcal O_{E'}$ is a lisse $\mathcal O_{E'}$-lattice in $(L_E)_{E'}$ on the
same strata. So the case of $E'$ applies on these strata with the bound $c_{a,L}$, which does not depend
on $E'$, and each term vanishes for $q>c_{a,L}$; hence so does the colimit.
