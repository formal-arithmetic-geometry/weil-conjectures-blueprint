+++
id = "sk-prop-av-image-open"
kind = "section"
title = "Finiteness of the image is open in the parameter"
order = 490
uses = ["sk-def-av"]
+++
*Proposition (sketch).*

Let $X$ be proper over $k$, $Z$ separated and locally of finite type
over $k$, $f:X\times_kY\to Z$ a morphism and $y_0\in Y(k)$. If
$f(X\times_k\{y_0\})$ is finite, then $f(X\times_k\{y\})$ is finite for
all $y$ in an open neighbourhood of $y_0$.

## Proof

Apply `0AH8` to the triangle over $S=Y$ formed by
$p=\mathrm{pr}_2:X\times_kY\to Y$, $q=\mathrm{pr}_2:Z\times_kY\to Y$
and $h=(f,p)$. Here $p$ is proper (base change of $X\to\Spec k$) and
$q$ is separated and locally of finite type, and the fibre over $y_0$
has finite image by hypothesis; loc. cit. gives an open
$U\ni y_0$ and a closed subscheme $W\subseteq Z\times_kU$ finite over
$U$ through which $h$ factors, so $f(X\times_k\{y\})\subseteq W_y$ is
finite for every $y\in U$.

Uses: [sk-def-av]
