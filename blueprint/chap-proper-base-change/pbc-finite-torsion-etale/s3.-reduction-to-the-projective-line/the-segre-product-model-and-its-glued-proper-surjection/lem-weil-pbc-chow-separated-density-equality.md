+++
id = "lem-weil-pbc-chow-separated-density-equality"
kind = "lemma"
title = "Agreement on a dense open, for a separated target"
order = 1578
uses = ["def-weil-pbc-chow-scheme-theoretic-closure", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-closed-immersion-products"]
+++
Let $Z$ be a scheme, $U\subseteq Z$ a scheme-theoretically dense
([def-weil-pbc-chow-scheme-theoretic-closure]) open subscheme, and $f,g:Z\to
X$ two morphisms into a separated scheme $X$ with $f|_U=g|_U$. Then $f=g$.

## Proof

The equalizer $E$ of $f$ and $g$ is the inverse image of the diagonal of $X$
under $(f,g):Z\to X\times X$; as $X$ is separated, the diagonal is a closed
immersion, and closed immersions are stable under base change, so $E\subseteq
Z$ is a closed subscheme. It contains $U$, which is scheme-theoretically dense
in $Z$ by [def-weil-pbc-chow-scheme-theoretic-closure]; hence $E=Z$, i.e.
$f=g$. (This is Stacks Project, Morphisms, Lemma 29.7.10, Tag
[01RH](https://stacks.math.columbia.edu/tag/01RH).)
