+++
id = "sbc-lem-smooth-criterion"
kind = "lemma"
title = "Smoothness by flatness and smooth fibres"
order = 1375
uses = ["def-sbc-smooth-morphisms"]
+++
A morphism $f:X\to Y$ of schemes is
smooth if and only if it is flat,
locally of finite presentation, and every fibre $X_y$ is smooth over
$\kappa(y)$.

## Proof

This is classical: smooth morphisms are flat and locally of finite presentation (Stacks Project, Lemmas 29.35.8 and 29.35.9, [Tag 01VE](https://stacks.math.columbia.edu/tag/01VE), [Tag 01VF](https://stacks.math.columbia.edu/tag/01VF)), have smooth fibres by base change (Lemma 29.35.5, [Tag 01VB](https://stacks.math.columbia.edu/tag/01VB)), and conversely flatness with local finite presentation and smooth fibres gives smoothness (Lemma 29.35.3, [Tag 01V8](https://stacks.math.columbia.edu/tag/01V8)), the two definitions of smoothness being identified by Lemma 37.11.7 ([Tag 02H6](https://stacks.math.columbia.edu/tag/02H6)); for morphisms of finite type this is the Jacobian criterion, Lemma 29.35.14 ([Tag 01V9](https://stacks.math.columbia.edu/tag/01V9)). No separate proof is given.
