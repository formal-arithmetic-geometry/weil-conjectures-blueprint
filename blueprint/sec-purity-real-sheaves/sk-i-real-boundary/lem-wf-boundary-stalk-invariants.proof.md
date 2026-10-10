+++
kind  = "proof"
of    = "lem-wf-boundary-stalk-invariants"
+++
The strict-henselization stalk formula of
[prop-weil-pbc-strict-henselization-stalk-formula] is a statement about
torsion sheaves, and a lisse $\Qlb$-sheaf is in general not trivialized
by any finite etale cover (the unipotent Kummer extension on
$\mathbf G_m$ has infinite geometric monodromy), so the formula is
applied at the finite levels $\mathcal F_n$ of an $\mathcal O_E$-model
of $\mathcal F$, which are locally constant sheaves of finite
$\mathcal O_E/\mathfrak m_E^n$-modules. For each $n$ the stalk of
$j_*\mathcal F_n$ at the geometric point $\bar x$ is computed on the
punctured strict henselian trait
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{C_0,\bar x}\setminus\{x\}$,
the spectrum of a field with absolute Galois group the inertia group
$I_x=\operatorname{Gal}(\overline{\kappa(\eta_x)}/\kappa(\eta_x))$: the
sections of the locally constant sheaf $\mathcal F_n$ over it are the
invariants $M_n^{I_x}$ of the finite-level geometric generic stalk
$M_n$. The geometric stalk of the adic sheaf $j_*\mathcal F$ (in the
sense of [def-weil-pbc-geometric-stalks], formed levelwise) is
$(\varprojlim_nM_n^{I_x})\otimes_{\mathcal O_E}E$. Invariants commute
with inverse limits, so $\varprojlim_nM_n^{I_x}=M^{I_x}$ for the lattice
$M=\varprojlim_nM_n$ of $\mathcal F_{\bar\eta}$, and
$M^{I_x}=M\cap\mathcal F_{\bar\eta}^{I_x}$ is saturated in $M$, so
$M^{I_x}\otimes_{\mathcal O_E}E=\mathcal F_{\bar\eta}^{I_x}$; the tower
$(M_n^{I_x})_n$ need not be adic, but only its limit enters. This is the
displayed identification.

For the Frobenius equivariance, let $D_x=\operatorname{Gal}(\overline K_x/K_x)$
be the decomposition group of [d-real-boundary], $K_x$ the fraction
field of the henselization $\mathcal O^{\mathrm h}_{C_0,x}$, so that
$D_x/I_x=\operatorname{Gal}(\overline{\kappa(x)}/\kappa(x))$ and
$\overline K_x^{I_x}$ is the fraction field of
$\mathcal O^{\mathrm{sh}}_{C_0,\bar x}$. The identification above is
the restriction of sections of $\mathcal F$ from the punctured strict
henselian trait to its geometric generic point, which is natural in
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
