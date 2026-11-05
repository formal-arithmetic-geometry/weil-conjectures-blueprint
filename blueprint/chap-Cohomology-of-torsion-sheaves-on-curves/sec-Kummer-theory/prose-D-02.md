+++
id = "prose-D-02"
kind = "hidden"
title = "Kummer theory (1)"
order = 1575
+++
Let $C$ be a smooth curve over an algebraically closed field $k$, and
let $\nu_C^*\mathbf G_m$ be the
pullback of the multiplicative group $\mathbf G_m$ of $C_{\acute{e}t}$ to $C_{\mathrm{pro}\acute{e}t}$. For $n$ invertible
in $k$, the Kummer sequence $0\to\mu_n\to\mathbf G_m\xrightarrow{n}\mathbf G_m\to0$
reduces the cohomology of $\mu_n$ to that of $\nu_C^*\mathbf G_m$, so
we compute the latter first.
In degree one, $H^1(C,\mathbf G_m)$ is the Picard group, as in the
Zariski topology, while the groups $H^q(C,\mathbf G_m)$ vanish for $q\ge2$
(Lemma [lemma-cohomology-multiplicative-group]). In particular the
Brauer group of $C$ is zero. This matches, over $\mathbf C$, the topology of a Riemann surface, whose integral cohomology
vanishes above degree two, and whose $H^2$ is accounted for by the degree of
line bundles. In algebraic geometry the vanishing comes from Tsen's
theorem, which says that forms of low degree over the function field
$k(C)$ have nontrivial zeros. Over a finite field Tsen's theorem fails:
by class field theory the function field of a curve has nonzero Brauer
group. This is one reason why we work over an algebraically closed field.
With the lemma and the Jacobian, the Kummer sequence then computes the
cohomology of $\mu_n$ on a proper curve
(Proposition [proposition-smooth-proper-curves-torsion-prime]).
