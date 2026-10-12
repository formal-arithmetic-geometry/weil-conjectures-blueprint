+++
id = "lem-sc-constant-locus-closed"
kind = "lemma"
title = "The locus of parameters with constant fibre is closed"
lean = ["AlgebraicGeometry.isClosed_setOf_subsingleton_image"]
order = 492
+++
Let $k$ be a field, $X$ a $k$-scheme proper over $k$, $Z$ a
$k$-scheme separated over $k$, $Y$ a $k$-scheme and
$f:X\times_kY\to Z$ a morphism of $k$-schemes. For $y\in Y$ let
$\bar y:\Spec\overline{\kappa(y)}\to Y$ be a geometric point over $y$
(an algebraic closure of $\kappa(y)$) and let

$$
f_{\bar y}:X_{\overline{\kappa(y)}}\longrightarrow Z_{\overline{\kappa(y)}}
$$

be the base change of $(f,\operatorname{pr}_2):X\times_kY\to Z\times_kY$
along $\bar y$. Then

$$
L:=\{y\in Y: f_{\bar y}(X_{\overline{\kappa(y)}})\ \text{consists of at most one point}\}
$$

is closed in $Y$.

For $X$ nonempty, $f_{\bar y}(X_{\overline{\kappa(y)}})$ consists of at
most one point exactly when it is a single point. Constancy has to be
measured on the geometric fibre, not by the set-theoretic image
$f(\operatorname{pr}_2^{-1}(y))\subseteq Z$: for $k$ algebraically closed
of characteristic $\ne2$, $X=\Spec k\sqcup\Spec k$, $Y=Z=\mathbf A^1_k$
and $f$ given by $t\mapsto t$ on the first copy and $t\mapsto -t$ on the
second, the set $f(\operatorname{pr}_2^{-1}(y))$ is a single point exactly
when $y$ is the generic point or $y=0$, and this set is not closed. With
the definition above, $L=\{0\}$.
