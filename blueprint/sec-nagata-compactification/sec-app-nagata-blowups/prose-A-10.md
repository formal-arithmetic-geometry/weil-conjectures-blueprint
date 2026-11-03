+++
id = "prose-A-10"
kind = "hidden"
title = "Blow-ups, strict transforms and elimination (6)"
order = 831
+++
This is [conrad07, Theorem 2.4], with the auxiliary base
equal to $T$; note that $Y$ is qcqs, since $p$ is separated and of
finite type and $T$ is qcqs. The hypothesis on $f$ says that
$f$ is a quasi-domination of $V$ over $Y$. When $V=U$ it holds
automatically, because a section of a separated morphism is a closed
immersion; this case is [conrad07, Remark 2.5], and later
sections apply the theorem only in this case.

We explain how the proof reduces to a quasi-affine $Y\to T$, since this
is where Zariski's Main Theorem enters. If $Y\to T$ is quasi-affine and
$T$ is affine, then $Y$ is a quasi-affine scheme of finite type over $T$
and embeds in some $\mathbf A^n_T$ [Stacks, Tag 04II](https://stacks.math.columbia.edu/tag/04II). The coordinates of
$f$ are then finitely many fractions, and a blow-up clearing their
denominators extends $f$; one first makes $U$ schematically dense, so
that the extended coordinates still satisfy the equations of $Y$. A
finite affine cover of $T$ gives the quasi-affine case over a qcqs
base. The proof needs this quasi-affine case for opens
$U\subseteq V$ with $U$ not necessarily dense, because the reduction
below applies it to the opens $f^{-1}(Y_i)\subseteq V$, which need not
be dense; a further construction in Conrad's proof keeps the centers
outside $V$.

For a general $Y$, choose a finite affine open cover
$Y=\bigcup_iY_i$. Since $T$ is quasi-separated, each $Y_i\to T$ is
quasi-compact, and as $Y_i$ is affine it is quasi-affine. Apply the
quasi-affine case to $f|_{f^{-1}(Y_i)}$ and take a common
$V$-admissible blow-up $T_1\to T$. The schematic closure $Z$ of the
image of $f$ in $Y\times_TT_1$ meets each $Y_i\times_TT_1$ inside the
closed graph of an extension, which has at most one point over each
point of $T_1$. Since there are finitely many $Y_i$, the fibres of
$Z\to T_1$ are finite; as $Z\to T_1$ is separated and of finite type,
it is quasi-finite. Hence it is quasi-affine by
Proposition [sk-prop-app-nagata-zmt], and the quasi-affine case extends
the section into $Z$. The composite of the two blow-ups is
$V$-admissible by Lemma [sk-lem-nagata-sketch-blowups].
