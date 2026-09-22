+++
id = "lem-fin-finite-constant-pushforward"
kind = "lemma"
title = "Finite pushforwards of constant sheaves"
order = 5161
lean = ["AlgebraicGeometry.Etale.isConstructible_pushforward_constant_of_isFinite"]
uses = ["sbc-def-coefficient-conventions"]
+++
Let $g:V\to S$ be finite with $S$ of finite type over $k$, and let $M$ be a
finite abelian group. Then $g_*\underline M$ is constructible on $S_{\Et}$.

## Proof

The finite constant abelian sheaf $\underline M$ is constructible. The
Noetherian finite-image theorem of the proper-base-change chapter therefore
applies directly. Its proof obtains a dense lisse open by an explicit
finite-algebra calculation, and treats the closed complement by Noetherian
induction and finite base change. In particular it does not infer that the
original finite morphism becomes étale merely by ignoring inseparable
contributions.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-finite-pushforward-constructible-noetherian, def:weil-pbc-etale-sheaves
