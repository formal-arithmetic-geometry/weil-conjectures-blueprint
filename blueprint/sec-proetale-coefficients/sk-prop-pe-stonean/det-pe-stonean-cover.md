+++
id = "det-pe-stonean-cover"
kind = "lemma"
title = "Stonean covers of compact Hausdorff spaces"
lean = ["CompHaus.projectivePresentation", "ultrafilterBasis_is_basis", "ultrafilter_compact", "Ultrafilter.t2Space", "denseRange_pure", "CompHaus.projective_ultrafilter", "continuous_ultrafilter_extend", "ultrafilter_extend_extends"]
order = 896
uses = ["det-pe-stonean-projective"]
+++
Let $T$ be a compact Hausdorff space (for instance profinite) and let $D$ be its underlying
set with the discrete topology. Let $\beta D$ be the set of ultrafilters on $D$, topologized
by the basis of sets $\widehat E=\{\mathfrak p\in\beta D: E\in\mathfrak p\}$ for $E\subset D$.

1. $\beta D$ is compact Hausdorff, the sets $\widehat E$ are clopen, and $D\to\beta D$,
   $d\mapsto$ (principal ultrafilter at $d$), has dense image.
2. $\beta D$ is extremally disconnected; hence (by [det-pe-stonean-projective]) it is
   profinite and projective.
3. The map $\pi\colon\beta D\to T$ sending $\mathfrak p$ to the unique limit in $T$ of the
   ultrafilter $\mathfrak p$ is continuous and surjective, and it extends the identity of
   the underlying set.
