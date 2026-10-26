+++
id = "compatible-strict-henselization-residue-square"
kind = "lemma"
title = "Residue maps commute for compatible strict henselizations"
lean = ["AlgebraicGeometry.Etale.compatibleStrictHenselization_residue_square"]
order = 1600
uses = ["compatible-strict-henselization-core-data"]
+++
Let $g:T\to S$, the separably closed fields $k,k'$, the algebraically closed field $\Omega$, and
$\sigma,\tau,\iota,\nu$ with $\sigma\circ\iota=g\circ\tau$ be as in [compatible-strict-henselization-core-data],
with geometric points $\bar s=\sigma\iota\nu$ and $\bar t=\tau\nu$ (no integrality hypothesis is needed). Let $A$
and $B$ be henselian local rings with separably closed residue fields $\kappa_A,\kappa_B$, with isomorphisms
$e_A:\operatorname{Spec}A\xrightarrow{\sim}S_{(\bar s)}$ and $e_B:\operatorname{Spec}B\xrightarrow{\sim}T_{(\bar t)}$, and
let $\rho_A:\operatorname{Spec}k\to\operatorname{Spec}\kappa_A$ and $\rho_B:\operatorname{Spec}k'\to\operatorname{Spec}\kappa_B$
satisfy
$\pi_{\bar s}\circ e_A\circ\operatorname{Spec}(A\to\kappa_A)\circ\rho_A=\sigma$ and
$\pi_{\bar t}\circ e_B\circ\operatorname{Spec}(B\to\kappa_B)\circ\rho_B=\tau$.
Then there exists a local homomorphism $\varphi:A\to B$ such that
$\pi_{\bar s}\circ e_A\circ\operatorname{Spec}\varphi=g\circ\pi_{\bar t}\circ e_B$ and the induced residue map
$\bar\varphi:\kappa_A\to\kappa_B$ satisfies

$$
\operatorname{Spec}(\bar\varphi)\circ\rho_B=\rho_A\circ\iota .
$$

This asserts the existence of one compatible $\varphi$, not the compatibility of every such map.
