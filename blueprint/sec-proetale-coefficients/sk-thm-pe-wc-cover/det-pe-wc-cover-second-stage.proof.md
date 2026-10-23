+++
kind = "proof"
of = "det-pe-wc-cover-second-stage"
+++
*Preliminaries.* The ring $L$ is the filtered colimit of the products $C^{\mathcal Q}$ over
the finite partitions $\mathcal Q$ of $S$ into clopen subsets, so $\operatorname{Spec}L$ is
the limit of the spaces $\mathcal Q\times\operatorname{Spec}C$, i.e.
$S\times\operatorname{Spec}C$. The graph $\Gamma$ is closed as $S$ is Hausdorff. The
connected components of $S\times\operatorname{Spec}C$ are the sets $\{s\}\times K$ with $K$ a
component of $\operatorname{Spec}C$, since $S$ is totally disconnected, and $\Gamma$ is a
union of them; so $Z$ is closed. Clopen subsets of $\operatorname{Spec}L$ correspond to
idempotents of $L$, and localizing at an idempotent $e$ is the quotient by $1-e$. Hence
$L\to D$ is surjective, $\operatorname{Spec}D\to\operatorname{Spec}L$ is a closed embedding,
and its image is the intersection of the clopen neighbourhoods of $\Gamma$, which is
$\Gamma$ because $\Gamma$ is a closed union of components of a compact space.

*1.* Each $L_{e_U}$ is a principal localization of $L$, and $C\to C^{\mathcal Q}$ is a finite
product of copies of the identity, so $C\to L\to D$ is a composite of filtered colimits of
local isomorphisms, i.e. ind-Zariski [def-weil-pbc-ind-etale-algebra]; it is ind-étale and
flat by [lem-weil-pbc-ind-etale-stability], and ind-Zariski maps identify local rings.
Surjectivity on spectra follows from 2: for $x\in\operatorname{Spec}C$ choose $s$ with
$f(s)=\pi(x)$.

*2.* By the preliminaries, $\operatorname{Spec}D$ is homeomorphic to the subspace $\Gamma$ of
$S\times\operatorname{Spec}C$, which is the fibre product $S\times_P\operatorname{Spec}C$ of
topological spaces.

*3.* The product $S\times\operatorname{Spec}C$ of a profinite space and a w-local space is
w-local, with closed points $S\times(\operatorname{Spec}C)^c$, and a closed subspace of a
w-local space is w-local with closed points the closed points lying in it. So
$\operatorname{Spec}D\cong\Gamma$ is w-local, with closed points the $(s,x)\in\Gamma$ with
$x$ closed. The fibre of $\Gamma\to S$ over $s$ is $\pi^{-1}(f(s))$, a connected component
of $\operatorname{Spec}C$; hence the connected components of $\Gamma$ are exactly these
fibres, and $\pi_0(\Gamma)\to S$ is a continuous bijection from a compact space to a
Hausdorff space, hence a homeomorphism. By [det-pe-wlocal-components],
$(\operatorname{Spec}D)^c\to\pi_0(\operatorname{Spec}D)$ is a homeomorphism.

*4.* By 3, a maximal ideal of $D$ lies over a maximal ideal $\mathfrak m$ of $C$, and by 1 its
local ring is $C_{\mathfrak m}$, which is strictly henselian; so $D$ is w-strictly local. By
3, $\pi_0(\operatorname{Spec}D)\cong S$ is extremally disconnected.
