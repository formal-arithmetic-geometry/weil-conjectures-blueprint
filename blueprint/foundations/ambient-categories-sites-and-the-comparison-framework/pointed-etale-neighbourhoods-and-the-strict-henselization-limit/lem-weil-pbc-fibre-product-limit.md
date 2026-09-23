+++
id = "lem-weil-pbc-fibre-product-limit"
kind = "lemma"
title = "Fiber products commute with the neighborhood limit"
order = 1295
uses = ["def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit-detailed"]
+++
If $f:X\to S$ is quasi-compact and quasi-separated
[def-weil-pbc-scheme-conventions], then

$$
 X\times_SS_{(\bar s)}\xrightarrow{\sim}
 \varprojlim_{(V,\bar v)}X\times_SV.
$$

## Proof

On affine charts, tensor products commute with filtered colimits, and
quasi-compactness gives finitely many charts while quasi-separatedness gives
quasi-compact pairwise intersections; the affine identifications glue to the
displayed identification of
[def-weil-pbc-strict-henselization-limit-detailed].
