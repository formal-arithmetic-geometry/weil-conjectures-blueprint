+++
kind = "proof"
of = "det-lem-int-integral-heart-local-model"
+++
(1) By [sk-lem-integral-models](1),(2), restriction of scalars along the flat
map $\underline{\mathcal O_E}\to\mathcal O_{E,X}$ identifies
$\Dbc(X,\mathcal O_E)$ with the category $\Dc(X,\mathcal O_E)$ of Stacks, Tags
099I, 099L. For our Noetherian schemes, Stacks, Tag 09C7 gives the claimed
stratification and local models; since $\mathcal O_E$ is already complete,
the completed coefficient ring of Stacks, Tag 09C4 is $\mathcal O_E$ itself.
(The mechanism: $K/\pi_E$ is a classical constructible complex, hence on a
stratum locally a perfect complex of $\mathcal O_E/\pi_E$-modules, which may
be represented by a bounded complex of finite free modules; on a weakly
contractible cover, where cohomology vanishes in positive degrees, this
complex and its successive deformations to $\mathcal O_E/\pi_E^n$ lift
compatibly to finite free complexes over $\mathcal O_E/\pi_E^n$, and their
derived limit is $K$ by derived completeness.)

(2) *Completeness.* The pro-étale site has enough weakly contractible affines
(Stacks, Tag 0990); on such a site cohomology sheaves of derived complete
complexes are derived complete (Stacks, Tag 099Q(5)). *Local form.* Since
$\underline{\mathcal O_E}\to\mathcal O_{E,X}$ is flat, on a local chart of (1)
we have $H^q(K)=H^q(M^\bullet)\otimes_{\mathcal O_E}\mathcal O_{E,S}$, the
completion of the finitely generated $\mathcal O_E$-module $H^q(M^\bullet)$.
*Constructibility of the reduction.* A finitely generated $\mathcal O_E$-module
$N$ has a free resolution $0\to\mathcal O_E^a\to\mathcal O_E^b\to N\to0$, in
degrees $-1,0$. Hence $H^q(K)\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E$ has
cohomology only in degrees $-1$ and $0$, and on the strata of (1) these
cohomology sheaves are locally the constant sheaves attached to the finite
modules $\ker(\pi_E|N)$ and $N/\pi_E N$, i.e. locally constant with finite
stalks. Such sheaves come from constructible sheaves on the étale site
(Stacks, Tags 099Y, 09AK). So $H^q(K)$ is derived complete with bounded
constructible reduction, i.e. $H^q(K)\in\Dbc(X,\mathcal O_E)$.

(3) $K$ is bounded, so each truncation is obtained from finitely many
$H^q(K)[-q]$ by successive extensions (triangles
$\tau_{\le q-1}\to\tau_{\le q}\to H^q[-q]$). Since $\Dbc(X,\mathcal O_E)$ is
closed under shifts and extensions (both conditions of
[sk-def-sfb-constructible] are), the truncations lie in it.
