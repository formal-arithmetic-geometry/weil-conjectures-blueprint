+++
kind = "proof"
of = "sk-prop-tf-trace-specialization"
uses = ["sk-thm-sf-kunneth-verdier", "sk-prop-tf-nearby-external-kunneth", "sk-prop-tf-nearby-duality-foundation", "sk-lem-tf-nearby-mate-coherences"]
+++
Let $P_X=K\boxtimes\mathbb DK$ be the external product of
Lemma [sk-thm-sf-kunneth-verdier], and $P_X'=K'\boxtimes\mathbb DK'$ its
analogue on the special fibre. The two identities
(1) below, which compare the external-duality
isomorphism and the diagonal evaluation with nearby cycles on
$X\times_SX$, carry the content of the proof; the passage to $C$ and to
the trace class is formal. The external product comparison is

$$
 \Pi_{M,N}=\mu(\alpha_{p_1}\otimes\alpha_{p_2}):
 S_XM\boxtimes S_XN\longrightarrow S_{X\times_SX}(M\boxtimes N),
$$

and it is invertible by Proposition [sk-prop-tf-nearby-external-kunneth].
Using it and the nearby duality isomorphism $\delta_K=\delta_{X,K}$ of
Proposition [sk-prop-tf-nearby-duality-foundation], define the isomorphism
in $D^b_c((X_s\times_kX_s)_{\mathrm{\acute et}},A)$

$$
 \rho:S_{X\times_SX}P_X\xrightarrow{\Pi_{K,\mathbb DK}^{-1}}
 K'\boxtimes S_X\mathbb DK\xrightarrow{1\boxtimes\delta_K}P_X'.
$$

Write $\lambda_K:P_X\xrightarrow{\sim}
\cHom_A(p_2^*K,p_1^!K)$ for the external-duality isomorphism of
Lemma [sk-thm-sf-kunneth-verdier] and
$e_K:P_X\to R\Delta_*\omega_X$ for the diagonal evaluation. Let

$$
 \mathfrak h:S_{X\times_SX}\cHom_A(p_2^*K,p_1^!K)\longrightarrow
 \cHom_A(p_{2s}^*K',p_{1s}^!K')
$$

be the comparison obtained from the tensor–Hom mate of
$S(\operatorname{ev})\mu$ by precomposing with $\alpha_{p_2}$
and postcomposing with $\beta_{p_1}$. We claim

$$
 \mathfrak h\,S(\lambda_K)=\lambda_{K'}\rho,
 \qquad
 e_{K'}\rho=R\Delta_{s*}\theta_X\,\chi_\Delta\,S(e_K).
 \tag{1}
$$

For the first equality precompose with $\Pi_{K,\mathbb DK}$ and take
tensor–Hom adjoints. Both maps have source

$$
 (p_{1s}^*K'\dt p_{2s}^*S_X\mathbb DK)\dt p_{2s}^*K'
$$

and target $p_{1s}^!K'$. The adjoint defining $\lambda_K$ is

$$
 (p_1^*K\dt p_2^*\mathbb DK)\dt p_2^*K
 \xrightarrow{1\otimes\widetilde{\operatorname{ev}}_K}
 p_1^*K\dt p_2^*\omega_X
 \xrightarrow{\mathrm{sym}}p_2^*\omega_X\dt p_1^*K
 \xrightarrow{\kappa_K}p_1^!K,
$$

where $\widetilde{\operatorname{ev}}_K$ is
$\mathbb DK\dt K\xrightarrow{\mathrm{sym}}K\dt \mathbb DK
\xrightarrow{\operatorname{ev}_K}\omega_X$;
these symmetries carry all Koszul signs. Monoidality of $\alpha$
moves the ordinary comparisons past $\mu$, and the identity
$\beta_{p_1}S(\kappa_M)\mu(\alpha_{p_2}\otimes\alpha_{p_1})=\kappa_{S_XM}(p_{2s}^*\theta_X\otimes1)$
of [sk-lem-tf-nearby-mate-coherences] handles the last arrow.
The remaining adjacent pair is evaluated by
$\theta_XS_X(\operatorname{ev}_K)\mu_X$, that is, by evaluation
against $\delta_K$. The result is the adjoint of
$\lambda_{K'}(1\boxtimes\delta_K)$, and invertibility of $\Pi$
gives the first equality.

For the second equality, precompose again with $\Pi_{K,\mathbb DK}$ and take
$\Delta_s^*\dashv R\Delta_{s*}$-adjoints. By monoidality and
composition of $\alpha$,
$\alpha_\Delta\Delta_s^*\Pi_{K,\mathbb DK}$ is
$\mu_X:K'\dt S_X\mathbb DK\to S_X(K\dt \mathbb DK)$, so both adjoints
are the normalized pairing defining $\delta_K$.
Since $\Delta$ is proper, the direct-image comparison is
$\chi_\Delta$. This proves (1).

It remains to pull these identities back to $C$. For the correspondence $c$, let
$\lambda_{c,K}:c^!P_X\xrightarrow{\sim}\cHom_A(c_2^*K,c_1^!K)$ be the
external-duality isomorphism on $C$, and define $\mathfrak h_c$ as
$\mathfrak h$, with $\alpha_{c_2}$ and $\beta_{c_1}$ in place of
$\alpha_{p_2}$ and $\beta_{p_1}$. Then

$$
 \mathfrak h_cS_C(\lambda_{c_\eta,K})
   =\lambda_{c_s,K'}\,c_s^!\rho\,\beta_c(P_X).
 \tag{2}
$$

Indeed, after taking tensor–Hom adjoints, factor the ordinary
comparison through $c_2=p_2c$ and the exceptional comparison through
$c_1=p_1c$, and apply the projection-formula identity
$\beta_fS_V(t_{f_\eta})\mu_V(1\otimes\alpha_f)=f_s^!\mu_W\,t_{f_s}(\beta_f\otimes1)$ of
[sk-lem-tf-nearby-mate-coherences] for $f=c$.
What remains is the first equality of
(1) pulled back by $c_s^!$.
If $k_u:A_{C_\eta}\to c_\eta^!P_X$ is the section corresponding to
$u$, then (2) and
$\mu(\sigma\otimes1)=1$ show that the section corresponding to $u_s$ is

$$
 k_{u_s}=c_s^!\rho\,\beta_c\,S_C(k_u)\,\sigma_C.
$$

The trace morphism is $t_{c,K}=B\,c^!e_K$, where
$B:c^!R\Delta_*\xrightarrow{\sim} Rr_*d^!$ is exceptional proper base change.
The second equality of (1),
then the fixed-square identity
$Rr_{s*}\beta_d\,\chi_r\,S_C(B_\eta)=B_s\,c_s^!(\chi_\Delta)\,\beta_c(R\Delta_{\eta*})$,
and finally the composition law
$\theta_F=d_s^!\theta_X\,\beta_d(\omega_{X_\eta})$ for $d$, both from
[sk-lem-tf-nearby-mate-coherences], give

$$
 t_{c_s,K'}c_s^!\rho\,\beta_c
   =Rr_{s*}\theta_F\,\chi_r\,S_C(t_{c_\eta,K}).
$$

Apply this to $k_{u_s}$ and take
$r_s^*\dashv Rr_{s*}$-adjoints. It remains to check the unit identity

$$
 \chi_r S_C(\eta_{r_\eta})\sigma_C
      =Rr_{s*}(\sigma_F)\eta_{r_s}.
$$

Its ordinary adjoint is the identity
$\sigma_F=\alpha_r r_s^*\sigma_C$ of the unit composition law,
followed by the ordinary
triangle identity. This gives the asserted equality of trace
classes. The only proper maps used are the closed immersions
$\Delta$ and $r$, so $F$ may be singular and nonreduced. For the
deformation to the normal cone, $F$ is the fixed scheme of the
deformed correspondence; Lemma [sk-lem-tf-contracting-fixed-geometry]
relates it to the original fixed scheme.
