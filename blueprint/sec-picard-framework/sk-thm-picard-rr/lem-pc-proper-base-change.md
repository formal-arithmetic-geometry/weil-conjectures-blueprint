+++
id = "lem-pc-proper-base-change"
kind = "lemma"
title = "Proper and smooth morphisms are stable under base change"
lean = ["AlgebraicGeometry.isProper_and_smooth_of_isPullback"]
order = 730
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-pc-scheme", "def-weil-scheme-morphism-properties"]
+++
Let $f:X\to S$ be a proper morphism, let $g:S'\to S$ be arbitrary, and
let $f':X'=X\times_SS'\to S'$ be the base change. Then $f'$ is
proper. If $f$ is smooth, then $f'$ is smooth.
