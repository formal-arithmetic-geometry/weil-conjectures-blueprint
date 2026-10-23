+++
kind  = "proof"
of    = "lem-fd-character-integral"
uses = ["lem-wft-as-unit-trivialization", "lem-fd-character-orthogonality", "sk-def-sp-trace", "sk-prop-sp-trace-composition"]
+++
*The constant sheaf on the line.* The vector-bundle trace of
[thm-pur-vector-bundle-thom] for the trivial line bundle
$p:\mathbf A^1_\Omega\to\operatorname{Spec}\Omega$ is an isomorphism
$R\Gamma_c(\mathbf A^1_\Omega,\Lambda)\simeq\Lambda(-1)[-2]$. A translation
$\tau$ of $\mathbf A^1_\Omega$ is an automorphism over $\operatorname{Spec}\Omega$,
so it preserves the trace: the trace of the line is the smooth trace of $p$
([sk-def-sp-trace]), and by transitivity
([sk-prop-sp-trace-composition]) for $p=p\circ\tau$, with $\tau$ étale of
relative dimension $0$ and trace the identity, one has
$\operatorname{Tr}_p\circ Rp_!(\tau^*)=\operatorname{Tr}_p$; since the
cohomology is concentrated in the single degree $2$, $\tau$ acts on it as
the identity.

*A nontrivial character on the line.* Fix a nontrivial
$\Psi:\mathbf F_p\to\Lambda^\times$ and let
$\pi:\mathbf A^1_u\to\mathbf A^1_x$, $u\mapsto u^p-u$, be the covering of
[lem-fd-as-cover-affine-line] (over $\Omega$). It is finite étale, so
$R\pi_!=\pi_*$ is exact ([lem-fd-finite-pushforward-cohomology] (2)), and
$R\Gamma_c(\mathbf A^1_x,\pi_*\Lambda)\cong R\Gamma_c(\mathbf A^1_u,\Lambda)
\cong\Lambda(-1)[-2]$, equivariantly for the deck translations
$\sigma_b$, $b\in\mathbf F_p$. The decomposition
$\pi_*\Lambda=\bigoplus_\chi\mathcal L_\chi$ of [lem-fd-as-characters] is the
decomposition by the idempotents $e_\chi$ of the deck action, so
$R\Gamma_c(\mathbf A^1_x,\mathcal L_\chi)=e_\chi R\Gamma_c(\mathbf A^1_u,\Lambda)$.
The deck translations act trivially by the previous step, and on a trivial
representation $e_\chi$ acts by $\frac1p\sum_b\chi(-b)=0$ for $\chi\neq1$
(orthogonality). Hence $R\Gamma_c(\mathbf A^1_\Omega,\mathcal L_\Psi)=0$ for
the summand $\mathcal L_\Psi=e_\Psi\pi_*\Lambda$.

*All nonzero linear forms on the line.* Let $\lambda(x)=cx$ with
$c\in\Omega^\times$. Write $\psi(z)=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$
with $a\in k_0^\times$ ([lem-wft-as-comparison] (1)). By
[lem-wft-as-comparison] (2) for the function $x$, $\mathcal L_\psi$ is the
$\Psi$-summand of the $\mathbf F_p$-covering of $ax$, so
$\lambda^*\mathcal L_\psi$ is the $\Psi$-summand of the covering of $acx$,
which is $\mu^*\mathcal L_\Psi$ for the automorphism $\mu:x\mapsto acx$ of
$\mathbf A^1_\Omega$. Hence
$R\Gamma_c(\mathbf A^1_\Omega,\lambda^*\mathcal L_\psi)\cong
R\Gamma_c(\mathbf A^1_\Omega,\mathcal L_\Psi)=0$.

*Higher dimension.* For $\lambda\neq0$ choose linear coordinates
$(t,s)\in\mathbf A^1\times\mathbf A^{r-1}$ with $\lambda=t$; then
$\lambda^*\mathcal L_\psi=\mathcal L_{\psi,t}\boxtimes\Lambda$, and the
Künneth isomorphism of [lem-wft-kunneth-compatibilities] (1) over
$S=\operatorname{Spec}\Omega$ gives
$R\Gamma_c(\mathbf A^r,\lambda^*\mathcal L_\psi)\cong
R\Gamma_c(\mathbf A^1,\mathcal L_{\psi,t})\otimes R\Gamma_c(\mathbf A^{r-1},\Lambda)=0$.
For $\lambda=0$ the sheaf is $\Lambda$ (via [lem-wft-as-unit-trivialization]),
and $r$ applications of the Künneth isomorphism give
$\Lambda(-1)[-2]^{\otimes r}=\Lambda(-r)[-2r]$; by
[lem-wft-kunneth-compatibilities] (3) (or the compatibility of the
vector-bundle trace with direct sums in [thm-pur-vector-bundle-thom]) the
product of the $r$ traces of the line is the trace of $\mathbf A^r_\Omega$.

*Coefficients.* The computation is made with $\Lambda=E$; extension of
scalars to $\overline{\mathbf Q}_\ell$ commutes with $R\Gamma_c$ and with the
traces ([sk-prop-sfb-finite-extension-compatibility]), which gives the case
$\Lambda=\overline{\mathbf Q}_\ell$.
