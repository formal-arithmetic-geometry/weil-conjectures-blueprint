+++
id = "pqf-lem-limit-iso-descends"
kind = "lemma"
title = "Isomorphisms spread out from a filtered limit with closed immersions"
order = 2025
uses = ["def-weil-pbc-scheme-conventions", "pqf-lem-limit-immersion-descends", "pqf-lem-limit-qc-open-descends"]
+++
Let $S$ be a scheme and let $X=\varprojlim_{i\in I}X_i$ be a filtered
limit of $S$-schemes with affine transition morphisms such that every
$X_i$ is quasi-compact and
locally of finite type over $S$, and such that every transition morphism
$X_{i'}\to X_i$ is a closed immersion. If $X\to S$ is locally of
finite presentation, then the projection $X\to X_i$ is an isomorphism for
all sufficiently large $i$.
(*Stacks Project, Limits of Schemes, Lemma 32.4.16 (3), Tag
[081B](https://stacks.math.columbia.edu/tag/081B); recorded classical
input, quoted verbatim in the source note of this section.*)

## Proof

This is Limits of Schemes, Lemma 32.4.16 (3), Tag
[081B](https://stacks.math.columbia.edu/tag/081B), whose statement is
quoted verbatim in the source note of this section; it is recorded here as
the classical input it is, in the form used below, exactly as
[pqf-lem-limit-qc-open-descends] and
[pqf-lem-limit-immersion-descends] record Tags 01Z4 and 081B (1) and
prove their scheme-theoretic content. The Stacks Project derives it by
working affine locally on $X_0$ for some $0\in I$, as in the proof of
[pqf-lem-limit-immersion-descends], and reducing to the affine
statement that a directed colimit of quotients of a fixed algebra, with
surjective transition maps, whose colimit is of finite presentation over
the algebra it is a quotient of, stabilizes; that algebra statement is
elementary, as the said proof shows, and we use only the scheme-theoretic
statement quoted above.
