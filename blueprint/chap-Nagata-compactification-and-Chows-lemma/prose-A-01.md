+++
id = "prose-A-01"
kind = "hidden"
title = "Nagata compactification and Chow's lemma"
order = 1393
+++
The main text defines cohomology with compact support as in topology:
to push forward along $f:X\to Y$, embed $X$ as an open subset of
something proper over $Y$, extend by zero and push forward, so that
$Rf_!=Rp_*j_!$ (Proposition [proposition-construction-independence-rf-shriek]).
This definition needs every morphism to have a compactification, and it
needs any two compactifications to be dominated by a third, so that
proper base change can show that $Rf_!$ does not depend on the choice.
The second point is elementary once we use compactifications in which
$X$ is scheme-theoretically dense: the closure of $X$ in the fibre
product of two of them dominates both
(Proposition [proposition-dense-compactifications-form-cofiltered-category]).
The first point is Nagata's theorem,
Theorem [theorem-nagata-s-compactification-theorem]: every separated
morphism of finite type $X\to S$ with $S$ quasi-compact and
quasi-separated factors as a quasi-compact open immersion $X\to\overline
X$ followed by a proper morphism $\overline X\to S$.

Why is this hard? Locally a compactification is easy to find: if $S$ and
$X$ are affine, we take the closure of $X$ in projective space over $S$.
The difficulty is to glue. Cover $X=\mathbf A^1_k$ by
$U_1=\mathbf A^1\setminus\{0\}$ and $U_2=\mathbf A^1\setminus\{1\}$,
compactify each by $\mathbf P^1$, and glue the two copies of $\mathbf
P^1$ along $U_1\cap U_2$. The result is $\mathbf P^1$ with the three
points $0$, $1$ and $\infty$ doubled, which is not separated. For curves
blow-ups are not needed. They would not help either, since blowing up a
point on a regular curve does nothing. In dimension at least two the
closures of $U_1\setminus U_2$ and $U_2\setminus U_1$ can meet in the
boundary. We pull them apart by blow-ups with centers in the boundary,
which leave $X$ unchanged (Lemma [lemma-separation-closures] and
Proposition [proposition-compactifying-union-two-opens]). Induction
over an affine cover then gives the theorem over a Noetherian base
(Section [sec-Proof-of-Nagatas-theorem]). Noetherian approximation gives the
general case, which we need because proper base change is proved over
arbitrary qcqs bases.

Proper base change itself is computed on projective space, and Chow's
lemma carries it to every proper morphism
(Section [sec-Proper-morphisms]). We use it in the form of
Theorem [theorem-chow-s-lemma-projective-form]: for a proper
morphism $X\to S$ there is a proper surjection $\widetilde X\to X$ with
$\widetilde X$ projective over $S$.
