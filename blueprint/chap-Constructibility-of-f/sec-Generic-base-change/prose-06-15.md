+++
id = "prose-06-15"
kind = "hidden"
title = "Generic base change (1)"
order = 576
+++
Let $j:X\hookrightarrow Y$ be an open immersion of schemes over an
integral base $S$, and let $F$ be a constructible $\Fell$-sheaf on $X$.
For such data, Deligne's generic base change theorem says that over a dense open of $S$
the complex $Rj_*F$ is bounded constructible and its formation commutes
with base change. In particular, over a field it gives the finiteness of $Rj_*$ (Corollary [corollary-open-direct-image-over-field]), and this is all that the
computation of $f^!$ requires. On the other hand, the punctured plane over the $t$-line, discussed at the beginning of this section, shows that we cannot ask for
more than a dense open.

In characteristic $p$ the generic fibre need not contain a smooth dense
open. For example, let $X=\mathbf A^1_{\mathbf F_p}$ map to the $t$-line
by $x\mapsto x^p$. The generic fibre is
$\operatorname{Spec}\mathbf F_p(t^{1/p})$, which is not smooth over
$\mathbf F_p(t)$. For this reason Step 3 of the proof of
Theorem [theorem-generic-constructibility-base-change-rj] below allows a finite universal
homeomorphism of the base. Such a map changes neither the étale topoi
nor the conclusion.

We fix notation for base change. With $j$ as above and a morphism $T\to S$, we write
$j_T:X_T\hookrightarrow Y_T$ for the base change and
$g_X:X_T\to X$, $g_Y:Y_T\to Y$ for the projections. The base change map $g_Y^*Rj_*K\to Rj_{T,*}g_X^*K$ is then the map (4.5).

The proof of Theorem [theorem-generic-constructibility-base-change-rj]
is an induction on the dimension of the generic fibre, in three steps. The next three lemmas are the parts of this proof that do not use the
induction hypothesis, and each serves one step.
First, Lemma [lemma-extension-across-finite-subset] is Step 2: if $X$ is smooth and $F$ locally constant, it extends the conclusion from an open
$G$ with complement finite over $S$, provided by Step 1, across that complement.
Next, Lemma [lemma-universal-homeomorphism-base] allows Step 3 to replace
$S$ by a finite universal homeomorphism, as the example above requires.
Lemma [lemma-generic-smooth-open] then provides, after this
replacement, the dense open $V$ of Step 3, smooth with $F$ locally
constant, whose complement has a smaller generic fibre.
