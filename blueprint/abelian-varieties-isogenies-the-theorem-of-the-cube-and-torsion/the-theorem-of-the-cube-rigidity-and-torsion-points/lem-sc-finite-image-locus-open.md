+++
id = "lem-sc-finite-image-locus-open"
kind = "lemma"
title = "Finiteness of the image is an open condition on the parameter"
order = 4015
lean = ["AlgebraicGeometry.exists_isOpen_finite_image"]
+++
Let $k$ be a field, $X$ a $k$-scheme proper over $k$, $Z$ a $k$-scheme
separated and locally of finite type over $k$, $Y$ a $k$-scheme,
$f:X\times_kY\to Z$ a morphism and $y_0\in Y(k)$. If
$f(X\times_k\{y_0\})$ is finite, then there is an open neighbourhood
$U\subseteq Y$ of $y_0$ such that $f(X\times_k\{y\})$ is finite for every
$y\in U$.

## Proof

Apply Stacks Project, More on Morphisms, Lemma 37.44.3 ([Tag
0AH8](https://stacks.math.columbia.edu/tag/0AH8)) to the commutative
triangle over $S:=Y$ formed by the two morphisms
$p=\operatorname{pr}_2:X\times_kY\to Y$,
$q=\operatorname{pr}_2:Z\times_kY\to Y$ and
$h=(f,p):X\times_kY\to Z\times_kY$, so that $q\circ h=p$. The hypotheses of
loc. cit. hold at $s=y_0$: $p$ is the base change of the proper morphism
$X\to\Spec k$, hence proper; $q$ is separated (it is the base change of
$Z\to\Spec k$, which is separated) and locally of finite type (the base
change of $Z\to\Spec k$, which is locally of finite type); and the fibre
$X_{y_0}=X\times_k\{y_0\}$ has image $f(X\times_k\{y_0\})$ in
$Y_{y_0}=Z\times_k\{y_0\}\cong Z$, which is finite by hypothesis. Loc. cit.
therefore gives an open $U\ni y_0$ and a closed subscheme
$W\subseteq Z\times_kU$ finite over $U$ such that $h|_{X\times_kU}$ factors
through $W$. For $y\in U$ the set $f(X\times_k\{y\})$ is contained in the
fibre $W_y$, which is finite over $\kappa(y)$; hence $f(X\times_k\{y\})$ is
finite.
