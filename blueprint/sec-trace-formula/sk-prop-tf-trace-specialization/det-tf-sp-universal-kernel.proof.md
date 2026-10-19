+++
kind = "proof"
of = "det-tf-sp-universal-kernel"
uses = ["thm-trf-verdier-duality"]
+++
*First equality.* Precompose with $\Pi_{K,\mathbb DK}$ and take tensor–Hom adjoints.
Both maps have source $(p_{1s}^*K'\dt p_{2s}^*S_X\mathbb DK)\dt p_{2s}^*K'$ and target
$p_{1s}^!K'$. The adjoint defining $\lambda_K$ is

$$
 (p_1^*K\dt p_2^*\mathbb DK)\dt p_2^*K
 \xrightarrow{1\otimes\widetilde{\operatorname{ev}}_K}
 p_1^*K\dt p_2^*\omega_X
 \xrightarrow{\mathrm{sym}}p_2^*\omega_X\dt p_1^*K
 \xrightarrow{\kappa_K}p_1^!K,
$$

where $\widetilde{\operatorname{ev}}_K$ is
$\mathbb DK\dt K\xrightarrow{\mathrm{sym}}K\dt\mathbb DK\xrightarrow{\operatorname{ev}_K}\omega_X$
and $\kappa_K:p_2^*\omega_X\dt p_1^*K\to p_1^!K$ is the normalized external-duality map;
the symmetries carry all Koszul signs. Monoidality of $\alpha$ moves the ordinary
comparisons past $\mu$, and the identity

$$
 \beta_{p_1}S(\kappa_M)\mu(\alpha_{p_2}\otimes\alpha_{p_1})
   =\kappa_{S_XM}(p_{2s}^*\theta_X\otimes1)
$$

handles the last arrow. The remaining adjacent pair is evaluated by
$\theta_XS_X(\operatorname{ev}_K)\mu_X$, which is evaluation against $\delta_K$. The result
is the adjoint of $\lambda_{K'}(1\boxtimes\delta_K)$. Since $\Pi$ is invertible, the first
equality follows.

*Second equality.* Precompose again with $\Pi_{K,\mathbb DK}$ and take
$\Delta_s^*\dashv R\Delta_{s*}$-adjoints. By monoidality of $\alpha$ and the composition
law $\alpha_{gf}=\alpha_f(g_\eta^*)f_s^*\alpha_g$, applied to $p_i\Delta=\mathrm{id}$, the
map $\alpha_\Delta\Delta_s^*\Pi_{K,\mathbb DK}$ is
$\mu_X:K'\dt S_X\mathbb DK\to S_X(K\dt\mathbb DK)$. Both adjoints are therefore the
normalized pairing $\theta_XS_X(\operatorname{ev}_K)\mu_X$ defining $\delta_K$, followed on
the left by $\delta_K$ and evaluation. Since $\Delta$ is proper, the direct-image comparison
for $\Delta$ is $\chi_\Delta$, which gives the second equality.
