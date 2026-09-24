+++
id = "thm-zl-wme-deligne-estimate"
kind = "theorem"
title = "General $Rf_!$ weight theorem"
order = 4333
uses = ["def-weil-complex-weights", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "lem-zl-finite-pushforward", "lem-zl-open-closed-weight", "lem-zl-sheaves-to-complexes", "lem-zl-shriek-composition", "thm-zl-relative-line-step", "thm-zl-relative-noether"]
+++
For every separated finite-type morphism $f:X_0\to Y_0$ of separated
finite-type $k_0$-schemes and every constructible $\Qlb$-Weil complex
$K$ (in the coefficient categories of
[def-weil-pbc-qbar-category]),

$$
K\in D_{\le w}(X_0)\quad\Longrightarrow\quad Rf_!K\in D_{\le w}(Y_0),
$$

where $D_{\le w}$ is the complex-weight predicate of
[def-weil-complex-weights].

## Proof

By [lem-zl-sheaves-to-complexes], reduce first to a mixed
cohomology sheaf. Noetherian induction and the localization rule
[lem-zl-open-closed-weight] reduce to the source and target strata
of [thm-zl-relative-noether]. The finite first arrow
$\nu$ preserves the upper weight bound by
[lem-zl-finite-pushforward]; every subsequent affine-line
projection preserves it by [thm-zl-relative-line-step]. Repeated
use of the composition isomorphism [lem-zl-shriek-composition]
gives the bound for the whole factorization. The same localization
induction glues all strata and completes the proof.
