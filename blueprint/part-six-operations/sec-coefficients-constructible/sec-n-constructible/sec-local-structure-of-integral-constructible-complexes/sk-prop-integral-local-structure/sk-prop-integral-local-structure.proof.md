+++
kind = "proof"
of = "sk-prop-integral-local-structure"
uses = ["sk-lem-integral-finite-levels", "sk-lem-integral-scalar-towers", "sk-prop-sf-open-closed-triangle", "sk-prop-pe-milnor", "sk-lem-pe-derived-nakayama"]
+++
We first trivialize each $K_n$ locally, separately for each $n$, and then make
the trivializations compatible. Choose a finite stratification on which all cohomology sheaves of
$K_1$ are locally constant, and refine it by connected components.
There are finitely many of these, since the strata are Noetherian. Restriction
to an open subscheme preserves limits, and so does restriction to a
closed subscheme on the pro-étale site
(Proposition [sk-prop-sf-open-closed-triangle]), and both are exact and commute with the
two-term cones defining the reductions. Hence for every stratum $S$ the restriction $K|_S$ is again derived
complete with constructible first reduction. Fix a connected stratum $S$.

*Local trivializations at each finite level.*
By Lemma [sk-lem-integral-finite-levels] each $K_n|_S$ is classical, of
finite Tor amplitude, with locally constant finite cohomology. We work on
$S_{\acute{e}t}$ and fix a geometric point $\bar s$. The stalk complex at
$\bar s$ has a minimal finite free model $M_n$ in the common interval
$[a,b]$. A finite free model of the stalk at any geometric point
$\bar t$ extends to an étale neighbourhood of $\bar t$. Indeed, the stalk
isomorphism is a section at $\bar t$ of the zeroth cohomology sheaf of
the derived internal Hom out of the constant finite free complex, and we may extend
this section and lift it locally to a derived map. The cone has bounded
locally constant finite cohomology and zero stalk at $\bar t$, so
its finitely many cohomology sheaves vanish after shrinking the
neighbourhood. Thus $K_n$ is locally isomorphic to a constant perfect
complex. For each isomorphism class of such complexes, the union of the
neighbourhoods on which $K_n$ has that model is open, and different
classes give disjoint open sets, since different classes cannot occur
at the same point. As $S$ is connected, $K_n|_S$ is everywhere locally
isomorphic to the constant complex $(M_n)_S$; compare [Stacks, Tag 09BI](https://stacks.math.columbia.edu/tag/09BI).

On stalks at $\bar s$, the reduction maps $K_{n+1}\to K_n$ induce maps
$M_{n+1}\to M_n$ inducing isomorphisms
$M_{n+1}\otimes^{\mathbf L}_{\mathcal O_E/\pi_E^{n+1}}\mathcal O_E/\pi_E^n\simeq M_n$, because
the étale stalk functor is exact and symmetric monoidal.
By Lemma [sk-lem-integral-scalar-towers](1) there is a bounded finite free
complex $P^\bullet$ with $P^\bullet/\pi_E^n\simeq M_n$. Back on
$S_{\mathrm{pro}\acute{e}t}$, we get for each $n$ local isomorphisms
$(P^\bullet/\pi_E^n)_S\simeq K_n|_S$ in
$D(S_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$. They are chosen separately for
each $n$, and we now make them compatible.

*Compatible isomorphisms on a weakly contractible cover.*
Choose an affine weakly contractible cover $W\to S$. For each $n$, the
local isomorphism becomes an isomorphism
$(P^\bullet/\pi_E^n)_W\simeq K_n|_W$ on all of $W$, since by weak
contractibility a covering by trivializing charts splits. Consider the
tower of complexes

$$
\cHom_{(\mathcal O_E/\pi_E^n)_W}\bigl((P^\bullet/\pi_E^n)_W,K_n|_W\bigr)
\in D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n),
$$

with transition maps induced by the reduction maps $K_{n+1}\to K_n$, and
the tower of groups
$\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)}\bigl((P^\bullet/\pi_E^n)_W,K_n|_W\bigr)$
obtained by applying $H^0R\Gamma(W,-)$. Since $P^\bullet$ is finite
free, the first tower is the tower of reductions of
$(\mathcal O_{E,W}\otimes_{\mathcal O_E}(P^\bullet)^\vee)\otimes^{\mathbf L}_{\mathcal O_{E,W}}K|_W$.

These Hom groups can be infinite, so the Mittag–Leffler condition
has to come from a uniform bound. Let $Q^\bullet=(P^\bullet)^\vee\otimes_{\mathcal O_E}P^\bullet$
and choose $e$ such that $\pi_E^e$ kills the torsion of
$H^1(Q^\bullet)$. Let $N\ge m\ge n+e$ and choose one isomorphism
$(P^\bullet/\pi_E^N)_W\simeq K_N|_W$. Its reductions to levels $m$ and
$n$ identify the three internal Hom complexes at levels $N\to m\to n$
with the constant complexes
$Q^\bullet/\pi_E^N\to Q^\bullet/\pi_E^m\to Q^\bullet/\pi_E^n$. Their
zeroth cohomology sheaves are therefore the constant sheaves on the groups
$H^0(Q^\bullet/\pi_E^N)\to H^0(Q^\bullet/\pi_E^m)\to H^0(Q^\bullet/\pi_E^n)$,
and by Lemma [sk-lem-integral-scalar-towers](2) the images from levels $N$
and $m$ at level $n$ agree, as subsheaves. Since $W$ is weakly
contractible, taking sections over $W$ is exact. Hence it commutes with
taking cohomology and images, and the images in the Hom group at level $n$
from levels $N$ and $m$ coincide as well. Since $e$ does not depend on
$n$, $m$ or $N$, this is the Mittag–Leffler condition: for every $n$ the
images at level $n$ are constant from level $n+e$ on.

*The integral isomorphism.*
Each Hom group contains an isomorphism, and the reduction of an
isomorphism to level $1$ is again an isomorphism. The stable image at
level $1$ is the image from level $1+e$, so it contains an invertible
class, and by the Mittag–Leffler property it lifts to a compatible
family $(\varphi_n)_n$ in the inverse limit of the Hom groups. The
Milnor sequence gives a surjection

$$
\begin{aligned}
&H^0R\varprojlim_n R\Gamma\bigl(W,\cHom_{(\mathcal O_E/\pi_E^n)_W}
((P^\bullet/\pi_E^n)_W,K_n|_W)\bigr)\\
&\qquad\longrightarrow
\varprojlim_n\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)}
\bigl((P^\bullet/\pi_E^n)_W,K_n|_W\bigr),
\end{aligned}
$$

whose source is
$\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E)}(\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet,K|_W)$.
This holds because derived sections commute with inverse limits, $K|_W$ is complete, and
tensoring with the finite free dual of $P^\bullet$ commutes with
inverse limits. Consequently $(\varphi_n)$ lifts to a morphism
$\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet\to K|_W$ whose first reduction is an isomorphism.
Both objects are complete. For the source this follows termwise from
$\mathcal O_{E,W}=\varprojlim(\mathcal O_E/\pi_E^n)_W$, since the
transition maps are epimorphisms and so this limit agrees with the
derived limit by Proposition [sk-prop-pe-milnor]. By derived Nakayama (Lemma [sk-lem-pe-derived-nakayama]),
the morphism is an isomorphism.
