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
refinement: part (1) of [det-uniform-constructible-ext-devissage] along the finitely many fixed source
strata gives the maximum with no further degree shift, and part (2) along the refinement of $T$
(which depends only on $M$) does not change the bound.

*Coefficients $\Qlb$.* First fix, from $(a,L)$ alone and before $b$ and $M$ are chosen, the descent
field $E_0$, the lisse $E_0$-model $L_{E_0}$ of $L$, the source stratification $S=\bigsqcup_kS_k$ and
the lisse $\mathcal O_{E_0}$-lattices $L_{E_0,k}\subset L_{E_0}|_{S_k}$ of the statement. Only then, given
$b$ and $M$, [sk-lem-lisse-finite-descent] gives a finite $E\supset E_0$ and a lisse $E$-sheaf $M_E$ on
$T$ with $M=(M_E)_{\Qlb}$; put $C_E=a_!(L_{E_0})_E$ and $N_E=b_!M_E$, so that $a_!L=(C_E)_{\Qlb}$ and
$b_!M=(N_E)_{\Qlb}$. Since $\overline{\mathbf Q}_{\ell,X}=\varinjlim_{E'}E'_X$ (filtered over finite
$E'\supset E$) is flat over $E_X$, adjunction gives

$$
R\operatorname{Hom}_{\Qlb}((C_E)_{\Qlb},(N_E)_{\Qlb})=R\operatorname{Hom}_E\bigl(C_E,\varinjlim_{E'}(N_E)_{E'}\bigr),
$$

and [sk-lem-constructible-ext-continuity] identifies its $H^q$ with
$\varinjlim_{E'}\Ext^q_E(C_E,(N_E)_{E'})=\varinjlim_{E'}\Ext^q_{E'}((C_E)_{E'},(N_E)_{E'})$. After
extending the fixed lattices, $L_{E_0,k}\otimes_{\mathcal O_{E_0}}\mathcal O_{E'}$ is a lisse
$\mathcal O_{E'}$-lattice in $(L_{E_0})_{E'}|_{S_k}$ on each fixed stratum; $S$ is not refined again. So
the case of $E'$ applies on these strata with the bound $c_{a,L}$, which depends only on the source data
fixed above, not on $E'$, $b$ or $M$, and each term vanishes for $q>c_{a,L}$; hence so does the colimit.
