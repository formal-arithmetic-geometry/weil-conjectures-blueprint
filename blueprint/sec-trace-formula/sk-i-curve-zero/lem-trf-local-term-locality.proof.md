+++
kind  = "proof"
of    = "lem-trf-local-term-locality"
+++
*The stalk of the trace-class source.* By [def-trf-trace-class-source]
the source is $\mathcal H_c(K)=R\mathcal Hom_A(c_2^*K,c_1^!K)$. Its stalk
at $y$ is **not** $R\mathcal Hom_A(K_{\bar y},K_{\bar y})$: restriction to
a point commutes with $i^!$ on internal Hom, but not with $i^*$. For
$X=\mathbf A^1$, $j:\mathbf G_m\hookrightarrow X$, $K=j_!A$ and the graph
of a Frobenius (so that $c_2^*K\simeq K$ and $c_1^!K=K$), internal-Hom
adjunction gives $R\mathcal Hom_A(j_!A,j_!A)\simeq Rj_*A$, whose
degree-zero stalk at $0$ is $A$ (the punctured strictly henselian curve is
connected), although $K_0=0$. Hence (1) and (2) cannot be read off from
the stalk: the trace map of [lem-trf-trace-map-from-external-duality] is
local on $F$, but its source at $y$ sees more than $(K_{\bar y},u_{\bar y})$.
A nonzero source can still map to zero, and for contracting correspondences
it does; this is the content of (1) and (2).

*(1) and (2).* These are the contracting-correspondence theorem of
Varshavsky, [Thm. 2.1.3](https://arxiv.org/abs/math/0505564), translated
into the present conventions. In Varshavsky's convention a $c$-morphism is
$c_1^*\mathcal F\to c_2^!\mathcal F$; interchanging the legs, his
hypothesis "$c$ stabilizes $Z$ and is contracting near $Z$" for
$Z=\{y\}$ reads
$c_2^{\cdot}(\mathcal I_y)\subset c_1^{\cdot}(\mathcal I_y)\mathcal O_C$ and
$c_2^{\cdot}(\mathcal I_y)^n\subset(c_1^{\cdot}(\mathcal I_y)\mathcal O_C)^{n+1}$,
which is the hypothesis above. His conclusion, for the open-and-closed
component $\beta=\{y\}$ of $F$, which meets $Z$, is
$\operatorname{Tr}_c(u)|_y=\operatorname{Tr}_{c|_Z}(u|_Z)|_y$ and
$\operatorname{LT}_y(u)=\operatorname{LT}_y(u|_Z)$, where
$c|_Z:c_1^{-1}(Z)_{\mathrm{red}}\to Z\times Z$ is the correspondence
induced on $Z$ and $u|_Z$ the restricted coefficient morphism (his 1.5.6).
Since $c_1^{-1}(y)=y$ is reduced, $c|_Z$ is the identity correspondence of
the point $y\cong\Spec k$, with coefficient $K_{\bar y}$ and morphism the
stalk map $u_{\bar y}$; its local term is
$\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$ by
[lem-trf-local-term-point]. This proves (1), and (2) is the case
$K_{\bar y}=0$, where $\operatorname{tr}_A(0\mid0)=0$. Varshavsky's theorem
is proved by specialization to the normal cone of $Z$ (his §§1.3–1.4 and
2.1); it holds for every $c$-morphism and for the finite coefficient rings
$A=A_{E,n}$ (his §1.1), and nothing is inverted. Its proof reduces, via
the additivity of trace classes along the open–closed decomposition
$X=Z\sqcup U$ and proper pushforward from $Z$, precisely to the vanishing
(2) for $j_!j^*K$, which is then shown by the normal-cone argument; the
blueprint quotes this argument and does not reprove it.

*(3).* The graph correspondence of $(\Phi^m,v)$ has
$C=X$, $c_1=\operatorname{id}_X$, $c_2=\Phi^m$ and fixed scheme
$\operatorname{Fix}(\Phi^m)$ by [def-trf-graph-correspondence]. By
[thm-trf-frobenius-fixed-points] this fixed scheme is the disjoint
union of copies of $\Spec k$, one for each point of
$X_0(\mathbf F_{q^m})$; in particular it is finite over $k$, hence
proper with finitely many open-and-closed components, so the local
terms of [def-trf-local-term] are defined, and the geometric point
$\bar x$ over $x$ is one of these components, an isolated reduced fixed
point. The graph is contracting at $\bar x$: $c_1^{-1}(\bar x)=\bar x$,
$\Phi^m(\bar x)=\bar x$, and if $t_i$ are affine coordinates with
$a_i=t_i(x)\in\mathbf F_{q^m}$, then
$\Phi^{m\cdot}(t_i-a_i)=t_i^{q^m}-a_i=(t_i-a_i)^{q^m}$, so
$\Phi^{m\cdot}(\mathcal I_{\bar x})\mathcal O_X\subset\mathcal I_{\bar x}^{\,q^m}\subset\mathcal I_{\bar x}^{\,2}$
as $q^m\geq2$; this holds for every separated finite-type $X_0$, not only
for curves. Its stalk map is
$v_{\bar x}:K_{\bar x}=(L\Phi^{m*}K)_{\bar x}\to K_{\bar x}$, using
$\Phi^m(\bar x)=\bar x$. Applying (2) with $y=\bar x$ and $u=v$ gives
$\operatorname{LT}_{\bar x}(v)=0$ when $K_{\bar x}=0$; since (1) and
(2) use no invertibility of $u$, this holds both for the
scheme-Frobenius map $u_m$ and for an arbitrary Frobenius coefficient
morphism.
