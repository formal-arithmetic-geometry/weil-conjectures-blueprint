+++
id = "lem-weil-pbc-direct-image-filtered-colimit"
kind = "lemma"
title = "Filtered colimits and higher direct image"
order = 1352
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-qcqs-higher-direct-image"]
+++
If $u:U\to V$ is quasi-compact and quasi-separated
[def-weil-pbc-scheme-conventions] and $(F_i)$ is a filtered system of torsion
etale sheaves [def-weil-pbc-etale-sheaves], then for every $q\geq0$ the
canonical map

$$
 \varinjlim_iR^qu_*F_i\xrightarrow{\sim}R^qu_*(\varinjlim_iF_i)
$$

involving the higher direct image [def-weil-pbc-direct-image] is an
isomorphism. The same assertion holds after arbitrary base change.

## Proof

The higher direct image of [def-weil-pbc-direct-image] is the sheafification
of $W\mapsto H^q(W\times_VU,F|)$ by
[lem-weil-pbc-qcqs-higher-direct-image], the morphism $u$ being quasi-compact
and quasi-separated.

Use the basis of affine etale $W\to V$. Then $W\times_VU$ is quasi-compact
and quasi-separated, so [lem-weil-pbc-cohomology-filtered-colimit] applies to
the displayed presheaf on every basis object. Inverse image to $W\times_VU$
commutes with filtered colimits. Finally, sheafification preserves colimits,
and filtered colimits are exact. Sheafifying the resulting isomorphisms
proves the assertion. Quasi-compactness and quasi-separatedness are preserved
by base change, so this argument also proves the last sentence.
