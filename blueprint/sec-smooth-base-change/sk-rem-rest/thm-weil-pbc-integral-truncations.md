+++
id = "thm-weil-pbc-integral-truncations"
kind = "theorem"
title = "Truncations of the integral category"
order = 1468
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-complete", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-intrinsic-completion", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-reconstruction-uniform-tower", "prop-weil-pbc-levelwise-truncations"]
+++
Let the adic datum be $A=\mathcal O_E$, $I=(\varpi)$, $P_n=A_{E,n}$, and let
$T$ be noetherian of finite dimension with the torsion orders invertible.
For $K\in\Dbc(T_{\Proet},A)$ [def-weil-pbc-bounded-constructible-complete],
with its canonical reduction tower $K_\bullet$ (uniformly bounded
constructible with compatible etale-origin witnesses). *Assume that the
Tor-compatibility condition (1) of [prop-weil-pbc-levelwise-truncations]
holds for $K_\bullet$ above every level* (this is the case, for instance,
when the cohomology sheaves of the local models are flat over $A_T$), and
define
$$
 \tau^{\le m}K:=\Rlim\tau^{\le m}K_\bullet,\qquad
 \tau^{\ge m+1}K:=\Rlim\tau^{\ge m+1}K_\bullet,
$$
the derived limits of the towers of
[prop-weil-pbc-levelwise-truncations]. Then
$\tau^{\le m}K,\tau^{\ge m+1}K\in\Dbc(T_{\Proet},A)$, and:

1. *reductions:* there are canonical isomorphisms
   $$
    (\tau^{\le m}K)\otimes^L_AP_n\xrightarrow{\sim}\tau^{\le m}K_n,
    \qquad
    (\tau^{\ge m+1}K)\otimes^L_AP_n\xrightarrow{\sim}\tau^{\ge m+1}K_n,
   $$
   compatible with the normalization maps;
2. *cohomology and universality:*
   $$
    \mathcal H^i(\tau^{\le m}K)=\mathcal H^i(K)\ (i\le m),\qquad
    \mathcal H^i(\tau^{\le m}K)=0\ (i>m),
   $$
   $$
    \mathcal H^i(\tau^{\ge m+1}K)=\mathcal H^i(K)\ (i\ge m+1),\qquad
    \mathcal H^i(\tau^{\ge m+1}K)=0\ (i\le m),
   $$
   so that $\tau^{\le m},\tau^{\ge m+1}$ are additive endofunctors of
   $\Dbc(T_{\Proet},A)$ characterized by the vanishing of these cohomology
   sheaves; they coincide with the canonical truncations of the ambient
   derived category;
3. *truncation triangles:* the levelwise triangles assemble into
   distinguished triangles
   $$
    \tau^{\le m}K\longrightarrow K
    \longrightarrow\tau^{\ge m+1}K
    \longrightarrow\tau^{\le m}K[1],
   $$
   functorial in $K$.
