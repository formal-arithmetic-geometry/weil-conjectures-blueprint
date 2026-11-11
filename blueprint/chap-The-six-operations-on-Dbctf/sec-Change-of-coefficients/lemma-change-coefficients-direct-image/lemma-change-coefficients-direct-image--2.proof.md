+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--2"
order = 636005
uses = ["lemma-acyclic-resolutions--1", "definition-sp-scalar-extension--2"]
+++
*Maps $\mathcal O_E\to A$ with $A$ finite.* Since $\mathcal O_E$ is a
discrete valuation ring, $A$ has a finite free $\mathcal O_E$-resolution of
length at most one. Its condensed version is again exact. Indeed, a
continuous map from a profinite set to the finite quotient $A$ is constant
on the pieces of a finite clopen partition, and hence lifts to a continuous
map to the free module. The pullback of this resolution to $X$ is a finite free resolution of $A_X$ over
$\mathcal O_{E,X}$. Consequently, tensoring with $A_X$ is computed by finite
sums and a cone, and these commute with the exact functor $Rf_*$.

*Source:* the proof of Lemma [lemma-change-coefficients-direct-image].
