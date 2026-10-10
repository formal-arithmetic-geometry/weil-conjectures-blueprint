+++
id = "lemma-nagata-conrad-quasi-domination-proper-target"
kind = "lemma"
title = "A quasi-domination over a proper target is everywhere defined (Conrad)"
order = 223
uses = ["def-nagata-conrad-quasi-domination"]
+++
Let $Y\to S$ be proper and let $(U,f)$ be a quasi-domination of $X$ over
$Y$. Then $U=X$; that is, $f$ extends to an $S$-morphism $X\to Y$.

## Proof

The projection $X\times_SY\to X$ is proper, being a base change of
$Y\to S$. The graph $\Gamma_f$ is a closed subscheme of $X\times_SY$ by
hypothesis, so its image in $X$ is closed. That image is $U$, because
$\Gamma_f\to U$ is an isomorphism. Thus $U$ is a closed subset of $X$
which is also dense and open, so $U=X$. Under the resulting isomorphism
$\Gamma_f\cong X$ the second projection is the desired extension.
