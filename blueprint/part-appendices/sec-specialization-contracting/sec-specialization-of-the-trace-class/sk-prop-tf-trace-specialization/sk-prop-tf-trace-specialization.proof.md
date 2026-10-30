+++
kind = "proof"
of = "sk-prop-tf-trace-specialization"
uses = ["sk-thm-sf-kunneth-verdier", "sk-prop-tf-nearby-external-kunneth", "sk-prop-tf-nearby-duality-foundation", "sk-lem-tf-nearby-mate-coherences"]
+++
Let $P_X=K\boxtimes\mathbb DK$ be the external product of
Lemma [sk-thm-sf-kunneth-verdier]. A trace class has two ingredients,
the external duality isomorphism identifying correspondences with
sections of $c^!(K\boxtimes \mathbb DK)$ and the evaluation along the
diagonal. We first prove the two identities
(E.19) below, which compare both with nearby
cycles on $X\times_SX$, and then we deduce the general case by pulling
back along $c$. The comparison map for external products is

$$
\Pi_{M,N}=\mu(\alpha_{p_1}\otimes\alpha_{p_2}):
\Psi_XM\boxtimes \Psi_XN\longrightarrow \Psi_{X\times_SX}(M\boxtimes N),
$$

and it is invertible by Proposition [sk-prop-tf-nearby-external-kunneth].
Using this map and the duality isomorphism $\delta_K=\delta_{X,K}$ for nearby
cycles of Proposition [sk-prop-tf-nearby-duality-foundation], we define the isomorphism

$$
\rho:\Psi_{X\times_SX}P_X\xrightarrow{\Pi_{K,\mathbb DK}^{-1}}
K'\boxtimes \Psi_X\mathbb DK\xrightarrow{1\boxtimes\delta_K}K'\boxtimes\mathbb DK'.
$$

Write $\lambda_K:P_X\xrightarrow\sim \cHom_A(p_2^*K,p_1^!K)$ for the external duality isomorphism of
Lemma [sk-thm-sf-kunneth-verdier], and
$e_K:P_X\to R\Delta_*\omega_X$ for the evaluation along the diagonal. Let

$$
\mathfrak h:\Psi_{X\times_SX}\cHom_A(p_2^*K,p_1^!K)\longrightarrow
\cHom_A(p_{2s}^*K',p_{1s}^!K')
$$

be the comparison obtained from the tensor–Hom mate of
$\Psi(\operatorname{ev})\mu$ by precomposing with $\alpha_{p_2}$
and postcomposing with $\beta_{p_1}$. We claim that

$$
\mathfrak h\,\Psi(\lambda_K)=\lambda_{K'}\rho,
\qquad
e_{K'}\rho=R\Delta_{s*}\theta_X\,\chi_\Delta\,\Psi(e_K).
\tag{E.19}
$$

For the first equality, we precompose with $\Pi_{K,\mathbb DK}$ and take
tensor–Hom adjoints. Both maps then have source

$$
(p_{1s}^*K'\otimes^{\mathbf L} p_{2s}^*\Psi_X\mathbb DK)\otimes^{\mathbf L} p_{2s}^*K'
$$

and target $p_{1s}^!K'$. The adjoint defining $\lambda_K$ is

$$
(p_1^*K\otimes^{\mathbf L} p_2^*\mathbb DK)\otimes^{\mathbf L} p_2^*K
\xrightarrow{1\otimes\widetilde{\operatorname{ev}}_K}
p_1^*K\otimes^{\mathbf L} p_2^*\omega_X
\xrightarrow{\sim}p_2^*\omega_X\otimes^{\mathbf L} p_1^*K
\xrightarrow{\kappa_K}p_1^!K,
$$

where $\widetilde{\operatorname{ev}}_K$ is
$\mathbb DK\otimes^{\mathbf L} K\xrightarrow{\sim}K\otimes^{\mathbf L} \mathbb DK \xrightarrow{\operatorname{ev}_K}\omega_X$; in both displays the arrows
marked $\sim$ are the symmetry isomorphisms of the tensor product.
All Koszul signs come from these symmetries. Since $\alpha$ is
monoidal, we can move the ordinary comparison maps past $\mu$, and
(E.10) computes what $\beta_{p_1}$ does to the
last arrow $\kappa_K$. What remains on the factors $K'$ and
$\Psi_X\mathbb DK$ is the composite
$\theta_X\Psi_X(\operatorname{ev}_K)\mu_X$, which is the pairing
(E.13), that is, evaluation
against $\delta_K$. The result is the adjoint of
$\lambda_{K'}(1\boxtimes\delta_K)$, and since $\Pi$ is invertible, the
first equality follows.

For the second equality, we again precompose with $\Pi_{K,\mathbb DK}$
and take adjoints for $\Delta_s^*\dashv R\Delta_{s*}$. Since $\alpha$
is monoidal and compatible with composition, the map
$\alpha_\Delta\Delta_s^*\Pi_{K,\mathbb DK}$ is
$\mu_X:K'\otimes^{\mathbf L} \Psi_X\mathbb DK\to \Psi_X(K\otimes^{\mathbf L} \mathbb DK)$, so both
adjoints are the pairing (E.13) defining $\delta_K$.
Since $\Delta$ is proper, the comparison map for direct image is
$\chi_\Delta$. This proves (E.19).

It remains to pull these identities back to $C$. For the correspondence $c$, let
$\lambda_{c,K}:c^!P_X\xrightarrow\sim\cHom_A(c_2^*K,c_1^!K)$ be the
external duality isomorphism on $C$, and define $\mathfrak h_c$ as
$\mathfrak h$, with $\alpha_{c_2}$ and $\beta_{c_1}$ in place of
$\alpha_{p_2}$ and $\beta_{p_1}$. Then

$$
\mathfrak h_c\Psi_C(\lambda_{c_\eta,K})
=\lambda_{c_s,K'}\,c_s^!\rho\,\beta_c(P_X).
\tag{E.20}
$$

Indeed, after taking tensor–Hom adjoints, we factor the ordinary
comparison map through $c_2=p_2c$ and the exceptional comparison map
through $c_1=p_1c$, and we apply (E.8) for
$f=c$. What remains is the first equality of
(E.19) pulled back by $c_s^!$.
If $k_u:A_{C_\eta}\to c_\eta^!P_X$ is the section corresponding to
$u$, then (E.20) and
$\mu(\sigma\otimes1)=1$ show that the section corresponding to $u_s$ is

$$
k_{u_s}=c_s^!\rho\,\beta_c\,\Psi_C(k_u)\,\sigma_C.
$$

The trace morphism is $t_{c,K}=\zeta\,c^!e_K$.
Using the second equality of (E.19),
then (E.11), and finally
(E.9) for $d$, we get

$$
t_{c_s,K'}c_s^!\rho\,\beta_c
=Ri_{s*}\theta_F\,\chi_i\,\Psi_C(t_{c_\eta,K}).
$$

We apply this to $k_{u_s}$ and take adjoints for
$i_s^*\dashv Ri_{s*}$. It remains to check the identity for the units

$$
\chi_i \Psi_C(\eta_{i_\eta})\sigma_C
=Ri_{s*}(\sigma_F)\eta_{i_s}.
$$

Its ordinary adjoint is the identity
$\sigma_F=\alpha_i i_s^*\sigma_C$ of
(E.7), followed by the ordinary
triangle identity. This proves the asserted equality of trace
classes.
