+++
id = "compatible-strict-henselization-core-data"
kind = "lemma"
title = "Compatible strict henselization core data without final residue square"
lean = ["AlgebraicGeometry.Etale.exists_compatibleStrictHenselizationCoreData"]
order = 1620
+++
Let $g:T\to S$ be a morphism of schemes, let $k,k'$ be separably closed fields and $\Omega$ an algebraically closed
field. Let $\sigma:\operatorname{Spec}k\to S$, $\tau:\operatorname{Spec}k'\to T$ and
$\iota:\operatorname{Spec}k'\to\operatorname{Spec}k$ satisfy $\sigma\circ\iota=g\circ\tau$. Assume that $\sigma$
factors as $\operatorname{Spec}k\to\operatorname{Spec}\kappa(s_0)\to S$ for a point $s_0\in S$ with
$\kappa(s_0)\to k$ integral, and that $\tau$ factors likewise through $\operatorname{Spec}\kappa(t_0)$ for a point
$t_0\in T$ with $\kappa(t_0)\to k'$ integral. Let $\nu:\operatorname{Spec}\Omega\to\operatorname{Spec}k'$ and
consider the geometric points $\bar s=\sigma\iota\nu$ of $S$ and $\bar t=\tau\nu$ of $T$, with strict localizations
$\pi_{\bar s}:S_{(\bar s)}\to S$ and $\pi_{\bar t}:T_{(\bar t)}\to T$.

Then there exist henselian local rings $A$ and $B$ with separably closed residue fields $\kappa_A$ and $\kappa_B$,
a local homomorphism $\varphi:A\to B$, isomorphisms $e_A:\operatorname{Spec}A\xrightarrow{\sim}S_{(\bar s)}$ and
$e_B:\operatorname{Spec}B\xrightarrow{\sim}T_{(\bar t)}$, and morphisms
$\rho_A:\operatorname{Spec}k\to\operatorname{Spec}\kappa_A$ and $\rho_B:\operatorname{Spec}k'\to\operatorname{Spec}\kappa_B$
such that

- **(a)** $\rho_A$ and $\rho_B$ are universal homeomorphisms;
- **(b)** $\pi_{\bar s}\circ e_A\circ\operatorname{Spec}\varphi=g\circ\pi_{\bar t}\circ e_B$;
- **(c)** $\pi_{\bar s}\circ e_A\circ\operatorname{Spec}(A\to\kappa_A)\circ\rho_A=\sigma$ and
  $\pi_{\bar t}\circ e_B\circ\operatorname{Spec}(B\to\kappa_B)\circ\rho_B=\tau$.

The compatibility of $\rho_A,\rho_B$ with $\iota$ and the residue map of $\varphi$ is not asserted.
