+++
id = "lem-trf-local-term-locality"
kind = "lemma"
title = "Locality and zero-stalk vanishing of the local term"
order = 2495
uses = ["d-curve-pieces", "def-trf-frobenius-coefficient-morphism", "def-trf-graph-correspondence", "def-trf-iterated-weil-map", "def-trf-local-term", "def-trf-trace-class-source", "lem-trf-trace-map-from-external-duality", "thm-trf-frobenius-fixed-points"]
+++
Let $c$ be an admissible correspondence with
$\operatorname{Fix}(c)=F$, and let $y\in F(k)$ be a geometric fixed
point which is an open-and-closed component of $F$.

1. The restriction
$\operatorname{Tr}_c(u)|_y$, and hence the local term
$\operatorname{LT}_y(u)$ of [def-trf-local-term], depend only on
the stalk $K_{\bar y}$ and on the stalk map
$u_{\bar y}:K_{\bar y}\to K_{\bar y}$ induced by $u$, together with
the fixed-point datum $c_1(y)=c_2(y)$. No invertibility of $u$ is
required.
1. (Zero-stalk vanishing.) If $K_{\bar y}=0$, then
$\operatorname{Tr}_c(u)|_y=0$ and $\operatorname{LT}_y(u)=0$, for
every coefficient morphism $u$.
1. (Smooth-curve form.) In the smooth-curve setting of
[d-curve-pieces] — $X_0$ smooth of pure dimension one, $m\ge1$,
$x\in X_0(\mathbf F_{q^m})$ with geometric point $\bar x$ — let
$v:L\Phi^{m*}K\to K$ be either the scheme-Frobenius map
$u_m=\varphi^{[m]}\circ\kappa^{(m)}_K$ of [def-trf-iterated-weil-map]
(the map written $\varphi_m$ in [d-curve-pieces]) or an arbitrary,
not necessarily invertible, Frobenius coefficient morphism
$L\Phi^{m*}K\to K$ (in the sense of
[def-trf-frobenius-coefficient-morphism] for $\Phi^m$, the
$q^m$-power Frobenius of $X_0\times_{k_0}\mathbf F_{q^m}$; for
instance the iterate $\psi_m$ of a Frobenius coefficient morphism
$\psi$), and consider the graph correspondence of
$(\Phi^m,v)$ of [def-trf-graph-correspondence], assumed admissible
as throughout so that its trace class is defined. If $K_{\bar x}=0$,
then the local term $\operatorname{LT}_{\bar x}(v)$ at the fixed
point $\bar x$ is zero.

## Proof

By [def-trf-trace-class-source], the trace-class source is the
internal Hom $\mathcal H_c(K)=R\mathcal Hom_A(c_2^*K,c_1^!K)$, whose
stalk at the fixed point $y$ — using the purity clause of the
six-operations package in relative dimension zero, which identifies
$c_1^!K$ and $c_2^*K$ with $K$ on the fixed scheme — is

$$
\mathcal H_c(K)_{\bar y}\cong R\mathcal Hom_A(K_{\bar y},K_{\bar y}),
$$

and the mate $\widetilde u$ restricts to the mate of $u_{\bar y}$.
By [lem-trf-trace-map-from-external-duality], the trace map is the
composite of the evaluation map $e_K$, the fixed-square base change
and the dualizing composition, all of which are local on the fixed
scheme: their restriction to the open-and-closed component $y$ is
computed from the stalk data alone. Hence the restriction
$\operatorname{Tr}_c(u)|_y$, and the integral of
[def-trf-local-term] over the component $y$, depend only on
$(K_{\bar y},u_{\bar y})$. Nowhere was $u$ inverted: the mate, the
evaluation, the base change and the dualizing composition are
defined for an arbitrary morphism $u$. This proves (1).

For (2), if $K_{\bar y}=0$ then the stalk
$\mathcal H_c(K)_{\bar y}\cong R\mathcal Hom_A(0,0)=0$, so the
restriction of the mate $\widetilde u$ to the component $y$ is a map
into the zero object, and so is its image under the evaluation map
$e_K$ restricted to $y$. The restriction $\operatorname{Tr}_c(u)|_y$
is obtained from this zero map by composing with the (local)
base-change and dualizing-composition maps, hence is the zero map
$A_y\to\omega_{y,A}$. The integration of [def-trf-local-term] is
$A$-linear, so $\operatorname{LT}_y(u)=\int_y 0=0$.

For (3), the graph correspondence of $(\Phi^m,v)$ has
$C=X$, $c_1=\operatorname{id}_X$, $c_2=\Phi^m$ and fixed scheme
$\operatorname{Fix}(\Phi^m)$ by [def-trf-graph-correspondence]. By
[thm-trf-frobenius-fixed-points] this fixed scheme is the disjoint
union of copies of $\Spec k$, one for each point of
$X_0(\mathbf F_{q^m})$; in particular it is finite over $k$, hence
proper with finitely many open-and-closed components, so the local
terms of [def-trf-local-term] are defined, and the geometric point
$\bar x$ over $x$ is one of these components, an isolated and hence
open-and-closed fixed point. Its stalk map is
$v_{\bar x}:K_{\bar x}=(L\Phi^{m*}K)_{\bar x}\to K_{\bar x}$, using
$\Phi^m(\bar x)=\bar x$. Applying (2) with $y=\bar x$ and $u=v$ gives
$\operatorname{LT}_{\bar x}(v)=0$ when $K_{\bar x}=0$; since (1) and
(2) use no invertibility of $u$, this holds both for the
scheme-Frobenius map $u_m$ and for an arbitrary Frobenius coefficient
morphism.
