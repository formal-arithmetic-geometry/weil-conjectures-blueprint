+++
id = "lemma-nagata-separated-descent-stage-exists"
kind = "lemma"
title = "Existence of a separated descent stage"
order = 367
lean = ["AlgebraicGeometry.Scheme.exists_isSeparated_pullback_snd"]
uses = ["def-nagata-finite-presentation-descent", "lemma-nagata-closed-immersion-stage-exists", "lemma-nagata-diagonal-base-change", "lemma-nagata-diagonal-finite-presentation", "lemma-nagata-finite-presentation-descends"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of schemes with affine
transition maps and limit $S$, and let $X\to S$ be separated. Let
$Y_\lambda\to S_\lambda$ be of finite presentation, with $S_\lambda$
quasi-compact and quasi-separated, such that
$X\cong Y_\lambda\times_{S_\lambda}S$ over $S$. Then the base change of
$Y_\lambda$ to some later stage is separated. In particular, if $X\to S$ is
also of finite presentation and
$X^{\mathrm{desc}}_{\lambda_{\mathrm{rel}}}\to S_{\lambda_{\mathrm{rel}}}$ is the finite-presentation descent model,
there is a later index $\lambda_{\mathrm{sep}}$ for which the descended
model is separated, remains of finite presentation, and has base change
canonically isomorphic to $X\to S$.

## Proof

Let $D$ be the diagonal of the finite-presentation descended model over
$S_{\lambda_{\mathrm{rel}}}$. It is of finite presentation by
[lemma-nagata-diagonal-finite-presentation]. By
[lemma-nagata-finite-presentation-descends], base change identifies
the source model with $X$. Under this identification,
[lemma-nagata-diagonal-base-change] identifies the base change of
$D$ with $\Delta_{X/S}$, which is a closed immersion because $X\to S$ is
separated. Apply
[lemma-nagata-closed-immersion-stage-exists] to $D$ and choose the
resulting index $\lambda_{\mathrm{sep}}$. The diagonal at that stage is
closed, so the corresponding descended morphism is separated. Its finite
presentation and its comparison isomorphism with $X$ are obtained by base
changing the finite-presentation descent data to this later stage.
