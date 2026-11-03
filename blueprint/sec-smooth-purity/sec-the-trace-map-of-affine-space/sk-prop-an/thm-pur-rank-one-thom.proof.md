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

and all other supported cohomology vanishes, so the map on the
cohomology sheaves is the
def:coefficient-twists-canonical identification

$$
R\Gamma_c(\mathbf A^1_{\bar b},\Lambda(1)[2])
\cong \Lambda_b\cdot(\text{the class of the origin})
\cong\Lambda
$$

(the shift and twist being the ones of the boundary). Hence
$\tau_E$ is an isomorphism at every geometric point; the cone is a
bounded constructible complex with zero geometric stalks, so it is
zero (the standard truncation argument of
[def-weil-derived-cohomology-sheaves]).

Step 3: base change. The class of the zero divisor, the Kummer
boundary, and the compactly supported direct image are compatible with
base change ([lem-pur-divisor-class], and
[lem-pur-cfiber-stalk]) by the compatibilities of the
corresponding statements; hence so is $\tau_E$.
