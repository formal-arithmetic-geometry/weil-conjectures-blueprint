+++
kind = "proof"
of = "theorem-contracting-correspondences-local-terms"
order = 1711
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "corollary-evaluation-weakly-contractible-objects", "corollary-continuity-cohomology", "theorem-comparison-direct-images", "definition-pro-etale-base-change-map", "lemma-change-coefficients", "definition-deformation-normal-bundle", "definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "theorem-proper-pushforward-lefschetz-verdier", "proposition-additivity-trace-classes", "lemma-sheaves-finite-support-finite-morphisms", "lemma-functoriality-deformation", "theorem-verdier-s-theorem-specialization-zero", "proposition-external-kunneth-formula-nearby-cycles", "proposition-nearby-cycles-commute-verdier-duality", "proposition-specialization-trace-class", "corollary-specialization-when-fixed-point-scheme", "lemma-normal-cones-contracting-ideals"]
+++
We split $K$ by the triangle $j_!j^*K\to K\to Ri_*i^*K$ and use
additivity of trace classes. The piece supported on $Z$ gives the trace
of $u_Z$. The piece $j_!j^*K$, on the other hand, has zero trace, which we show by deforming
to the normal cone.

*Reductions.* We may assume that $W=C$, that $\Fix(c)=F_0$ and that
the ideal inclusions hold on $C$. Indeed, by
Remark [remark-reduction-connected-fixed-point-scheme], restricting $C$ to $W$
and removing the other connected components of $\Fix(c)$ changes neither
the trace class on $F_0$ nor $u_Z$ near $F_{0,Z}$.
By Lemma [lemma-fixed-point-scheme-deformation], the common map
$\Fix(c)\to X$ maps set-theoretically into $Z$. The same lemma shows
that after base change from $T$ to $S$ the reduction of the fixed scheme
of the deformed correspondence is $(\Fix(c)\times S)_{\mathrm{red}}$, as
Corollary [corollary-specialization-when-fixed-point-scheme] requires.

*The case $i^*K=0$.* We show that $\operatorname{Tr}_c(u)=0$. First,
the specialized complex vanishes on the zero section,

$$
\operatorname{Sp}_{X,Z}(K)|_Z=0,
$$

because Verdier's theorem on the zero section
(Theorem [theorem-verdier-s-theorem-specialization-zero]) identifies the restriction of
$\operatorname{Sp}_{X,Z}(K)$ to the zero section with the restriction
of $K$ to $Z$, and invariance under the nilpotent thickening
$Z_{\mathrm{red}}\to Z$ passes from $Z$ to $Z_{\mathrm{red}}$.

Next, consider the leg $\gamma_2$ of the correspondence on the special
fibre, along which we take ordinary pullback. It maps set-theoretically
into the zero section by
Lemma [lemma-normal-cones-contracting-ideals](2). Invariance under
nilpotent thickenings therefore gives $\gamma_2^*\operatorname{Sp}_{X,Z}(K)=0$.
So the specialized morphism has zero source, and its trace is zero.

Finally, we relate this trace to $\operatorname{Tr}_c(u)$. The generic
fibre of the deformed correspondence is $c$ over $\eta$. So
Proposition [proposition-specialization-trace-class] identifies the
zero trace with the specialization of the pullback of
$\operatorname{Tr}_c(u)$ to the generic fibre. By
Corollary [corollary-specialization-when-fixed-point-scheme],
specialization is the identity under the identifications for constant
families, and these carry that pullback to $\operatorname{Tr}_c(u)$.
Hence $\operatorname{Tr}_c(u)=0$.

*General $K$.* We apply Proposition [proposition-additivity-trace-classes](2)
to the triangle

$$
j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K,
\qquad j:X\setminus Z_{\mathrm{red}}\hookrightarrow X,
$$

whose hypothesis $c_1^{-1}(Z_{\mathrm{red}})\subset c_2^{-1}(Z_{\mathrm{red}})$
follows from $I_2\subset I_1$.
The open piece has zero trace by the case just treated, while the closed
graded piece is the proper pushforward of $u_Z$ along $i$ and $i'$, by
Lemma [lemma-closed-piece-pushforward], and
Theorem [theorem-proper-pushforward-lefschetz-verdier] identifies its trace with the
pushforward of the trace class of $u_Z$.
To compare with $F_0$, note that the map $h_{F_0}$ is an isomorphism after reduction, because $\Fix(c)$ lies
in $c_1^{-1}(Z)$ set-theoretically by
Lemma [lemma-fixed-point-scheme-deformation]. This proves the displayed formula.
If $F_0$ is proper, then so is $F_{0,Z}$, and pushing both sides forward to
$\operatorname{Spec}k$ and composing with the trace map of
Definition [definition-trace-class-local-terms] gives the equality of
local terms.
