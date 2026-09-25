+++
id = "lem-zl-quasi-finite"
kind = "lemma"
title = "Quasi-finite upper-weight bound"
order = 3023
uses = ["def-weil-complex-weights", "def-weil-pbc-qbar-category", "lem-zl-finite-pushforward", "lem-zl-open-closed-weight", "thm-pqf-zmt-factorization"]
+++
If $g:Z_0\to Y_0$ is separated and quasi-finite and
$K\in D_{\le w}(Z_0)$, then $Rg_!K\in D_{\le w}(Y_0)$.

## Proof

By Zariski's main theorem – the standard factorization of a separated
quasi-finite morphism as an open immersion followed by a finite
morphism, [thm-pqf-zmt-factorization] of the quasi-finite chapter – the
morphism $g$ factors locally on the target as

$$
Z_0\xrightarrow{\ j_0\ }\overline Z_0\xrightarrow{\ \bar g\ }Y_0
$$

with $j_0$ an open immersion and $\bar g$ finite; by the composition
isomorphism the assertion for $g$ follows from the assertion for the
two pieces. For $j_0$: extension by zero has the same stalks as
$K$ on $Z_0$ and stalk zero outside (the extension-by-zero rule),
so $j_{0!}K\in D_{\le w}(\overline Z_0)$; for $\bar g$: the finite
pushforward bound of [lem-zl-finite-pushforward] applies. The
local factorizations are glued by the localization induction of
[lem-zl-open-closed-weight] (the target devissage of an open–closed
decomposition), which completes the proof.
