+++
id = "thm-wf-real-mixed-curve"
kind = "theorem"
title = "An $\\iota$-real constructible sheaf on a curve is $\\iota$-mixed; the curve case of Kiehl–Weissauer 1.4.3(1)"
order = 4187
uses = ["def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "def-wf-iota-real", "def-wf-middle-extension", "fin2-lem-lisse-dense-open", "thm-rp-real-lisse-purity-affine"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, and let $\mathcal H$ be a
constructible Weil sheaf on
$X_0$ which is $\iota$-real. Then
$\mathcal H$ is $\iota$-mixed
in the sense of [def-weil-punctual-weights].

## Proof

Step 1 (a lisse locus). By [fin2-lem-lisse-dense-open] there is a
dense open immersion $j:U_0\hookrightarrow X_0$ whose complement
$S_0$ satisfies $\dim S_0<\dim X_0=1$, i.e. is finite, and on which
the restriction $\mathcal H|_{U_0}$ is lisse. Reality is a pointwise
condition on the local characteristic factors
([def-wf-iota-real]), so the restriction of an $\iota$-real sheaf
is $\iota$-real, and $\mathcal H|_{U_0}$ is an $\iota$-real lisse
sheaf on the smooth geometrically connected affine curve $U_0$.

Step 2 (the open part is mixed). By
[thm-rp-real-lisse-purity-affine] every irreducible constituent
$\mathcal W$ of $\mathcal H|_{U_0}$ is punctually $\iota$-pure of
its determinant weight. The constituents form a finite composition
series of the lisse sheaf $\mathcal H|_{U_0}$ whose successive
quotients are punctually $\iota$-pure, which is exactly the mixedness
of [def-weil-punctual-weights]; hence $\mathcal H|_{U_0}$ is
$\iota$-mixed.

Step 3 (the punctual part is mixed). The complement $S_0$ is finite, so
the restriction $\mathcal H|_{S_0}$ is the finite direct sum of its
stalks, and at each closed point $s\in S_0$ the local Frobenius has a
conjugation-stable spectrum, by reality of $\mathcal H$ at $s$. The
generalised eigenspaces of that Frobenius are stable under it and carry
a single eigenvalue each; they therefore filter the stalk by subquotients
that are punctually $\iota$-pure of the single weight determined by
that eigenvalue. Hence $\mathcal H|_{S_0}$, as a sheaf on the
zero-dimensional scheme $S_0$, is $\iota$-mixed.

Step 4 (extension). In the middle-extension formalism of
[def-wf-middle-extension] there is, for the closed immersion
$i:S_0\hookrightarrow X_0$, an exact sequence of sheaves on $X_0$

$$
0\longrightarrow j_!(\mathcal H|_{U_0})\longrightarrow\mathcal H
\longrightarrow i_*(\mathcal H|_{S_0})\longrightarrow0 .
$$

The functor $j_!$ is exact, preserves the stalks over $U_0$ and kills
those over $S_0$; applied to a filtration of $\mathcal H|_{U_0}$ with
punctually pure quotients it therefore exhibits
$j_!(\mathcal H|_{U_0})$ as $\iota$-mixed, the extension by zero of a
punctually $\iota$-pure sheaf being punctually $\iota$-pure of the
same weight (its stalks are the original ones or zero). A filtration of
$\mathcal H|_{S_0}$ with punctually pure quotients pulls back along
$i$ to one of $i_*(\mathcal H|_{S_0})$. Mixedness is closed under
extensions: the preimages in $\mathcal H$ of the members of a
filtration of the quotient, prolonged by the members of a filtration of
the subobject, form a filtration of $\mathcal H$ whose successive
quotients are punctually $\iota$-pure, in the sense of
[def-weil-punctual-weights]. Hence $\mathcal H$ is
$\iota$-mixed.
