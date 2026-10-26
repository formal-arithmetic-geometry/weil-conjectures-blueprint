+++
kind = "proof"
of = "sk-lem-int-integral-heart"
uses = ["sk-prop-integral-criterion", "sk-prop-integral-local-structure", "sk-def-sfb-constructible"]
+++
The conditions of [sk-prop-integral-criterion] are stable under cones and shifts: derived
completeness, and bounded constructibility of the reduction modulo $\pi_E$. Hence
$\Dbc(X,\mathcal O_E)$ is a triangulated subcategory.

The local structure is the key point, and it is condition (3) of [sk-prop-integral-criterion]
(the implication from (2) to (3) is [sk-prop-integral-local-structure]): *for
$K\in\Dbc(X,\mathcal O_E)$ there is a finite stratification of $X$ such that on each stratum
$S$, pro-étale locally, $K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ for a bounded
complex $P^\bullet$ of finite free $\mathcal O_E$-modules.* Since the map from the constant sheaf
$\underline{\mathcal O_E}$ to $\mathcal O_{E,S}$ is flat (\stacks{099L}), on these local models

$$
H^q(K)|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}H^q(P^\bullet),
$$

with $H^q(P^\bullet)$ a finitely generated $\mathcal O_E$-module, possibly with torsion. The strata
are quasi-compact, so finitely many charts suffice and $K$ is bounded. A finitely generated
$\mathcal O_E$-module has a free resolution of length one, so $H^q(K)$ again satisfies condition
(3) of [sk-prop-integral-criterion] on the same strata, and hence lies in
$\Dbc(X,\mathcal O_E)$. This gives (2), and since every truncation of $K$ is a finite extension
of shifts of the $H^q(K)$, it also gives stability under truncation.

Stability under truncation gives (1) for the heart: the kernel and cokernel of a map of
constructible sheaves are cohomology sheaves of its cone, and an extension of two constructible
sheaves is the middle term of a triangle with constructible ends. Essential smallness holds
because a constructible sheaf is determined up to isomorphism by a finite stratification, local
presentations, descent data and finitely many extension classes, and these form a set. For (3),
the length one free resolution of the local model gives the derived dual and the evaluation and
coevaluation maps locally, and the Tor amplitudes can be read off from it.

For the local model $\mathcal O_E/\pi_E$ the amplitudes in (3) can be seen directly. The
resolution $0\to\mathcal O_E\xrightarrow{\pi_E}\mathcal O_E\to\mathcal O_E/\pi_E\to0$ shows that
$M\otimes^{\mathbf L}\mathcal O_E/\pi_E$ is the cone of $\pi_E$ on $M$, which lives in degrees
$[-1,0]$ for a module $M$. Applying $R\operatorname{Hom}(-,\mathcal O_E)$ to the same resolution
gives the dual $\mathcal O_E/\pi_E[-1]$, whose Tor amplitude is $[0,1]$.
