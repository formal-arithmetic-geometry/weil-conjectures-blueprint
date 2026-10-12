+++
id = "lemma-weil-pbc-normalization-exact-sequence"
kind = "lemma"
title = "Normalization comparison exact sequence"
order = 1177
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-extension-by-zero", "def-weil-pbc-finite-open-comparison", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-eight-curve-devissage", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-pushforward-extension-zero", "thm-sc-main"]
+++
Let $X$ be a reduced curve over an algebraically closed field,
$\nu:X^\nu\to X$ its finite normalization, $j:U\hookrightarrow X$ open,
and $j^\nu:U^\nu\hookrightarrow X^\nu$ its pullback. For every prime
$\ell$, the unit and the finite-open comparison define a monomorphism

$$
\alpha:j_!\underline{\mathbf F_\ell}\longrightarrow
\nu_*j^\nu_!\underline{\mathbf F_\ell}
$$

whose cokernel $Q$ is constructible and supported on the finite nonnormal
locus. The sequence

$$
0\longrightarrow j_!\underline{\mathbf F_\ell}
\xrightarrow{\alpha}\nu_*j^\nu_!\underline{\mathbf F_\ell}
\longrightarrow Q\longrightarrow0
$$

and all its cohomology boundary maps commute with algebraically closed field
extension and restriction to opens.
