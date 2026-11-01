+++
kind  = "proof"
of    = "lem-fd-first-formula"
uses = ["lem-fd-character-integral", "lem-wft-as-unit-trivialization", "sk-prop-sf-open-closed-triangle", "det-thm-sfb-shriek-base-change", "thm-pur-vector-bundle-thom"]
+++
All sheaves are $E$-sheaves: $\mu_p\subset E$, since the nontrivial
character $\Psi$ takes values in $E^\times$ and its image is $\mu_p$ (the
characteristic $p$ comes from [def-fd-kernel]), so the exponential sheaves and
the kernel are lisse $E$-sheaves of rank one; the formulas with
$\overline{\mathbf Q}_\ell$-coefficients follow by the extension of scalars
$\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}-$, which is exact and commutes with
the operations used ([det-prop-sfb-finite-extension-compatibility]).

*The constant sheaf.* For a geometric point
$\bar\xi:\operatorname{Spec}\Omega\to V^\vee$, [lem-fd-stalk-formula] identifies
the stalk of $\operatorname{FT}_\psi(\underline{E})$ with
$R\Gamma_c(\mathbf A^1_\Omega,\lambda^*\mathcal L_\psi)[1]$ for the linear
form $\lambda(x)=x\xi$. By [lem-fd-character-integral] this vanishes for
$\xi\neq0$. So the restriction of $\operatorname{FT}_\psi(\underline E)$ to
the open complement of the origin $i_0:\{0\}\hookrightarrow V^\vee$ has zero
stalks, hence is zero, and the localization triangle of
[sk-prop-sf-open-closed-triangle] gives
$\operatorname{FT}_\psi(\underline E)\cong i_{0*}i_0^*\operatorname{FT}_\psi(\underline E)$.
By compact-support base change along $i_0$ ([det-thm-sfb-shriek-base-change]),
$i_0^*\operatorname{FT}_\psi(\underline E)\cong
R\Gamma_c(\mathbf A^1,\mathcal L_{\psi,0})[1]$, and the unit trivialization
$\mathcal L_{\psi,0}\cong\underline E$ ([lem-wft-as-unit-trivialization]) and
the trace of the line ([thm-pur-vector-bundle-thom], the case $\lambda=0$ of
[lem-fd-character-integral]) identify this with $E(-1)[-2][1]=E(-1)[-1]$. The
trace is defined over the ground field, so the twist $(-1)$ is the Tate twist
as a Weil structure. Hence $\operatorname{FT}_\psi(\underline E)\cong
\delta_0(-1)[-1]$.

*The skyscraper.* The support of $p_1^*\delta_0$ is $\{0\}\times V^\vee$, on
which $p_2$ restricts to the canonical isomorphism onto $V^\vee$; the kernel
restricted to the support is $\mathcal L_{\psi,0}$ (the pairing vanishes
there), which is $\underline E$ by the unit trivialization. The
compact-support direct image along $p_2$ of the constant sheaf on the support
is therefore $\underline E$ on $V^\vee$, and the shift gives $\underline E[1]$.
