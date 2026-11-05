+++
id = "example-finite-direct-image-double-cover"
kind = "example"
title = "A ramified double cover"
order = 387
+++
Let $k$ be algebraically closed of characteristic $\neq2$, let
$u:\mathbf A^1_k\to\mathbf A^1_k$ be $x\mapsto x^2$, and let $A$ be a finite
ring. Over a point $t\neq0$ the fibre consists of the two points
$\pm\sqrt t$, whereas over $t=0$ it is the single point $x=0$, with a nonreduced
structure that the étale topology does not see. By Lemma [lemma-finite-direct-images], therefore,

$$
(u_*A)_{\bar t}=A\oplus A\quad(t\neq0),\qquad (u_*A)_{\bar0}=A,
$$

and the rank of the stalks jumps at the origin, so $u_*A$ is not lisse. It is,
however, constructible for the stratification $\mathbf G_m\sqcup\{0\}$. Base
change to the origin gives the stalk $A$, the cohomology of the fibre, as
Lemma [lemma-finite-morphisms] predicts. For the open immersion $j:\mathbf G_m\to\mathbf A^1$,
by contrast, the stalk of $j_*A$ at $0$ is $A$ while the fibre is empty.
