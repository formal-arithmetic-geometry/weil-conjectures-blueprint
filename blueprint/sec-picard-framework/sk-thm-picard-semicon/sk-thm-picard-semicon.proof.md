+++
kind  = "proof"
of    = "sk-thm-picard-semicon"
+++
The standard semicontinuity theorem: the perfect complex $Rf_*\mathcal F$
supplied by [sk-thm-picard-coherence](a) is, locally on $T$, represented by a
bounded complex of finite free modules whose formation commutes with
base change, and the assertions follow from the flatness of the
family together with the base-change comparison; the last clause is
Grauert's theorem, which needs no Noetherian hypothesis: in the local
model $K^\bullet$ one has
$\dim_{\kappa(t)}H^q(X_t,\cF_t)=\operatorname{rk}K^q-\rho_q(t)-\rho_{q-1}(t)$
with $\rho_j(t)$ the rank of $d^j\otimes\kappa(t)$; each $\rho_j$ is
lower semicontinuous, so if their sum is locally constant both are, and
over a *reduced* base a map of finite free modules whose fibre
rank is locally constant has, locally and in suitable bases, the normal
form $\begin{pmatrix}I&0\\0&0\end{pmatrix}$ (all larger minors vanish
at every point, hence are nilpotent, hence zero). Thus
$\operatorname{im}d^{q-1}\subseteq\ker d^q$ are local direct summands
of $K^q$, so $R^qf_*\cF=\ker d^q/\operatorname{im}d^{q-1}$ is finite
locally free and its formation commutes with $\otimes\kappa(t)$, which
is the isomorphism claim. Reducedness
cannot be dropped: over $T=\Spec k[\varepsilon]/(\varepsilon^2)$ let
$\cL$ be a line bundle on $E\times_kT$, $E$ an elliptic curve, which
restricts to $\cO_E$ but is a nontrivial first-order deformation of it;
then $H^0(\cL)=\varepsilon H^0(E,\cO_E)\cong k$ is killed by
$\varepsilon$, so it is not flat over $T$, although $T$ is a point.
