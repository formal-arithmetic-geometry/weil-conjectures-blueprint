+++
kind  = "proof"
of    = "p-dl-a1-exact"
+++
*Step 1: the obstruction is a connecting map.* The short exact
sequence is a distinguished triangle $F_1\to F\to F_2\xrightarrow{+1}$
of Weil complexes on $U_0$. The derived direct image
[def-weil-derived-direct-image] is a triangulated functor and, with
its Weil structure and equivariant structure maps from
[lem-fix-weil-operations], gives a distinguished triangle of Weil
complexes $Rj_*F_1\to Rj_*F\to Rj_*F_2\xrightarrow{+1}$ on $C_0$.
Since $R^rj_*=0$ for $r<0$ and $R^0j_*=j_*$ is the ordinary direct
image ([def-wf-middle-extension]), its long exact sequence of
cohomology sheaves begins

$$
0\to j_*F_1\to j_*F\to j_*F_2\xrightarrow{\ \delta\ }R^1j_*F_1\to\cdots,
$$

and all maps, in particular $\delta$, are morphisms of Weil sheaves.
Hence the asserted sequence is exact if and only if $\delta=0$, and it
suffices to show that $\delta$ vanishes on every geometric stalk.

*Step 2: the open part.* By the unit/counit identities of
[prop-weil-open-closed-recollement-adjunctions],
$j^*Rj_*F_1\simeq F_1$, so $j^*R^1j_*F_1=\mathcal H^1(F_1)=0$ and
$\delta$ vanishes at every geometric point of $U$. Since $C_0$ is
locally of finite type over $k_0$, a sheaf on it vanishes once its stalks
at geometric points over closed points vanish; and every point of $Z_0$
is closed, because the non-closed points of the curve $C_0$ are generic
points of its irreducible components, which lie in the dense open $U_0$.
It remains to treat a geometric point $\bar s$ over a closed point
$s\in Z_0$. There
$\delta_{\bar s}:(j_*F_2)_{\bar s}\to(R^1j_*F_1)_{\bar s}$ commutes
with the local geometric Frobenius $F_s$, since $\delta$ is a morphism
of Weil sheaves. Write $q_s=|\kappa(s)|$.

*Step 3: localisation at $s$.* The curve $C_0$ need not be separated,
quasi-compact or geometrically connected, so before applying boundary
semicontinuity we localise. Let $X'_0\subseteq C_0$ be a connected affine
open neighbourhood of $s$ (a connected component of an affine open
neighbourhood; $C_0$ is smooth, so its local rings are regular and its
connected affine opens are irreducible). Then $X'_0$ is a smooth,
separated, irreducible affine curve of finite type over $k_0$. Let
$k_1$ be the algebraic closure of $k_0$ in its function field, a finite
field; then $X'_0$ is geometrically connected over $k_1$, hence a curve
over $k_1$ in the sense of [d-real-setup]. The open
$U'_0:=U_0\cap X'_0$ is dense in $X'_0$, so its complement is a proper
closed subset of an irreducible curve, hence finite. The formation of
$j_*$ and $R^1j_*$ commutes with restriction to the open $X'_0$, so
$(j_*F_2)_{\bar s}$, $(j_*F_1^\vee)_{\bar s}$ and $(R^1j_*F_1)_{\bar s}$
are the corresponding stalks for $j':U'_0\hookrightarrow X'_0$ and the
restrictions of the sheaves. Viewed over $k_1$ (Frobenius $F^{[k_1:k_0]}$),
the local Frobenius $F_x$ and the cardinality $q_x=|\kappa(x)|$ at every
closed point $x$ are unchanged, so the punctual weight conditions below
mean the same over $k_0$ and over $k_1$. If a restricted sheaf has rank
$0$ the stalks in question vanish and there is nothing to prove.

*Step 4: the source has weights at most $w$.* $F_2$ is punctually
pure, hence punctually mixed of weights at most $w$. The boundary
semicontinuity [lem-wf-boundary-semicontinuity], applied over $k_1$ to
$j'$ and $F_2|_{U'_0}$ (Step 3) with $\beta=w$, shows that every eigenvalue $\alpha$ of $F_s$ on
$(j_*F_2)_{\bar s}$ satisfies $|\iota(\alpha)|^2\le q_s^{w}$.

*Step 5: the target has weights at least $w+2$.* The local boundary
duality [lem-a1-local-boundary-duality] for $F_1$ gives an
$F_s$-equivariant isomorphism

$$
(R^1j_*F_1)_{\bar s}^\vee\simeq(j_*F_1^\vee)_{\bar s}(1);
$$

in particular $(R^1j_*F_1)_{\bar s}$ is finite-dimensional, and on the
left $F_s$ acts contragrediently. The dual $F_1^\vee$ is lisse and
punctually $\iota$-pure of weight $-w$ by [lem-tw-dual-negation], so
[lem-wf-boundary-semicontinuity], applied over $k_1$ to $j'$ and
$F_1^\vee|_{U'_0}$ (Step 3) with $\beta=-w$, bounds the
eigenvalues of $F_s$ on $(j_*F_1^\vee)_{\bar s}$ by
$|\iota(\cdot)|^2\le q_s^{-w}$. On the twist by $(1)$ the local
Frobenius is multiplied by $q_s^{-1}$ ([lem-wf-tate-twist-frobenius]),
so the eigenvalues on $(j_*F_1^\vee)_{\bar s}(1)$ satisfy
$|\iota(\cdot)|^2\le q_s^{-w-2}$. The eigenvalues of the contragredient
action are the inverses $\gamma^{-1}$ of the eigenvalues $\gamma$ of
$F_s$ on $(R^1j_*F_1)_{\bar s}$ ([p-linear-spectra]). Hence
$|\iota(\gamma)|^{-2}\le q_s^{-w-2}$, that is,

$$
|\iota(\gamma)|^2\ \ge\ q_s^{\,w+2}
$$

for every eigenvalue $\gamma$ of $F_s$ on $(R^1j_*F_1)_{\bar s}$.

*Step 6: the weight gap.* Let $I\subseteq(R^1j_*F_1)_{\bar s}$ be the
image of $\delta_{\bar s}$. It is $F_s$-stable, a quotient of
$(j_*F_2)_{\bar s}$ and a subspace of $(R^1j_*F_1)_{\bar s}$. By
[lem-a1-spectrum-exact-sequence], applied to the two short exact
sequences of Frobenius modules exhibiting $I$ as a quotient and as a
subobject, every eigenvalue $\lambda$ of $F_s$ on $I$ satisfies both
$|\iota(\lambda)|^2\le q_s^{w}$ (Step 4) and
$|\iota(\lambda)|^2\ge q_s^{w+2}$ (Step 5). Since $q_s>1$ these are
incompatible, so $I$ has no eigenvalue; being a finite-dimensional
space over the algebraically closed field $\Qlb$, it is zero. Thus
$\delta_{\bar s}=0$ for every boundary point, $\delta=0$ by Step 2,
and the sequence is exact by Step 1.
