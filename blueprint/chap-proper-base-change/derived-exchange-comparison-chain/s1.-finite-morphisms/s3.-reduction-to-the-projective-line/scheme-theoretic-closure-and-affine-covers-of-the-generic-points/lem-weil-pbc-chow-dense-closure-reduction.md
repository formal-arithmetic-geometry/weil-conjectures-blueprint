+++
id = "lem-weil-pbc-chow-dense-closure-reduction"
kind = "lemma"
title = "Reduction to scheme-theoretically dense opens"
order = 1476
uses = ["def-weil-pbc-chow-scheme-theoretic-closure", "def-weil-pbc-scheme-conventions"]
+++
Let $X$ be quasi-compact and let $U\subseteq X$ be a dense open subscheme. Let
$X^{*}\subseteq X$ be the scheme-theoretic closure of $U\to X$ in the sense of
[def-weil-pbc-chow-scheme-theoretic-closure]. Then $X^{*}\to X$ is a
surjective closed immersion, an isomorphism over $U$, and $U$ is
scheme-theoretically dense in $X^{*}$. If moreover $X=U_1\cup\dots\cup U_m$ is
a finite affine open cover and $U_i^{*}:=X^{*}\cap U_i$, then each $U_i^{*}$
is affine and $U_1^{*}\cap\dots\cap U_m^{*}=U$.

## Proof

By [def-weil-pbc-chow-scheme-theoretic-closure], $X^{*}\to X$ is a closed
immersion. Its image is a closed subset containing $U$, whose underlying set
is dense in $X$; hence the image is all of $X$, i.e. $X^{*}\to X$ is
surjective. The ideal sheaf of $X^{*}$ in $X$ is $\ker(\mathcal O_X\to
u_*\mathcal O_U)$ where $u:U\to X$; its restriction to the open $U$ is
$\ker(\mathcal O_U\to\mathcal O_U)=0$, so $X^{*}\cap U=U$: the closed
immersion is an isomorphism over $U$. By definition the scheme-theoretic image
of $U\to X^{*}$ is $X^{*}$, i.e. $U$ is scheme-theoretically dense in $X^{*}$.
Each $U_i^{*}$ is a closed subscheme of the affine scheme $U_i$, and a closed
subscheme of an affine scheme is affine, so $U_i^{*}$ is affine; and

$$
 U_1^{*}\cap\dots\cap U_m^{*}=X^{*}\cap U_1\cap\dots\cap U_m
 =X^{*}\cap U=U,
$$

the last equality because $U\subseteq X^{*}$.
