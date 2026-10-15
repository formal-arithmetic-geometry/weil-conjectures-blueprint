+++
id = "sk-thm-dnc"
kind = "lemma"
title = "A section and its normal bundle"
order = 1816
uses = ["sk-def-purity-conv", "sk-lem-geometry", "sk-prop-a1-inv", "sk-prop-an", "sk-prop-cohsm"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone"]
tags = ["sketch"]
+++
Let $g:V\to S$ be smooth of pure relative dimension $d$ and let $s:S\to V$ be
a section of $g$ that is a closed immersion. Then $s$ is a regular immersion of
codimension $d$. Let $N_s$ be its normal bundle, with projection
$\pi:N_s\to S$ and zero section $z:S\to N_s$.

The *deformation to the normal bundle* is the open subscheme
$\operatorname{Def}_s(V)$ of the blowup of $V\times\mathbf A^1$ along
$s(S)\times\{0\}$ obtained by removing the strict transform of $V\times\{0\}$.
It comes with a smooth morphism $\widetilde g:\operatorname{Def}_s(V)\to\mathbf A^1_S$
and a section $\widetilde s:\mathbf A^1_S\to\operatorname{Def}_s(V)$ that is a
closed immersion. Over $t=1$ the pair $(\widetilde g,\widetilde s)$ restricts
to $(g,s)$, and over $t=0$ to $(\pi,z)$. In local terms: if $s(S)$ is cut out
by relative coordinates $x_1,\dots,x_d$, then $\operatorname{Def}_s(V)$ has
coordinates $u_1,\dots,u_d$ with $x_i=tu_i$, and at $t=0$ the $u_i$ become
linear coordinates on $N_s$.

**Lemma.** There is a canonical isomorphism in
$\Dctf(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
s^*\omega_g\xrightarrow{\ \sim\ }z^*\omega_\pi.
$$

It is obtained by restricting to $t=0$ the unique isomorphism
$\widetilde s^*\omega_{\widetilde g}\to a^*s^*\omega_g$ in
$\Dctf(\mathbf A^1_{S,\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$ that is the identity at
$t=1$, and inverting; here $a:\mathbf A^1_S\to S$ is the projection.

The fibres of $\widetilde s^*\omega_{\widetilde g}$ at $t=1$ and $t=0$ are the two
sides of the isomorphism. The proof uses coordinates to show that this
shifted rank-one sheaf is pulled back from $S$, étale locally on $S$. The
geometric fibres of $\mathbf A^1_S\to S$ are connected, so a comparison fixed at
$t=1$ is unique, and the local comparisons glue. Coordinates are needed for
the first step: in positive characteristic a locally constant sheaf on
$\mathbf A^1_S$ need not be pulled back from $S$, and here it is because the
deformation is locally a product. The construction commutes with base change
along any $S'\to S$: pullback preserves the local product model and the
normalization at $t=1$, so the uniqueness statement identifies the
pulled-back isomorphism with the one constructed over $S'$.
