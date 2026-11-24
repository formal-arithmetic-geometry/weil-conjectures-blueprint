+++
id = "prose-E-23"
kind = "hidden"
title = "Specialization of the trace class (2)"
order = 1690
+++
Neither properness of the legs $c_1,c_2$ nor smoothness of $F$ is
assumed. This matters, because we apply the proposition to the
deformation of a [correspondence](@definition-correspondence) to the normal cone. Its generic fibre is
the original [correspondence](@definition-correspondence), but its [fixed scheme](@definition-correspondence), which we describe in
Lemma [lemma-fixed-point-scheme-deformation] of
Section [sec-Contracting-correspondences], may be singular and nonreduced.

A [trace class](@definition-trace-class-local-terms) has two ingredients besides $u$: the [external duality](@lemma-external-duality-trace-morphism)
isomorphism, which turns $u$ into a section of
$\href{@theorem-existence-exceptional-inverse-image}{c^!}(K\boxtimes\href{@definition-verdier-dual-evaluation}{\mathbb DK})$, and the evaluation along the diagonal. In
the proof we compare both once and for all on $X\times_SX$, for the
universal kernel $K\boxtimes\href{@definition-verdier-dual-evaluation}{\mathbb DK}$, and then pull the comparison
back along $c$. After taking adjoints, each comparison reduces to the
pairing (E.12) that defines $\delta_K$.

We fix the maps. In the setting of
Proposition [proposition-specialization-trace-class], let
$P_X=K\boxtimes\href{@definition-verdier-dual-evaluation}{\mathbb DK}$ be the external product of
Lemma [lemma-external-duality-trace-morphism].  The comparison map for
external products is

$$
\Pi_{M,N}=\mu(\alpha_{p_1}\otimes\alpha_{p_2}):
\Psi_XM\boxtimes \Psi_XN\longrightarrow \Psi_{X\times_SX}(M\boxtimes N),
$$

and it is invertible by
Proposition [proposition-external-kunneth-formula-nearby-cycles].
Using it and the isomorphism $\delta_K=\delta_{X,K}$ of
Proposition [proposition-nearby-cycles-commute-verdier-duality],
we define the isomorphism

$$
\rho:\Psi_{X\times_SX}\href{@lemma-external-duality-trace-morphism}{P_X}\xrightarrow{\Pi_{K,\href{@definition-verdier-dual-evaluation}{\mathbb DK}}^{-1}}
K'\boxtimes \Psi_X\href{@definition-verdier-dual-evaluation}{\mathbb DK}\xrightarrow{1\boxtimes\delta_K}K'\boxtimes\href{@definition-verdier-dual-evaluation}{\mathbb DK'}.
$$

Write $\lambda_K:P_X\xrightarrow\sim
\cHom_A(p_2^*K,\href{@theorem-existence-exceptional-inverse-image}{p_1^!K})$ for the external duality isomorphism of
Lemma [lemma-external-duality-trace-morphism], and
$e_K:\href{@lemma-external-duality-trace-morphism}{P_X}\to R\Delta_*\href{@definition-verdier-dual-evaluation}{\omega_X}$ for the evaluation along the diagonal
(Definition [definition-trace-morphism]). Let

$$
\mathfrak h:\Psi_{X\times_SX}\cHom_A(p_2^*K,\href{@theorem-existence-exceptional-inverse-image}{p_1^!K})\longrightarrow
\cHom_A(p_{2s}^*K',\href{@theorem-existence-exceptional-inverse-image}{p_{1s}^!K'})
$$

be the comparison obtained from the tensor–Hom mate of
$\Psi(\operatorname{ev})\mu$ by precomposing with $\alpha_{p_2}$
and postcomposing with $\beta_{p_1}$. For the [correspondence](@definition-correspondence) $c$, let
$\lambda_{c,K}:\href{@theorem-existence-exceptional-inverse-image}{c^!}P_X\xrightarrow\sim\cHom_A(c_2^*K,\href{@theorem-existence-exceptional-inverse-image}{c_1^!K})$ be the
[external duality](@lemma-external-duality-trace-morphism) isomorphism on $C$, and define $\mathfrak h_c$ as
$\mathfrak h$, with $\alpha_{c_2}$ and $\beta_{c_1}$ in place of
$\alpha_{p_2}$ and $\beta_{p_1}$.
