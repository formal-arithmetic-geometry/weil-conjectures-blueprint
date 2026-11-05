+++
kind = "proof"
of = "lemma-nearby-cycles-universal-kernel"
order = 1690
+++
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
$\mathbb DK\otimes^{\mathbf L} K\xrightarrow{\sim}K\otimes^{\mathbf L} \mathbb DK
\xrightarrow{\operatorname{ev}_K}\omega_X$. In both displays the arrows
marked $\sim$ are the symmetry isomorphisms of the tensor product, and
all Koszul signs come from these symmetries. Since $\alpha$ is
monoidal, we can move the ordinary comparison maps past $\mu$. By
(E.10) we know what $\beta_{p_1}$ does
to the last arrow $\kappa_K$. What remains on the factors $K'$ and
$\Psi_X\mathbb DK$ is the composite
$\theta_X\Psi_X(\operatorname{ev}_K)\mu_X$. This is the pairing
(E.12), that is, evaluation
against $\delta_K$. The result is the adjoint of
$\lambda_{K'}(1\boxtimes\delta_K)$. Since $\Pi$ is invertible, the
first equality follows.

For the second equality, we again precompose with $\Pi_{K,\mathbb DK}$
and take adjoints for $\Delta_s^*\dashv R\Delta_{s*}$. Since $\alpha$
is monoidal and compatible with composition, the map
$\alpha_\Delta\Delta_s^*\Pi_{K,\mathbb DK}$ is
$\mu_X:K'\otimes^{\mathbf L} \Psi_X\mathbb DK\to \Psi_X(K\otimes^{\mathbf L} \mathbb DK)$. Hence both
adjoints are the pairing (E.12) defining $\delta_K$.
Since $\Delta$ is proper, the comparison map for direct image is
$\chi_\Delta$.
