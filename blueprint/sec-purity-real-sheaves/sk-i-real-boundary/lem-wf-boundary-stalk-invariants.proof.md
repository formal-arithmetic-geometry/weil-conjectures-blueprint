+++
kind  = "proof"
of    = "lem-wf-boundary-stalk-invariants"
uses = ["d-real-boundary", "def-pe-derived-complete", "def-weil-derived-pullback-tensor-hom", "def-wf-fundamental-representation", "p-real-integral", "prop-weil-pbc-strict-henselization-stalk-formula", "sk-lem-integral-models", "sk-prop-integral-criterion", "sk-prop-pe-milnor", "sk-prop-scalar-six", "sk-prop-sfb-finite-extension-compatibility", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-pe-direct-image-comparison", "sk-thm-sf-ctf-stability"]
+++
Write $\mathcal F$ also for the underlying lisse $\overline{\mathbf Q}_{\ell,U}$-module
and $V=\mathcal F_{\bar\eta}$. The strict-henselization stalk formula of
[prop-weil-pbc-strict-henselization-stalk-formula] is a statement about
torsion sheaves, and a lisse $\Qlb$-sheaf is in general not trivialized
by any finite etale cover (the unipotent Kummer extension on
$\mathbf G_m$ has infinite geometric monodromy), so the computation passes
through an integral model, used here only as a consequence of the condensed theory.
By [p-real-integral], after enlarging $E$, there are a $\pi_1(U)$-stable
$\cO_E$-lattice $M\subset V$ and a lisse $\cO_{E,U}$-module $\mathcal F_0$ with stalk
$M$, with $\mathcal F\simeq\mathcal F_0\otimes_{\cO_{E,U}}\overline{\mathbf Q}_{\ell,U}$,
whose reductions $\mathcal F_n=\mathcal F_0/\mathfrak m_E^n\mathcal F_0$ are locally
constant sheaves of finite $\cO_E/\mathfrak m_E^n$-modules with stalks
$M_n=M/\mathfrak m_E^nM$.

*Finite levels.* By [sk-thm-sf-ctf-stability], $Rj_*\mathcal F_0\in\Dbc(C,\cO_E)$, and by
the coefficient comparisons of [sk-prop-scalar-six]
$Rj_*\mathcal F\simeq Rj_*\mathcal F_0\otimes_{\cO_E}\Qlb$ and
$Rj_*\mathcal F_0\otimes^{\mathbf L}_{\cO_E}\cO_E/\mathfrak m_E^n\simeq Rj_*\mathcal F_n$.
At finite level $Rj_*\mathcal F_n$ is the étale direct image
([sk-thm-pe-direct-image-comparison]), so its stalk at the geometric point $\bar x$ is
computed by [prop-weil-pbc-strict-henselization-stalk-formula] on the
punctured strict henselian trait
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{C_0,\bar x}\setminus\{x\}$,
the spectrum of a field with absolute Galois group the inertia group
$I_x=\operatorname{Gal}(\overline{\kappa(\eta_x)}/\kappa(\eta_x))$: the
sections of the locally constant sheaf $\mathcal F_n$ over it are the
invariants $M_n^{I_x}$, and $(Rj_*\mathcal F_n)_{\bar x}$ has no cohomology in negative
degrees.

*Limit.* The stalk $\bar x^*Rj_*\mathcal F_0$ lies in $\Dbc(\bar x,\cO_E)$, since pullback
preserves $\Dbc(-,\cO_E)$ ([sk-lem-integral-models] (3)), hence is derived complete
([def-pe-derived-complete], [sk-prop-integral-criterion]). Its reductions modulo $\pi_E^n$ are the stalks
$(Rj_*\mathcal F_n)_{\bar x}$, because $\bar x^*$ commutes with
$-\otimes^{\mathbf L}_{\cO_E}\cO_E/\pi_E^n$ ([def-weil-derived-pullback-tensor-hom]) and by
the comparison of the finite levels. So
$\bar x^*Rj_*\mathcal F_0\simeq R\varprojlim_n(Rj_*\mathcal F_n)_{\bar x}$, and the global
sections over $\bar x$, a right adjoint, commute with this derived limit. The Milnor
sequence ([sk-prop-pe-milnor]) in degree $0$, whose $\varprojlim^1$-term involves only
degree $-1$ and vanishes, gives
$(j_*\mathcal F_0)_{\bar x}=\varprojlim_nM_n^{I_x}=M^{I_x}$, since invariants commute
with inverse limits; the tower $(M_n^{I_x})_n$ need not be adic, but only its limit
enters.

*Scalars.* As $\overline{\mathbf Q}_{\ell,C}$ is flat over $\cO_{E,C}$ ([sk-prop-sfb-qlbar-colimit-x], [sk-prop-sfb-finite-extension-compatibility]) and stalks are exact,
$(j_*\mathcal F)_{\bar x}=\mathcal H^0(Rj_*\mathcal F)_{\bar x}
=M^{I_x}\otimes_{\cO_E}\Qlb$. Invariants commute with inverting $\ell$ (an invariant
vector of $M[1/\ell]$ has an invariant multiple in $M$) and with the base change
$E\to\Qlb$ ($\Qlb$ is free as an $E$-vector space), so
$M^{I_x}\otimes_{\cO_E}\Qlb=(M\otimes_{\cO_E}\Qlb)^{I_x}=\mathcal F_{\bar\eta}^{I_x}$.
This is the displayed identification.

For the Frobenius equivariance, let $D_x=\operatorname{Gal}(\overline K_x/K_x)$
be the decomposition group of [d-real-boundary], $K_x$ the fraction
field of the henselization $\mathcal O^{\mathrm h}_{C_0,x}$, so that
$D_x/I_x=\operatorname{Gal}(\overline{\kappa(x)}/\kappa(x))$ and
$\overline K_x^{I_x}$ is the fraction field of
$\mathcal O^{\mathrm{sh}}_{C_0,\bar x}$. The identification above is
the restriction of sections of $\mathcal F_n$ from the punctured strict
henselian trait to its geometric generic point, compatibly in $n$ and then
passed through the limit and the extension of scalars; it is natural in
automorphisms of $\mathcal O^{\mathrm{sh}}_{C_0,\bar x}$ over
$\mathcal O^{\mathrm h}_{C_0,x}$. An element $\sigma\in D_x$ induces
such an automorphism, acting on $(j_*\mathcal F)_{\bar x}$ through its
image in $\operatorname{Gal}(\overline{\kappa(x)}/\kappa(x))$ and on
$\mathcal F_{\bar\eta}$ through the Weil fundamental representation of
[def-wf-fundamental-representation]; naturality says that these actions
correspond on $\mathcal F_{\bar\eta}^{I_x}$. Taking $\sigma$ a lift of
the geometric Frobenius of $\kappa(x)$ (in the local Weil group, so that
the action on $\mathcal F_{\bar\eta}$ is defined for a Weil sheaf) gives
the stated equivariance; two lifts differ by an element of $I_x$, which
acts trivially on the invariants.
