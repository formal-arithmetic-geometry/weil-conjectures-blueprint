+++
kind  = "proof"
of    = "thm-pur-rank-one-thom"
+++
The zero section and local trivializations are those of [def-pur-vector-bundle-zero-section]; at finite level the objects have the etale representatives of [def-weil-pbc-etale-origin-witness].
Step 1: the class is global. The zero divisor $z(B)\subset E$ is an
effective Cartier divisor, smooth over $B$ of pure codimension one,
so [lem-pur-divisor-class] supplies the class
$\operatorname{thom}(E)$ globally and canonically (the
coordinate-independence of [lem-pur-frame-independence]), and
$\tau_E$ is the induced morphism of the global objects.

Step 2: on a geometric fiber. Let $\bar b\to B$ be a geometric
point. By [lem-pur-cfiber-stalk], the stalk of $\tau_E$ at
$\bar b$ is the morphism

$$
\Lambda\;\longrightarrow\;R\Gamma_c\bigl(\mathbf A^1_{\bar b},
\Lambda(1)[2]\bigr)
$$

given by the class of the divisor $0\subset\mathbf A^1_{\bar b}$, i.e.
by the boundary of the Kummer class of the coordinate. By
[thm-pur-rank-one-local-calculation] this boundary is the
normalized generator of the free rank-one module

$$
H^2_0\bigl(\mathbf A^1_{\bar b},\Lambda(1)\bigr)
\;\cong\;\Lambda,
$$

and all other supported cohomology vanishes. This supported calculation
does not by itself identify $R\Gamma_c$; the compact-support identification
is obtained on the projective line. Let
$j:\mathbf A^1_{\bar b}\hookrightarrow\mathbf P^1_{\bar b}$, with complement
the point $\infty$. Localization gives the triangle

$$
C:=R\Gamma_c(\mathbf A^1_{\bar b},\Lambda(1)[2])
\longrightarrow R\Gamma(\mathbf P^1_{\bar b},\Lambda(1)[2])
\longrightarrow \Lambda(1)[2]\longrightarrow,
$$

the second map being restriction to $\infty$. The projective-line
decomposition given by the unit and $h=c_1(\mathcal O(1))$,

$$
R\Gamma(\mathbf P^1_{\bar b},\Lambda(1)[2])\simeq\Lambda(1)[2]\oplus\Lambda,
$$

precedes this theorem: it follows from the Kummer sequence, the degree on
the Picard group and the cohomology of curves
([03RQ](https://stacks.math.columbia.edu/tag/03RQ)), and uses neither
smooth purity nor Poincar\'e duality. Restriction to $\infty$ is
$(\mathrm{id},0)$, so $C\simeq\Lambda$ and
$H^2_c(\mathbf A^1_{\bar b},\Lambda(1))\to H^2(\mathbf P^1_{\bar b},\Lambda(1))$
is an isomorphism. The divisor morphism is identified by applying $j_!$
to the supported class and mapping to ordinary cohomology on
$\mathbf P^1_{\bar b}$: by naturality of the Cartier construction and
$j_!\dashv j^*$ the composite is the global class of the divisor $0$.
With the convention of [lem-pur-divisor-class], $\operatorname{cl}(0)=-c_0$,
this global class is $-h$, a generator. Hence the map on cohomology sheaves
is an isomorphism $\Lambda\cong R\Gamma_c(\mathbf A^1_{\bar b},\Lambda(1)[2])$,
and for the trace $t_c$ normalized by $t(h)=1$,

$$
t_c\circ\tau_E=-\mathrm{id},\qquad \tau_E^{-1}=-t_c ;
$$

the sign convention of [lem-pur-divisor-class] is kept. This is the
argument at a finite coefficient ring $\Lambda=A$; for integral
coefficients use the canonical reduction comparison and derived Nakayama
on the cone, completeness coming from the earlier constructibility
results, and for $E,\Qlb$ rationalization and descent. Hence
$\tau_E$ is an isomorphism at every geometric point; the cone is a
bounded constructible complex with zero geometric stalks, so it is
zero (the standard truncation argument of
[def-weil-derived-cohomology-sheaves]).

Step 3: base change. The class of the zero divisor, the Kummer
boundary, and the compactly supported direct image are compatible with
base change ([lem-pur-divisor-class], and
[lem-pur-cfiber-stalk]) by the compatibilities of the
corresponding statements; hence so is $\tau_E$.
