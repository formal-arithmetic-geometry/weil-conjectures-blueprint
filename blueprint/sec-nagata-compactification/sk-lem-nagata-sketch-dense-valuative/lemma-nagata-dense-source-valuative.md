+++
id = "lemma-nagata-dense-source-valuative"
kind = "lemma"
title = "[stacks-project]"
order = 282
lean = ["AlgebraicGeometry.IsSeparated.of_valuativeCriterion_of_isDominant", "AlgebraicGeometry.UniversallyClosed.of_valuativeCriterion_of_isDominant"]
uses = ["def-nagata-dense-compactification", "def-nagata-dense-valuation-probe", "def-nagata-extended-ideal", "def-nagata-scheme-image-comparison", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-composite-valuation-ring", "lemma-nagata-dense-flat-pullback", "lemma-nagata-dense-valuation-probe", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-valuation-ring-extension"]
+++
Let $f\colon X\to S$ be a morphism of schemes, let
$h\colon U\to X$ be quasi-compact, and assume $h(U)$ is dense in $X$. Suppose that for every valuation
ring $A$ with fraction field $K$, every commutative diagram

$$
\operatorname{Spec}(K)\longrightarrow U\longrightarrow X,
\qquad
\operatorname{Spec}(A)\longrightarrow S
$$

has a unique lift $\operatorname{Spec}(A)\to X$. If $f$ is
quasi-compact, then $f$ is universally closed. If $f$ is quasi-separated,
then $f$ is separated.

## Proof

**Universal closedness.** Assume $f$ is quasi-compact. By the existence
part of the valuative criterion (Stacks Project, Tag 01KF) it suffices to
show that every commutative square

$$
\operatorname{Spec}(K)\longrightarrow X,
\qquad
\operatorname{Spec}(A)\longrightarrow S,
$$

with $A$ a valuation ring with fraction field $K$, has a lift
$\operatorname{Spec}(A)\to X$.

*Reduction to an affine base.* The closed point of
$\operatorname{Spec}(A)$ maps into an affine open
$\operatorname{Spec}(R)\subseteq S$; since every point of
$\operatorname{Spec}(A)$ generalizes the closed point and opens are stable
under generization, all of $\operatorname{Spec}(A)$ maps into
$\operatorname{Spec}(R)$. Replace $S$ by $\operatorname{Spec}(R)$, $X$ by
$f^{-1}(\operatorname{Spec}(R))$ and $U$ by its inverse image: $f$ and $h$
stay quasi-compact, $h(U)$ stays dense, and the lifting hypothesis is
inherited, since lifts land in $f^{-1}(\operatorname{Spec}(R))$.

*Reduction to a scheme-theoretically dense source.* Let
$X_0=\operatorname{SIm}(h)\hookrightarrow X$, with factor map
$h_0=h^{\mathrm{im}}\colon U\to X_0$ ([def-nagata-scheme-image-factor]). Since
$h$ is quasi-compact, the underlying set of $X_0$ is the closure of
$h(U)$, which is $X$, and $\mathcal O_{X_0}\to h_{0*}\mathcal O_U$ is
injective ([lemma-nagata-scheme-image-ideal-qc]); thus $h_0$ is
scheme-theoretically dense, and it is quasi-compact because $h$ is and
$X_0\to X$ is separated. As $X_0$ is a closed subscheme of $X$ with the same
underlying set, its ideal consists of locally nilpotent sections, so $X_0$
contains $X_{\mathrm{red}}$, and every morphism from a reduced scheme to $X$
factors uniquely through $X_0$. Spectra of fields and of valuation rings are
reduced. Hence the lifting problems for $X_0\to S$ and for $X\to S$ are the
same, the hypothesis of the lemma holds for $X_0\to S$ and $h_0$, and
$X_0\to S$ is quasi-compact. Replacing $X$ by $X_0$, we may assume that
$h$ is scheme-theoretically dense, i.e. $\ker(h)=0$.

*A valuation probe.* Choose an affine open
$\operatorname{Spec}(B)\subseteq X$ through which the generic map
$\operatorname{Spec}(K)\to X$ factors. Choose a polynomial $B$-algebra $P$
and a surjection $P\twoheadrightarrow K$ presenting this field-valued point.
The map $\operatorname{Spec}(P)\to\operatorname{Spec}(B)\subseteq X$ is
flat. Therefore

$$
U_P=U\times_X\operatorname{Spec}(P)\longrightarrow\operatorname{Spec}(P)
$$

is quasi-compact and scheme-theoretically dense by
[lemma-nagata-dense-flat-pullback]; by
[lemma-nagata-scheme-image-ideal-qc] its image is then dense, i.e. it is
dominant. Apply [lemma-nagata-dense-valuation-probe] to it and the point
$\operatorname{Spec}(K)\subseteq\operatorname{Spec}(P)$. We obtain a
valuation ring $A'$, with fraction field $K'$, whose generic point maps
to $U_P$ and whose closed point maps to the chosen $K$-point of
$\operatorname{Spec}(P)$. If $k'=A'/\mathfrak m_{A'}$, this gives a field
embedding $K\to k'$. By [lemma-nagata-valuation-ring-extension], choose a
valuation ring $A''\subseteq k'$ with fraction field $k'$ such that
$K\cap A''=A$.

*The composite valuation ring.* Form the inverse-image ring

$$
C=\{a\in A'\mid a\bmod\mathfrak m_{A'}\in A''\}.
$$

By [lemma-nagata-composite-valuation-ring], $C$ is a valuation ring
with fraction field $K'$, and $C/\mathfrak m_{A'}=A''$. The map
$R\to A'$ lands in $C$: its reduction modulo $\mathfrak m_{A'}$ is
$R\to A\subseteq K\subseteq k'$, which lands in $A\subseteq A''$. Thus the
generic map $\operatorname{Spec}(K')\to U$ and the map
$\operatorname{Spec}(C)\to S$ form a diagram covered by the hypothesis.
Let $g_C\colon\operatorname{Spec}(C)\to X$ be its unique lift.

There are now two maps $\operatorname{Spec}(A')\to X$: one is obtained
from $\operatorname{Spec}(A')\to\operatorname{Spec}(P)\to X$, and the
other by composing $\operatorname{Spec}(A')\to\operatorname{Spec}(C)$
with $g_C$. They have the same generic map through $U$ and the same
composite to $S$. Applying the assumed uniqueness to the valuation ring
$A'$ shows that the two maps are equal.

*The lift.* Restrict $g_C$ along the closed immersion
$\operatorname{Spec}(A'')\to\operatorname{Spec}(C)$ induced by
$C/\mathfrak m_{A'}\cong A''$. Its generic point is
$\operatorname{Spec}(k')$, the residue field of the prime
$\mathfrak m_{A'}\subset C$. The preceding equality on
$\operatorname{Spec}(A')$ identifies this generic map with the closed-point
residue map of $\operatorname{Spec}(A')\to X$ and hence with the base
change of the original $\operatorname{Spec}(K)\to X$ along $K\to k'$. Let
$x\in X$ be the image of the closed point of $\operatorname{Spec}(A'')$. The
image of the induced local homomorphism $\mathcal O_{X,x}\to A''$ lies in
the subfield $K\subseteq k'$, hence in $K\cap A''=A$. So the local
homomorphism factors through $A$, and therefore defines a morphism
$\operatorname{Spec}(A)\to X$ extending $\operatorname{Spec}(K)\to X$. It is
compatible with $\operatorname{Spec}(A)\to S=\operatorname{Spec}(R)$: the
induced ring map $R\to A$, followed by the injection $A\subseteq A''$, is the
map $R\to C\to A''$ given by $g_C$, which is $R\to A\subseteq A''$; so it is
the given map $R\to A$. This is the required lift, and $f$ is universally
closed.

**Separatedness.** Assume $f$ is quasi-separated. Then its diagonal
$\Delta_f\colon X\to X\times_SX$ is quasi-compact. We check the hypothesis of
the lemma for $\Delta_f$ and the same $h\colon U\to X$. A square for
$\Delta_f$ consists of $\operatorname{Spec}(K)\to U\to X$ and a map
$\operatorname{Spec}(A)\to X\times_SX$, i.e. a pair of maps $a_1,a_2\colon
\operatorname{Spec}(A)\to X$ over $S$, both restricting to the given generic
map through $U$. By the uniqueness hypothesis for $f$, $a_1=a_2$, so the
pair factors through $\Delta_f$, and uniquely, since $\Delta_f$ is a
monomorphism. Applying the universal-closedness part, already proved, to the
quasi-compact morphism $\Delta_f$ shows that $\Delta_f$ is universally
closed. Since every diagonal is an immersion, a universally closed diagonal
is a closed immersion. Thus $f$ is separated.
