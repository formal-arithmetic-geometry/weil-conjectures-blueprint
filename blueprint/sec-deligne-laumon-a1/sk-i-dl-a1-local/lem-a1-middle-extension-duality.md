+++
id = "lem-a1-middle-extension-duality"
kind = "lemma"
title = "Duality for curve middle extensions"
order = 2924
uses = ["cor-cbc-proper-coincidence", "cor-pur-smooth-admissibility", "def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "def-wf-tate-twist", "fix-cor-verdier-exchange", "lem-a1-finite-boundary-cohomology", "lem-fix-weil-operations", "lem-pod-cohomology-of-dual-over-field", "prop-a1-curve-boundary-sequence", "prop-cohomological-finiteness", "prop-pur-rational-purity-trace-coherence", "thm-pur-rational-and-qbar-purity"]
+++
Let $\bar C_0$ be a smooth projective curve, let
$j:U_0\hookrightarrow\bar C_0$ be dense open with finite closed
complement $i:Z_0\hookrightarrow\bar C_0$, and let $\mathcal F$
be a lisse $\Qlb$-Weil sheaf on $U_0$.
Put $M=j_*\mathcal F$, the ordinary
middle extension, and put
$\mathcal G=\mathcal F^\vee(1)$, with the
Tate twist.
There are canonical perfect Frobenius-equivariant pairings

$$
H^r(\bar C,M)\times
H^{-r}\bigl(\bar C,\mathbb D_{\bar C}M\bigr)
\longrightarrow\Qlb,
$$

and

$$
H^r(\bar C,j_*\mathcal F)\times
H^{2-r}(\bar C,j_*\mathcal G)\longrightarrow\Qlb
\qquad(r\in\mathbf Z),
$$

with the cohomology
conventions of the blueprint. In degree one the second pairing is
the pairing on the images of compact-support cohomology in ordinary
cohomology.

## Proof

First derive the smooth-curve pairing with compact supports, allowing
the smooth curve to be nonproper. Smooth admissibility is supplied by
[cor-pur-smooth-admissibility], with the field-stage orientation
of [thm-pur-rational-and-qbar-purity].
Apply [fix-cor-verdier-exchange] to its structure map. Since the
dualizing object at the point is $\Qlb$, it gives

$$
R\Gamma_c(U,\mathcal F)^\vee
\cong R\Gamma(U,\mathbb D_U\mathcal F)
\cong R\Gamma(U,\mathcal F^\vee(1))[2].
$$

The last identification uses the smooth orientation and the ordinary
finite-rank dual of a lisse sheaf: at finite coefficient level it is
the finite locally free tensor–Hom identity, transported to the
field coefficient stage. The complexes at the point have finite
dimensional bounded cohomology by
[prop-cohomological-finiteness]. Taking cohomology, using
[lem-pod-cohomology-of-dual-over-field], gives perfect pairings

$$
H_c^r(U,\mathcal F)\times H^{2-r}(U,\mathcal G)
\longrightarrow\Qlb.
$$

Apply the same argument to $\mathcal G$, whose dual twist is
$\mathcal F$, to obtain the pairings with the two support
conditions exchanged. These pairings are evaluation followed by the
smooth trace. The equivariance of evaluation and adjunction maps is
[lem-fix-weil-operations], and that of the normalized trace and
orientation is [prop-pur-rational-purity-trace-coherence].
Consequently all the pairings are Frobenius-equivariant.

Write

$$
t_{\mathcal F}:H_c^1(U,\mathcal F)\longrightarrow H^1(U,\mathcal F),
\qquad
t_{\mathcal G}:H_c^1(U,\mathcal G)\longrightarrow H^1(U,\mathcal G)
$$

for forgetting supports. These two maps are transposes under the
displayed perfect pairings, with the usual degree-one cup-product
sign. Indeed, if $x,y$ have compact support, evaluating
$x\smile t_{\mathcal G}y$ or
$t_{\mathcal F}x\smile y$ and applying the trace gives the same
compactly supported cup product. This follows directly from the
natural map $j_!\to Rj_*$, tensor evaluation, and the adjunction
counit defining the trace; interchanging the two factors introduces
only the graded-commutativity sign. Thus it is an identity of the
specified maps, not only an abstract comparison of dimensions.

We identify the relevant images. By
[prop-a1-curve-boundary-sequence], [lem-a1-finite-boundary-cohomology]
and proper coincidence [cor-cbc-proper-coincidence], the maps

$$
H_c^1(U,\mathcal F)\longrightarrow H^1(\bar C,M),
\qquad H_c^2(U,\mathcal F)\longrightarrow H^2(\bar C,M)
$$

are respectively surjective and an isomorphism. Moreover
$H^0(\bar C,M)=H^0(U,\mathcal F)$ by the definition of ordinary
direct image. The cone of the natural map
$M=\mathcal H^0(Rj_*\mathcal F)\to Rj_*\mathcal F$ lies in
$D^{\geq1}$. Its derived global sections still lie in
$D^{\geq1}$, so the long exact sequence gives an injection

$$
H^1(\bar C,M)\hookrightarrow H^1(U,\mathcal F).
$$

The composite of this injection with the preceding surjection is
$t_{\mathcal F}$. Hence

$$
H^1(\bar C,j_*\mathcal F)=\operatorname{im}t_{\mathcal F}.
$$

The same identifications hold for $\mathcal G$.

For completeness, the linear algebra on these images is as follows.
Put $A=H_c^1(U,\mathcal F)$ and
$B=H_c^1(U,\mathcal G)$. The two perfect support pairings identify
the targets of $t_{\mathcal F}$ and $t_{\mathcal G}$ with
$B^\vee$ and $A^\vee$. Up to the fixed cup-product sign, the
maps $A\to B^\vee$ and $B\to A^\vee$ are transposes.
The bilinear form defining them has precisely their kernels as
its two radicals. It therefore induces a perfect form on the
quotients by those kernels, which are their images. This is the
asserted perfect pairing in degree one. The degree-zero and
degree-two assertions are exactly the smooth-curve pairings above,
using $H^0(\bar C,M)=H^0(U,\mathcal F)$ and
$H^2(\bar C,M)=H_c^2(U,\mathcal F)$.
The groups in the remaining degrees vanish: negative sheaf
cohomology is zero, the displayed smooth-curve duality gives
$H_c^r(U,\mathcal F)=0$ for $r>2$, and the finite-boundary
sequence gives the same vanishing for $M$.

Finally apply the formal exchange
[fix-cor-verdier-exchange] to the smooth proper structure map
of $\bar C$ and the constructible sheaf $M$. It gives
$R\Gamma(\bar C,M)^\vee\cong R\Gamma(\bar C,\mathbb D_{\bar C}M)$.
The same finite-dimensional point-dual calculation proves the first
displayed pairing. Neither argument uses general constructible
biduality or a general direct-image weight theorem.
