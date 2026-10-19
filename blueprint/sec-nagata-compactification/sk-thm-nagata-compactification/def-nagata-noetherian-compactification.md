+++
id = "def-nagata-noetherian-compactification"
kind = "definition"
title = "Recursive Noetherian compactification construction"
order = 331
lean = ["AlgebraicGeometry.noetherianCompactificationConstruction", "AlgebraicGeometry.noetherianCompactification"]
uses = ["def-nagata-affine-compactification", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-dense-affine-cover", "def-nagata-partial-affine-unions", "def-nagata-two-open-compactification-candidate", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-nagata-final-density", "lemma-nagata-partial-union-overlap-dense", "lemma-nagata-two-open-candidate-proper", "lemma-nagata-two-open-valuative-lifting", "prop-nagata-affine-compactification", "thm-nagata-two-open"]
+++
Let $S$ be Noetherian, let $f\colon X\to S$ be separated and of finite
type, and let $U_1,\ldots,U_n$ be affine opens of $X$ whose total
intersection $U_1\cap\cdots\cap U_n$ is dense in $X$ (for instance the
selected dense affine cover $\mathcal U_X$ of
[def-nagata-dense-affine-cover]). With $X_r$ the partial unions of
[def-nagata-partial-affine-unions], define for every $r\in\mathbb N$ a
compactification $\mathsf C_r$ of $X_r\to S$ in the sense of
[def-nagata-compactification], recursively on $r$; at each stage
$\mathsf C_r$ is a chosen compactification of $X_r\to S$, whose existence
is supplied as follows.

1. $X_0=\emptyset$, so $X_0\to S$ is proper and compactifies itself.
1. If $r\geq n$ then $X_{r+1}=X_r$, which has the compactification
$\mathsf C_r$.
1. $X_1=U_1$ is affine, and [prop-nagata-affine-compactification]
compactifies it.
1. If $1\leq r<n$, apply [thm-nagata-two-open] to the open cover
$X_{r+1}=X_r\cup U_{r+1}$, using the compactification $\mathsf C_r$ of
$X_r$, the affine compactification of $U_{r+1}$ from
[prop-nagata-affine-compactification], and the dense overlap from
[lemma-nagata-partial-union-overlap-dense].

Finally define

$$
\mathsf C_{\mathrm{Noeth}}(X/S)=\mathsf C_n .
$$

Since $S$ is Noetherian and $X\to S$ is of finite type, $X$ is Noetherian,
hence quasi-compact and quasi-separated, and the finite generic-point
argument of [def-nagata-dense-affine-cover] supplies such a family covering
$X$. At every stage $X_r\to S$ is separated and of finite type, by
restricting the corresponding properties of $X\to S$ to the open
$X_r\subseteq X$ (a finite union of affine opens, hence quasi-compact);
these are the hypotheses used at the next application of
[thm-nagata-two-open].
