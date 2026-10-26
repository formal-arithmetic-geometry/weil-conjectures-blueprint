+++
id = "det-pe-stonean-projective"
kind = "lemma"
title = "Gleason: extremally disconnected equals projective"
lean = ["CompactT2.projective_iff_extremallyDisconnected", "CompactT2.Projective", "ExtremallyDisconnected", "CompHaus.Gleason"]
order = 895
+++
Let $S$ be a compact Hausdorff space. The following are equivalent.

1. $S$ is extremally disconnected: for every open $U\subset S$, the closure
   $\overline U$ is open.
2. $S$ is projective for continuous surjections of compact Hausdorff spaces: for every
   continuous surjection $p\colon X\to Y$ of compact Hausdorff spaces and every continuous
   $f\colon S\to Y$ there is a continuous $g\colon S\to X$ with $p\circ g=f$.
3. Every continuous surjection $q\colon P\to S$ from a compact Hausdorff space $P$ has a
   continuous section.

Moreover an extremally disconnected compact Hausdorff space is totally disconnected, hence
profinite.
