+++
id = "the-finite-presentation-stage-of-the-descent"
kind = "section"
title = "The finite-presentation stage of the descent"
order = 3248
+++
The finite-presentation refinement of Zariski's main theorem, Stacks
Project, More on Morphisms, Lemma 37.43.4 ([Tag
0F2N](https://stacks.math.columbia.edu/tag/0F2N)), is proved here
[pqf-thm-zmt-fp] from the isomorphism-spreading lemma
[pqf-lem-limit-iso-descends]; [pqf-rem-fp-stage-status] records exactly
which clause of the interface [thm-pqf-immersion-descent] this settles and
which it does not.

*Source note (19 September 2026).* Every page quoted below was fetched and
read verbatim on that date.

Stacks Project, Limits of Schemes, Lemma 32.9.8, [Tag
09YY](https://stacks.math.columbia.edu/tag/09YY): "Let $f:X\to S$ be a
morphism of schemes. Assume (1) $f$ is finite, and (2) $S$ quasi-compact
and quasi-separated. Then $X$ is a directed limit $X=\lim X_i$ where the
transition maps are closed immersions and the objects $X_i$ are finite and
of finite presentation over $S$." Stacks' proof: write $X=\lim X_i$ as in
Limits of Schemes, Lemma 32.9.5, [Tag
09ZQ](https://stacks.math.columbia.edu/tag/09ZQ) ("$f$ locally of finite
type, $X$ quasi-compact and quasi-separated, $S$ quasi-separated" give
"$X=\lim X_i$ where the $X_i\to S$ are of finite presentation, the $X_i$
are quasi-compact and quasi-separated, and the transition morphisms
$X_{i'}\to X_i$ are closed immersions"), and then apply Limits of Schemes,
Lemma 32.4.19, [Tag 09ZN](https://stacks.math.columbia.edu/tag/09ZN) ("$S$
quasi-compact and quasi-separated, $X_i$ quasi-compact and quasi-separated,
the transition morphisms $X_{i'}\to X_i$ finite, $X_i\to S$ locally of
finite type, $X\to S$ integral" give "$X_i\to S$ is finite for $i$ large
enough"), which makes the stages finite.

Stacks Project, Limits of Schemes, Lemma 32.4.16 (3), [Tag
081B](https://stacks.math.columbia.edu/tag/081B): "If $Y\to X$ is an
isomorphism, $X_i$ quasi-compact, $X_i\to S$ locally of finite type, the
transition morphisms $X_{i'}\to X_i$ are closed immersions, and $Y\to S$ is
locally of finite presentation, then $Y\to X_i$ is an isomorphism for $i$
large enough."

Stacks Project, More on Morphisms, Lemma 37.43.4, [Tag
0F2N](https://stacks.math.columbia.edu/tag/0F2N): "With notation and
hypotheses as in Lemma 37.43.3. Assume moreover that $f$ is locally of
finite presentation. Then we can choose the factorization such that $T$ is
finite and of finite presentation over $S$."

*Why Tag 09YY does not apply to the presentation of the
finite-approximation tail.* That presentation has
$N_f=\varprojlim_\lambda T_\lambda$ with
$T_\lambda=\operatorname{Spec}_S\mathcal A_\lambda$ finite over $S$, so the
*objects* have the property the tag asks of its limit stages; but its
transition morphisms $T_\mu\to T_\lambda$ are dual to the injective algebra
maps $\mathcal A_\lambda\hookrightarrow\mathcal A_\mu$, hence are affine
and dominant, and they are closed immersions only when
$\mathcal A_\lambda=\mathcal A_\mu$ — exactly the condition the tag imposes
on its transition maps. Hypothesis (1) of the tag fails as well: the
morphism whose stages are being approximated is $\nu_f:N_f\to S$, which is
integral and not known to be finite at that point of the argument
(finiteness of the factorization scheme is what is being proved). The
affine-transition-map analogue of Tag 09YY is Limits of Schemes, Lemma
32.4.19, [Tag 09ZN](https://stacks.math.columbia.edu/tag/09ZN), whose
conclusion is only that the stages are finite over $S$ — a fact that Step 2
of the proof of [thm-pqf-zmt-factorization] already supplies — and not that
they are finitely presented. What Tag 09YY does apply to is the *finite*
morphism $T_0\to S$ of clause (i) of [thm-pqf-immersion-descent], and that
is how the finite-presentation clause is obtained in [pqf-thm-zmt-fp].

The three finite-presentation lemmas of the ambient-foundations chapter
(`lem:weil-pbc-finite-refinement-etale-cover`, Stacks Project Tag 09Z0;
`lem:weil-pbc-etale-finite-data-descent`;
`lem:weil-pbc-etale-section-continuity`) descend finite-presentation *data*
of etale $X$-schemes, and sections of sheaves on them, to a stage of a
limit of quasi-compact quasi-separated schemes. They concern neither the
finiteness of the stages $T_\lambda$ of the normalization nor their finite
presentation, and they supply nothing for clause (ii).
