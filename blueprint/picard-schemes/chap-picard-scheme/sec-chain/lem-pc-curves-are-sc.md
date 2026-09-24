+++
id = "lem-pc-curves-are-sc"
kind = "lemma"
title = "Curves in the sense of file 06"
order = 2616
uses = ["def-pc-curve", "def-pc-dimension", "def-pc-smooth-projective-curve", "def-sc-curves", "lem-sc-base-change-curve", "prop-pc-xk-integral"]
+++
Let $k$ be a field and let $X$ be a
smooth projective curve over
$k$. Then $X$ is a *curve over $k$* in the sense of
[def-sc-curves]: $X$ is nonempty, separated, of finite type over
$k$ and of dimension $\le1$, and smooth over $k$.

## Proof

By [def-pc-smooth-projective-curve] $X$ is a
curve over $k$, hence a
variety: integral, with
$X\to\operatorname{Spec}(k)$ separated and of finite type ([def-pc-curve]); in
particular $X$ is nonempty, separated, of finite type and, being a
curve, of dimension $1$. Its structure morphism is smooth by hypothesis,
and
[def-sc-curves] requires exactly: nonempty, separated scheme of
finite type of dimension $\le1$, smooth over $k$. This proves the
claim. (The same applies to base changes $X_K$: see
[lem-sc-base-change-curve] and [prop-pc-xk-integral].)
