+++
id = "sk-prop-av-const-locus"
kind = "proposition"
title = "The locus of constant fibres is closed"
lean = ["AlgebraicGeometry.isClosed_setOf_subsingleton_image"]
order = 491
uses = ["sk-def-av"]
tags = ["sketch"]
+++
Let $X$ be a $k$-scheme proper over $k$, $Z$ separated over $k$, $Y$ a
$k$-scheme and $f:X\times_kY\to Z$ a morphism of $k$-schemes. For $y\in Y$ let
$\bar y:\Spec\overline{\kappa(y)}\to Y$ be a geometric point over $y$
and $f_{\bar y}:X_{\overline{\kappa(y)}}\to Z_{\overline{\kappa(y)}}$
the base change of $(f,\mathrm{pr}_2):X\times_kY\to Z\times_kY$ along
$\bar y$. Then

$$
L:=\{y\in Y: f_{\bar y}(X_{\overline{\kappa(y)}})\ \text{consists of at most one point}\}
$$

is closed in $Y$. (For $X$ nonempty, "at most one point" means "a
single point". Constancy must be tested on the geometric fibre: for
$X=\Spec k\sqcup\Spec k$, $Y=Z=\mathbf A^1_k$, $k$ algebraically closed
of characteristic $\ne2$ and $f=(t\mapsto t,\ t\mapsto-t)$, the
set-theoretic image of the fibre over $y$ is one point exactly for $y$ the
generic point or $y=0$, which is not closed.)
