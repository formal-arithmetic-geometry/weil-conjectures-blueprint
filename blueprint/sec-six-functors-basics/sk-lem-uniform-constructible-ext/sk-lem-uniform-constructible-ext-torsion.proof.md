+++
kind = "proof"
of = "det-uniform-constructible-ext-torsion"
+++
Put $N=b_!(M_0/\pi_E^n)$. It is a torsion sheaf pulled back from $X_{\mathrm{ét}}$: the lisse torsion
sheaf $M_0/\pi_E^n$ descends to $T_{\mathrm{ét}}$ (Stacks, Tag 099Y), and extension by zero and closed
direct image commute with the pullback from the étale site (Stacks, Tags 09AF, 09A6).

(1) $j^*N$ is again pulled back from the étale site, and by Stacks, Tag 09A6 the pro-étale $Rj_*j^*N$ is
the pullback of the étale $Rj_*$ of the corresponding étale sheaf. By definition of
$\operatorname{cd}_\ell(j)$ ([sk-def-cd]), $R^qj_*$ vanishes on classical $\ell$-power torsion sheaves
for $q>\operatorname{cd}_\ell(j)$, so $Rj_*j^*N\in\D^{[0,\operatorname{cd}_\ell(j)]}$ with classical
cohomology sheaves. By part (1) of [sk-lem-formal-closed-support],

$$
R\underline\Gamma_ZN=i^*\fib(N\to Rj_*j^*N).
$$

The fiber of a map from a sheaf in degree $0$ to an object of $\D^{[0,c]}$ lies in $\D^{[0,c+1]}$ (long
exact sequence), and $i^*$ is exact and preserves the classical (étale-pulled-back) sheaves. This proves
(1); the cohomology sheaves need not be constructible.

(2) Put $G=(L_0^\vee/\pi_E^n)\otimes u^*R\underline\Gamma_ZN$. Since $L_0^\vee/\pi_E^n$ is locally free
over $\mathcal O_E/\pi_E^n$, tensoring is exact, so by (1) $G\in\D^{[0,\operatorname{cd}_\ell(j)+1]}(S)$,
with cohomology sheaves $\mathcal H^v(G)$ that are classical $\ell$-power torsion sheaves. The
hypercohomology spectral sequence

$$
E_2^{p,v}=H^p(S,\mathcal H^v(G))\Longrightarrow H^{p+v}R\Gamma(S,G)
$$

converges since $G$ is bounded. By definition of $\operatorname{cd}_\ell(S)$, $E_2^{p,v}=0$ for
$p>\operatorname{cd}_\ell(S)$, and $E_2^{p,v}=0$ unless $0\leq v\leq\operatorname{cd}_\ell(j)+1$. Hence
the abutment vanishes in degrees $>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+1$.
