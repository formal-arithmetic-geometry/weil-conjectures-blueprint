+++
kind  = "proof"
of    = "lem-amb-affine-space-top-trace"
+++
For $d=1$, apply the exact extension-by-zero triangle constructed in the proof
of [lem-amb-closed-support-hom] to the affine
open $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$
and the infinity section $i$. It gives

$$
Rp_{1!}A\longrightarrow Rq_*A\longrightarrow A_S
\longrightarrow Rp_{1!}A[1].
$$

Under [thm-amb-p1-decomposition], the second arrow
is $(1,0)$. Its value on the unit is the identity;
its value on $h=c_1(\mathcal O(1))$ is zero because
$i^*\mathcal O(1)\cong\mathcal O_S$.
Consequently the trace of [def-amb-p1-trace]
restricts to an isomorphism
$Rp_{1!}A(1)[2]\to A_S$. This restricted trace is
exactly the counit obtained by composing
$j_!\dashv j^*$ with the projective-line adjunction
in [cor-amb-affine-space-adjunction].

For general $d$, use the tower of affine-line
projections from [cor-amb-affine-space-adjunction].
The projection formula of
[lem-amb-proper-coproducts-projection], applied on
the chosen compactifications, and the just-proved
one-dimensional isomorphism show successively that
$Rp_{d!}A(d)[2d]\cong A_S$. Under this
identification the composite counit is the composite
of $d$ identity maps. The base-change statement
follows either from the same tower and the natural
extension-by-zero triangle, or from the explicit
unit–counit compatibility proved in
[prop-asd-smooth-base-change].
