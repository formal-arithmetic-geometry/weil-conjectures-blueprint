+++
id = "lem-wf-boundary-stalk-invariants"
kind = "lemma"
title = "Boundary stalk as inertia invariants"
order = 2830
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
action.

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
This is the displayed identification; the Frobenius structures agree
because the Weil structures descend through the trait.
