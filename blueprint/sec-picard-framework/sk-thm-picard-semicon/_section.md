+++
id = "sk-thm-picard-semicon"
kind = "section"
title = "Semicontinuity and base change"
order = 669
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
+++
*Theorem (sketch).*

With $f$ and $\cF$ as above, for every $t\in T$ the function
$t\mapsto\dim_{\kappa(t)}H^q(X_t,\cF_t)$ is upper semicontinuous in
$t$, and there are canonical base-change maps
$R^qf_*\cF\otimes\kappa(t)\to H^q(X_t,\cF_t)$. If moreover $T$ is
*reduced* and this function is locally constant, then $R^qf_*\cF$ is
finite locally free (in particular flat) and the base-change maps in
degree $q$ are isomorphisms.

## Proof

The standard semicontinuity theorem: the coherent complex supplied
by [sk-thm-picard-coherence] is, locally on $T$, represented by a
bounded complex of finite free modules whose formation commutes with
base change, and the assertions follow from the flatness of the
family together with the base-change comparison; the last clause is
Grauert's theorem, which uses that a coherent module on a reduced base
with locally constant fibre dimension is locally free. Reducedness
cannot be dropped: over $T=\Spec k[\varepsilon]/(\varepsilon^2)$ let
$\cL$ be a line bundle on $E\times_kT$, $E$ an elliptic curve, which
restricts to $\cO_E$ but is a nontrivial first-order deformation of it;
then $H^0(\cL)=\varepsilon H^0(E,\cO_E)\cong k$ is killed by
$\varepsilon$, so it is not flat over $T$, although $T$ is a point.
