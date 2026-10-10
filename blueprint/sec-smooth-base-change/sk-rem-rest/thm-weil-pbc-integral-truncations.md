+++
id = "thm-weil-pbc-integral-truncations"
kind = "theorem"
title = "Truncations of the integral category"
order = 1430
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

## Proof

Take the reduction tower and its local models. By
[prop-weil-pbc-levelwise-truncations] (whose Tor-compatibility condition (1)
holds here by the hypothesis of the statement), $\tau^{\le m}K_\bullet$ is an adic tower
which is uniformly bounded constructible and has compatible etale-origin
witnesses, so by the reconstruction lemma for uniform towers its derived
limit $\tau^{\le m}K$ is derived $I$-complete, has no cohomology outside the
model interval, and satisfies the reduction isomorphisms of (i) by the
finite-reduction reconstruction lemma; the same holds for
$\tau^{\ge m+1}K$. Hence both objects lie in $\Dbc(T_{\Proet},A)$ of
[def-weil-pbc-bounded-constructible-complete]. The cohomology formulas of
(ii) follow from (i) and the cohomology formulas of
[prop-weil-pbc-levelwise-truncations] (iii) at the reduction level, together
with the long exact cohomology sequence of the triangle of (iii) (the end
terms of the triangle are the two objects just constructed, with the
vanishing cohomology of (ii)); the functoriality and additivity are those of
the levelwise truncations and of the functor $\Rlim$. Since a truncation
triangle is characterized by the vanishing properties of its end terms, the
constructed truncations are the canonical truncations of the ambient
category. For (iii), the levelwise truncation triangles form a compatible
family under the normalization isomorphisms of
[prop-weil-pbc-levelwise-truncations] (i) (both the triangles and the
isomorphisms being canonical), hence a triangle in
$D(\operatorname{Tow}_A(T))$, whose image under the triangulated functor
$\Rlim$ is the displayed triangle; its functoriality is inherited from the
levelwise functoriality.
