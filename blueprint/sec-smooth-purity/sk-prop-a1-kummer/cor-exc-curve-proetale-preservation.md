+++
id = "cor-exc-curve-proetale-preservation"
kind = "theorem"
title = "Closed curve support for the ambient pro-etale right adjoint"
order = 2008
tags = ["latex:corollary"]
uses = ["def-sc-curves", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-complexes", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "prop-exc-closed-site-comparison", "prop-weil-pbc-site-comparison-finite-level", "thm-exc-curve-closed-preservation"]
+++
Let $i:Z\hookrightarrow T$ be the
closed immersion of a
finite reduced set of points in a smooth connected curve
over a finite field or its algebraic closure. Put $A=A_{E,n}$,
with $\ell$ invertible. For a
bounded constructible
etale complex $K$, the ambient pro-etale right adjoint satisfies

$$
Ri^{\times}\nu_T^*K\simeq\nu_Z^*Ri^!_{\mathrm{et}}K.
$$

Here $\nu^*$ is the
site comparison.
The value is bounded constructible; a cohomological interval
$[a,b]$ gives $[a,b+2]$. If $K$ has
finite Tor amplitude, its
image has the same bound $[a,b+2]$ on Tor amplitude, uniformly in
$n$, and commutes with finite coefficient reduction.

## Proof

The ambient comparison is [prop-exc-closed-site-comparison].
Its etale value has the asserted bounds by
[thm-exc-curve-closed-preservation]. The exact $\nu_Z^*$
of [prop-weil-pbc-site-comparison-finite-level] preserves
cohomological intervals. Pull back the finite constructible
stratification: finite locally constant modules remain finite locally
constant, giving the constructibility of
[def-weil-finite-torsion-constructibility].
An exact inverse-image tensor functor also takes a bounded flat
representative to a bounded flat representative, so the same Tor
bound applies to arbitrary module sheaves on the pro-etale target.
It commutes with the derived constant tensor of
[def-weil-derived-tensor], by pulling back flat resolutions.
Thus the etale coefficient comparisons in
[thm-exc-curve-closed-preservation] give the claimed
pro-etale comparisons as well.
