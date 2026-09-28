+++
id = "lem-sc-rigidity"
kind = "lemma"
title = "The rigidity lemma"
lean = ["AlgebraicGeometry.exists_eq_snd_comp"]
order = 490
uses = ["lem-sc-constant-locus-closed", "lem-sc-finite-image-locus-open"]
+++
Let $X,Y,Z$ be schemes over $k$ with $X$ proper, connected and
reduced over $k$, $Y$ connected and $Z$ separated over $k$,
and let $f:X\times_kY\to Z$ be a morphism such that
$f(X\times\{y_0\})$ is a single point for some $k$-point
$y_0\in Y(k)$. Then $f$ factors through the projection
$X\times_kY\to Y$: there is a morphism $g:Y\to Z$ with
$f=g\circ\operatorname{pr}_2$.

## Proof

*Recorded classical input: Milne, Abelian Varieties, Ch. I (the
rigidity lemma); Mumford, Abelian Varieties, II.6.* We prove the
elementary half of the argument in full and mark the remaining step as
the recorded input. The reducedness hypothesis on $X$ cannot be
dropped: for $\operatorname{char}k=p>0$, with
$X=\alpha_p=\Spec k[x]/(x^p)$ (proper and connected but not reduced),
$Y=Z=\mathbf A^1_k$ and $f(x,y)=y+x$, the set
$f(X\times\{0\})=\{0\}$ is a single point, yet $f$ does not factor
through $\mathbf A^1_k\to\mathbf A^1_k$ (the morphism $f$ is not the
pullback of any morphism of the $y$-line).

*Step 1: the locus of constant fibres is closed.* Put

$$
L:=\{y\in Y: f(X\times_k\{y\})\ \text{is a single point}\}.
$$

By [lem-sc-constant-locus-closed] applied to $X$, $Z$ and
$f$, the set $L$ is closed in $Y$. It is nonempty, since
$y_0\in L$ by hypothesis.

*Step 2: the locus of constant fibres is open, when $Z$ is
locally of finite type over $k$.* Let $y\in L$, so that
$f(X\times_k\{y\})$ is finite. By
[lem-sc-finite-image-locus-open] (whose sole input is Stacks
Project, More on Morphisms, Lemma 37.44.3,
[Tag 0AH8](https://stacks.math.columbia.edu/tag/0AH8)) there is an
open neighbourhood $U_y\ni y$ such that $f(X\times_k\{y'\})$ is
finite for every $y'\in U_y$. The scheme $X\times_k\{y'\}$ is
connected, being the base change of the connected $k$-scheme $X$;
its image under $f$ is therefore connected, and it is contained in a
finite $k$-scheme, whose underlying topological space is finite and
hence totally disconnected. A connected subset of a totally
disconnected space is a single point, so $y'\in L$. Hence $L$ is
open.

*Step 3: $L=Y$.* By Steps 1 and 2 the subset $L\subseteq Y$ is
both open and closed and is nonempty, while $Y$ is connected; hence
$L=Y$. In other words $f$ is constant on every fibre of
$\operatorname{pr}_2:X\times_kY\to Y$.

*Step 4 (recorded classical input).* The passage from Step 3 to
the factorization $f=g\circ\operatorname{pr}_2$ is the recorded
classical input of the statement: Milne, *Abelian Varieties*,
Ch. I, the rigidity lemma, and Mumford, *Abelian Varieties*, II.6.
That reference also removes the hypothesis "$Z$ locally of finite
type", which Step 2 uses; in this chapter the lemma is applied only with
$X=Y=Z=A$ an abelian variety over $k$, so that $Z=A$ is of finite
type over $k$ and Steps 1–3 apply. No separate proof of the passage
is given here.
