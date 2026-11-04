+++
id = "prose-A-16"
kind = "hidden"
title = "Elimination of indeterminacy (8)"
order = 1433
+++
We quote this theorem from [conrad07, Theorem 2.4], with the
auxiliary base equal to $T$, and explain below the structure of its
proof. Note that $Y$ is qcqs, since $p$ is separated and of
finite type and $T$ is qcqs. The hypothesis on $f$ says that
$f$ is a quasi-domination of $V$ over $Y$. We apply the theorem only
when $V=U$, the case of [conrad07, Remark 2.5]. Then the
hypothesis holds automatically, because a section of a separated
morphism is a closed immersion.

The proof first treats a quasi-affine $Y\to T$. If $Y\to T$ is
quasi-affine and $T$ is affine, then $Y$ is a quasi-affine scheme of
finite type over $T$, and it embeds in some $\mathbf A^n_T$
[Stacks, [04II](https://stacks.math.columbia.edu/tag/04II)]. The coordinates of $f$ are then finitely many fractions,
and a blow-up clearing their denominators extends $f$. One first makes
$U$ schematically dense, so that the extended coordinates still satisfy
the equations of $Y$. A finite affine cover of $T$ gives the
quasi-affine case over a qcqs base. The proof needs this case for opens
$U\subseteq V$ with $U$ not necessarily dense, because the reduction
below applies it to the opens $f^{-1}(Y_i)\subseteq V$, which need not be dense. A further
construction in Conrad's proof keeps the centers outside $V$.

The general case reduces to the quasi-affine one, and this reduction is
where Zariski's Main Theorem enters. The plan is to extend the section
on each affine open of $Y$ separately. The closure of the section is
then quasi-finite over the base, hence quasi-affine, and the
quasi-affine case applies once more.

In detail, choose a finite affine open cover $Y=\bigcup_iY_i$. Since $T$
is quasi-separated, each $Y_i\to T$ is quasi-compact, and as $Y_i$ is
affine it is quasi-affine. The quasi-affine case applies to each
$f|_{f^{-1}(Y_i)}$, and we take a common $V$-admissible blow-up
$T_1\to T$. Let $Z$ be the schematic closure of the image of $f$ in
$Y\times_TT_1$. It meets each $Y_i\times_TT_1$ inside the closed graph
of an extension, which has at most one point over each point of $T_1$.
Since there are finitely many $Y_i$, the fibres of $Z\to T_1$ are
finite. As $Z\to T_1$ is separated and of finite type, it is
quasi-finite, and it is quasi-affine by
Proposition [proposition-relative-form-zariski-s-main]. The
quasi-affine case then extends the section into $Z$. The composite of the two blow-ups is
$V$-admissible by Lemma [lemma-products-composites-u-admissible-blow].
