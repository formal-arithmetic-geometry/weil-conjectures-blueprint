+++
kind = "proof"
of = "det-uniform-constructible-ext-rational"
+++
*Coefficients $E$.* By [sk-lem-stratified-lattice], after refining the strata (which replaces
$a_!L$, $b_!M$ by finite extensions of sheaves of the same form, harmless by
[det-uniform-constructible-ext-devissage]) and after a finite extension $E'/E$, $L$ and $M$ contain
lisse lattices $L_0$, $M_0$ with $L_0[1/\pi_E]=L$, $M_0[1/\pi_E]=M$. Enlarging $E$ is harmless: $E'_X$
is finite free over $E_X$, so the restriction of scalars of the extended sheaves is a finite direct
sum of copies of the original ones, and $\Ext^q_{E'}((a_!L)_{E'},(b_!M)_{E'})=\Ext^q_E(a_!L,(b_!M)^{\oplus[E':E]})$,
a finite direct sum of the $\Ext^q_E(a_!L,b_!M)$. So a bound over $E'$ yields the same bound over $E$.

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

which vanishes for $q>c_a$ by [det-uniform-constructible-ext-integral].

*Coefficients $\Qlb$.* By [sk-lem-coefficient-finite-descent], there is a finite $E$ and constructible
$E$-sheaves $C_E$, $N_E$ (of the same form $a_!L_E$, $b_!M_E$) with $a_!L=(C_E)_{\Qlb}$ and
$b_!M=(N_E)_{\Qlb}$. Since $\overline{\mathbf Q}_{\ell,X}=\varinjlim_{E'}E'_X$ (filtered over finite
$E'\supset E$) is flat over $E_X$, adjunction gives

$$
R\operatorname{Hom}_{\Qlb}((C_E)_{\Qlb},(N_E)_{\Qlb})=R\operatorname{Hom}_E\bigl(C_E,\varinjlim_{E'}(N_E)_{E'}\bigr),
$$

and [sk-lem-constructible-ext-continuity] identifies its $H^q$ with
$\varinjlim_{E'}\Ext^q_E(C_E,(N_E)_{E'})=\varinjlim_{E'}\Ext^q_{E'}((C_E)_{E'},(N_E)_{E'})$. Each term
vanishes for $q>c_a$ by the case of $E'$, so the colimit vanishes.
