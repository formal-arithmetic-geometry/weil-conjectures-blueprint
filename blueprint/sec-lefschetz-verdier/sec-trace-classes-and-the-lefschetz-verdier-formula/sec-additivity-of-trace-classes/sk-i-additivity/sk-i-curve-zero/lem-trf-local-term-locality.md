+++
id = "lem-trf-local-term-locality"
kind = "lemma"
title = "Locality and zero-stalk vanishing of the local term"
order = 3797
uses = ["d-curve-pieces", "def-trf-correspondence", "def-trf-frobenius-coefficient-morphism", "def-trf-graph-correspondence", "def-trf-iterated-weil-map", "def-trf-local-term", "def-trf-trace-class-source", "lem-trf-local-term-point", "lem-trf-trace-map-from-external-duality", "thm-trf-frobenius-fixed-points"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be an admissible correspondence with
$\operatorname{Fix}(c)=F$, coefficient $K\in D^b_{ctf}(X,A)$ and
$u:c_2^*K\to c_1^!K$ ([def-trf-correspondence]), and let $y\in F(k)$ be a
geometric fixed point which is an open-and-closed component of $F$. Say
that $c$ is *contracting at $y$* if $c_1^{-1}(y)$ is the reduced point $y$,
$c_2(y)=y$, and the ideal sheaves on $C$ satisfy

$$
c_2^{\cdot}(\mathcal I_y)^n\subset\mathcal I_{y,C}^{\,n+1}\qquad\text{for some }n\geq1,
$$

where $\mathcal I_{y,C}=c_1^{\cdot}(\mathcal I_y)\mathcal O_C$ is the ideal of
the reduced point $y\subset C$. The stabilizing
inclusion $c_2^{\cdot}(\mathcal I_y)\subset\mathcal I_{y,C}$ follows from
$c_2(y)=y$, and the condition holds with $n=1$ whenever the map induced by
$c_2$ on the cotangent space at $y$ is zero.

1. (Contracting local terms.) If $c$ is contracting at $y$, then the
restriction $\operatorname{Tr}_c(u)|_y$, and hence the local term
$\operatorname{LT}_y(u)$ of [def-trf-local-term], depend only on the stalk
$K_{\bar y}$ and on the stalk map $u_{\bar y}:K_{\bar y}\to K_{\bar y}$
induced by $u$ (via $c_2(y)=y=c_1(y)$):
$\operatorname{LT}_y(u)=\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$.
No invertibility of $u$ is required.
1. (Zero-stalk vanishing.) If $c$ is contracting at $y$ and $K_{\bar y}=0$,
then $\operatorname{Tr}_c(u)|_y=0$ and $\operatorname{LT}_y(u)=0$, for
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
