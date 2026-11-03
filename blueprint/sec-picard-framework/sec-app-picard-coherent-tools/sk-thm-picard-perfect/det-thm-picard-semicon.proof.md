+++
kind  = "proof"
of    = "det-thm-picard-semicon"
uses = ["det-thm-picard-coherence"]
+++
The standard semicontinuity theorem, run on the local model of
[det-thm-picard-coherence](a): near each point of $T$ there is a bounded
complex $K^\bullet$ of finite free modules such that
$H^q(g^*K^\bullet)\cong R^qf'_*\cF'$ for every base change $g$ into that
neighbourhood; for $g$ the inclusion of a point $t$ this gives
$\dim_{\kappa(t)}H^q(X_t,\cF_t)=\operatorname{rk}K^q-\rho_q(t)-\rho_{q-1}(t)$
with $\rho_j(t)$ the rank of $d^j\otimes\kappa(t)$. Each $\rho_j$ is
lower semicontinuous (non-vanishing of minors), which gives upper
semicontinuity; if the sum is locally constant both $\rho_j$ are, and
over a *reduced* base a map of finite free modules whose fibre rank is
locally constant has, locally and in suitable bases, the normal form
$\begin{pmatrix}I&0\\0&0\end{pmatrix}$ (all larger minors vanish at every
point, hence are nilpotent, hence zero). Thus
$\operatorname{im}d^{q-1}\subseteq\ker d^q$ are local direct summands of
$K^q$, and taking for $g$ the inclusion of an open on which the normal
forms hold, $R^qf_*\cF=\ker d^q/\operatorname{im}d^{q-1}$ is finite
locally free there.

The base-change maps are defined on Čech complexes: over an affine open
$\Spec A\ni t$ and for a finite affine cover of its preimage, the Čech
complex $\check C^\bullet$ computes $R^qf_*\cF$ there, and
$\check C^\bullet\otimes_A\kappa(t)$ is the Čech complex of the induced
cover of $X_t$, which computes $H^q(X_t,\cF_t)$; the map is
$1\otimes[z]\mapsto[z\otimes1]$. If $A$ is moreover Noetherian, the
Čech complex is perfect, i.e. receives a quasi-isomorphism from a
bounded complex of finite projective $A$-modules which stays a
quasi-isomorphism after every base change $A\to B$; this is where the
Noetherian hypothesis enters. If $A$ is also reduced and the fibre
dimension is constant on the generizations of $t$ (for instance locally
constant), the same normal-form argument over the reduced local ring
$A_{\mathfrak p_t}$, whose points are exactly these generizations, makes
the cycles and boundaries in degree $q$ split, so the formation of
$H^q$ commutes with $\otimes\kappa(t)$: this is Grauert's theorem, the
isomorphism claim. Reducedness
cannot be dropped: over $T=\Spec k[\varepsilon]/(\varepsilon^2)$ let
$\cL$ be a line bundle on $E\times_kT$, $E$ an elliptic curve, which
restricts to $\cO_E$ but is a nontrivial first-order deformation of it;
then $H^0(\cL)=\varepsilon H^0(E,\cO_E)\cong k$ is killed by
$\varepsilon$, so it is not flat over $T$, although $T$ is a point.
