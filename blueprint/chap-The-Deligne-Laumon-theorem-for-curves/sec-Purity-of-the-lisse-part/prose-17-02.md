+++
id = "prose-17-02"
kind = "hidden"
title = "Purity of the lisse part (1)"
order = 1275
+++
Throughout this subsection and the next, $j:U_0\hookrightarrow\mathbf A^1_{k_0}$
is a dense open and $M$ is a nonzero irreducible lisse Weil sheaf
on $U_0$, pure of weight $w$. We assume that no geometric irreducible
constituent of $M$ is the restriction of $\mathcal L_{\psi(ax)}$ for
some $a\in\bar k_0$, and we let $M'$ be the lisse Weil sheaf on a dense
open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$ with
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$
(Proposition [proposition-fourier-transform-middle-extension]).

We build the real sheaf from extensions by zero, because for them we
can check reality on the trace function. Indeed, at a point of $U_0$ the
eigenvalues of $M^0$ and of its dual have absolute value one, and hence
they are complex conjugate. At a boundary point, however, the
stalk of $j_*M^0$ is the space of inertia invariants, and the stalk of
$j_*(M^0)^\vee$ is the space of invariants of the dual representation,
but nothing we know at this stage makes their Frobenius eigenvalues
conjugate. With $j_!$, by contrast, both stalks vanish there, and the trace function
of the sum of the two transforms is clearly real.

The price is that $j_!M$ is not a simple perverse sheaf, so its
transform $G$ is not $j'_*M'$ but an extension of $j'_*M'$ by the
transform $B'$ of the boundary. This $B'$ is a lisse sheaf of weights at
most $w$ (Lemma [lemma-fourier-transform-boundary-sequence]), and in the
proof of Proposition [proposition-purity-lisse-part-fourier-transform]
we use only that $G$ is a sheaf and that it surjects onto $j'_*M'$.
