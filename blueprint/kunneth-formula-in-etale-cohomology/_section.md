+++
id = "kunneth-formula-in-etale-cohomology"
kind = "section"
title = "Künneth formula in étale cohomology"
order = 6000
+++
The Künneth formula in étale cohomology, **without any properness
assumption**.

This chapter decomposes Stacks Project Section 59.97 ("Künneth in étale
cohomology", [Tag 0F13](https://stacks.math.columbia.edu/tag/0F13)) into
blueprint items and proves the general Künneth formula (Lemma 59.97.9, [Tag
0F1P](https://stacks.math.columbia.edu/tag/0F1P)) over a separably closed
field: for schemes $X,Y$ of finite type over $k$ and $n$ invertible in $k$,
the Künneth map for $X\times_kY$ is an isomorphism for arbitrary bounded —
in fact unbounded — complexes of $\mathbf Z/n\mathbf Z$-module sheaves, with
**no properness hypothesis** on $X$ or $Y$. The one-proper-factor case (Tag
0F14) is decomposed first and used repeatedly; the general case follows the
Stacks route: base change for open immersions (0F1H), base change towards
spectra of fields (0F1I), the derived projection-formula variant (0F1J), and
the removal of boundedness (0F1N), then the assembled statement 0F1P.

*Conventions and reuse.* The ambient machinery — the small étale site and
its sheaves, geometric stalks, derived categories, K-injective resolutions,
étale cohomology, direct and inverse image, cartesian squares, the exchange
morphisms, proper base change, continuity along affine limits, the finite
morphism facts, constructible approximations, the strict henselization as a
limit, the spectral-sequence machinery, and classical smooth base change —
is referenced, not redefined. The genuinely new items are: the derived
tensor product and tor amplitude on the small étale site, the Künneth map
and the relative cup product, the cohomological dimension and base-change
predicates, and a ladder of Stacks inputs (stated as decomposed statements
with intentionally omitted proofs, each carrying its Stacks tag).

*Status.* The final Künneth theorem [thm-kun-0F1P] and its proof were
decomposed first; the displayed order was then normalized so that every
dependency precedes its use. Every statement carrying a *Source:* note is an
input from the Stacks Project: its statement is fully decomposed but its
proof is intentionally omitted, in accordance with the opt-in rule for proof
decomposition. Claims that are basic commutative or homological algebra are
used directly.

*Import note.* The source defines several macros local to this chapter
(kunZn, kunFl, kunotimes, kunsupp, kuncd, kundim, pr, Ob). They are expanded inline here, so that no chapter-local macro is
needed in `blueprint.toml`.
