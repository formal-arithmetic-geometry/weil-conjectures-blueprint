+++
kind = "proof"
of = "proposition-local-structure-integral-constructible-complexes"
order = 244
+++
We first trivialize each $K_n$ locally, separately for each $n$, and then make
the trivializations compatible. To begin, choose a finite stratification on which all cohomology sheaves of
$K_1$ are locally constant, and refine it by connected components;
there are finitely many of these, since the strata are Noetherian.

For every stratum $S$ the restriction $K|_S$ is again derived complete with
constructible first reduction. Indeed, restriction to an open subscheme
preserves limits, and so does restriction to a closed subscheme on the
pro-étale site
(Proposition [proposition-extension-zero-restriction-closed-subscheme]).
Moreover, both restrictions are exact and commute with the two-term cones defining the
reductions. From now on we fix a connected stratum $S$.

*Local trivializations at each finite level.*
By Lemma [lemma-bounds-finite-reductions], each $K_n|_S$ is classical and
of finite Tor amplitude, with locally constant finite cohomology, so we
may work on $S_{\acute{e}t}$. Fix a geometric point $\bar s$. Then the stalk complex at
$\bar s$ has a minimal finite free model $M_n$ in the common interval
$[a,b]$. By Lemma [lemma-local-constancy-finite-level] the complex
$K_n|_S$ is étale locally isomorphic to the constant complex $(M_n)_S$.

On stalks at $\bar s$, the reduction maps $K_{n+1}\to K_n$ induce maps
$M_{n+1}\to M_n$ inducing isomorphisms
$M_{n+1}\otimes^{\mathbf L}_{\mathcal O_E/\pi_E^{n+1}}\mathcal O_E/\pi_E^n\simeq M_n$, because
the étale stalk functor is exact and symmetric monoidal.
By Lemma [lemma-perfect-complexes-over-oe] there is a bounded finite free
complex $P^\bullet$ with $P^\bullet/\pi_E^n\simeq M_n$. Back on
$S_{\mathrm{pro}\acute{e}t}$, we get for each $n$ local isomorphisms
$(P^\bullet/\pi_E^n)_S\simeq K_n|_S$ in
$D(S_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$, chosen separately for
each $n$.

*The integral isomorphism.*
Choose an affine weakly contractible cover $W\to S$. For each $n$, the
local isomorphism becomes an isomorphism
$(P^\bullet/\pi_E^n)_W\simeq K_n|_W$ on all of $W$, since by weak
contractibility a covering by trivializing charts splits. Moreover, the restriction
$K|_W$ is derived complete, and its reductions are the $K_n|_W$. By
Lemma [lemma-integral-model-weakly-contractible] we conclude that
$K|_W\simeq\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet$.
