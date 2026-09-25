+++
id = "lem-wf-boundary-stalk-invariants"
kind = "lemma"
title = "Boundary stalk as inertia invariants"
order = 2875
uses = ["d-real-boundary", "def-weil-pbc-geometric-stalks", "def-wf-fundamental-representation", "def-wf-middle-extension", "prop-weil-pbc-strict-henselization-stalk-formula"]
+++
Let $j:U_0\hookrightarrow C_0$ be a dense open immersion of smooth
curves over $k_0$, let $\mathcal F$ be lisse on $U_0$, and let
$x\in C_0\setminus U_0$ be a closed boundary point with local residue
field $\kappa(x)$ and inertia group $I_x$ of [d-real-boundary] inside the local
fundamental group of the
fundamental representation.
Then the boundary stalk of the
middle extension is

$$
(j_*\mathcal F)_{\bar x}\simeq\mathcal F_{\bar\eta}^{I_x},
$$

where $\mathcal F_{\bar\eta}$ is the
geometric generic stalk of
$\mathcal F$ at $x$ and the invariants are formed for the inertia
action. The identification is equivariant for Frobenius: the geometric
Frobenius of $\kappa(x)$ acting on the stalk of the Weil sheaf
$j_*\mathcal F$ at $\bar x$ corresponds to the action of a residue
Frobenius lift on $\mathcal F_{\bar\eta}^{I_x}$ of [d-real-boundary]
(which is independent of the lift).

## Proof

The stalk of $j_*\mathcal F$ at the geometric point $\bar x$ is
computed on the punctured strict henselian trait
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{C_0,\bar x}\setminus\{x\}$
by the strict-henselization stalk formula of
[prop-weil-pbc-strict-henselization-stalk-formula]: it is the
first fringe of the lisse sheaf restricted to the trait, i.e. the
invariants of the geometric generic stalk
$\mathcal F_{\bar\eta}$ (the geometric generic stalk in the
sense of [def-weil-pbc-geometric-stalks]) under the inertia group
$I_x=\operatorname{Gal}(\overline{\kappa(\eta_x)}/\kappa(\eta_x))$.
This is the displayed identification.

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
