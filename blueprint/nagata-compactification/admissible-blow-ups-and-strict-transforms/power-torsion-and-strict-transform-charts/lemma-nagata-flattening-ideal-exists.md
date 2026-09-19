+++
id = "lemma-nagata-flattening-ideal-exists"
kind = "lemma"
title = "Flattening ideal with an open strict transform, [stacks-project]"
order = 374
uses = ["def-nagata-strict-transform", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-cartier-boundary-preparation", "lemma-nagata-flat-strict-transform-open", "lemma-nagata-flattening-after-cartier-boundary", "lemma-nagata-strict-transform-dominating"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be separated and of finite type, let $X$ be qcqs,
and let $U\subseteq X$ be a quasi-compact open. Fix an isomorphism
$e_U\colon q^{-1}(U)\xrightarrow{\sim}U$ over $U$. There exists a finite type
quasi-coherent ideal $\mathcal F\subseteq\mathcal O_X$ satisfying
$\mathcal F|_U=\mathcal O_U$ such that, after blowing up $\mathcal F$, the
strict-transform projection

$$
\operatorname{ST}_{\operatorname{Bl}_{\mathcal F}(X)/X}(Z)
\longrightarrow \operatorname{Bl}_{\mathcal F}(X)
$$

is an open immersion and restricts over $U$ to $e_U$.

## Proof

Apply [lemma-nagata-cartier-boundary-preparation] to obtain a
$U$-admissible blow-up $X_1\to X$ with Cartier boundary. The transported
isomorphism over $U$ identifies the strict transform $Z_1\to X_1$ with the
original partial isomorphism. Apply
[lemma-nagata-flattening-after-cartier-boundary] to get a second
$U$-admissible blow-up $X_2\to X_1$ for which the strict transform
$Z_2\to X_2$ is flat and finitely presented. The preserved open is dense
after both steps by
[lemma-nagata-admissible-blowup-preserves-density], and strict
transforms identify with the direct strict transform by
[lemma-nagata-strict-transform-dominating]. The flat-partial-isomorphism
lemma makes $Z_2\to X_2$ an open immersion. Finally,
[lemma-nagata-admissible-blowup-comp] identifies the composite with the
blow-up of a single finite-type ideal $\mathcal F$ that is the unit on $U$;
transporting the open immersion and its restriction gives the required
witness.
