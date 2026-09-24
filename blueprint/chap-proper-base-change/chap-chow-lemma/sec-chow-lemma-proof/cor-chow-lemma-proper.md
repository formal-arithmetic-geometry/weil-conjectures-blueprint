+++
id = "cor-chow-lemma-proper"
kind = "theorem"
title = "Chow's lemma for proper morphisms"
order = 630
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpace"]
tags = ["latex:corollary"]
uses = ["def-nagata-projective-space-base-change", "lemma-nagata-projective-space-base-change-proper", "thm-chow-lemma"]
+++
Let $S$ be a noetherian scheme and let $f\colon X\to S$ be a proper morphism.
Then there are an integer $n\geq0$, a proper surjective morphism
$\pi\colon X'\to X$ and a *closed* immersion
$i\colon X'\to\mathbf P^n_S$ of $S$-schemes; moreover $\pi$ is an isomorphism
over a dense open subscheme of $X$. In particular every proper $S$-scheme is
dominated by a projective $S$-scheme through a proper surjective morphism.

## Proof

A proper morphism is separated and of finite type, so [thm-chow-lemma]
applies and yields $\pi\colon X'\to X$ and an immersion
$i\colon X'\to\mathbf P^n_S$ with the stated properties. Both $f$ and $\pi$
are proper, hence so is $f\circ\pi\colon X'\to S$. Since $\mathbf P^n_S\to S$
is separated, 01W6 shows that $i$ is universally closed; in
particular $i(X')\subseteq\mathbf P^n_S$ is closed, and an immersion with
closed image is a closed immersion by 01IQ. Thus $f\circ\pi$
is the composition of the closed immersion $i$ with the structure morphism
$\mathbf P^n_S\to S$, so $X'$ is projective over $S$.
