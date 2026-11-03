+++
id = "prose-A-01"
kind = "hidden"
title = "Nagata compactification and Chow's lemma"
order = 807
+++
For a map $f:X\to Y$ of locally compact spaces, the direct image with
compact support is built from a compactification: one embeds $X$ as an
open subset of a space proper over $Y$, extends by zero and pushes
forward. In algebraic geometry the same construction defines
$Rf_!=Rp_*j_!$ (Proposition [sk-prop-sf-comp-coherence]), and it
needs two things. Every morphism must have a compactification, and any
two must be dominated by a third, so that proper base change can show
that $Rf_!$ does not depend on the choice. The first is Nagata's theorem
(Theorem [sk-thm-nagata-compactification]): every separated morphism of finite
type $X\to S$ with $S$ quasi-compact and quasi-separated factors as a
quasi-compact open immersion $X\to\overline X$ followed by a proper
morphism $\overline X\to S$. The second is elementary: we take the
closure of $X$ in the fibre product of two compactifications, provided we
work with compactifications in which $X$ is scheme-theoretically dense
(Proposition [sk-prop-nagata-sketch-comp-category]). The proof of proper base change
uses a different theorem, Chow's lemma: for a proper morphism $X\to S$
there is a proper surjection $\widetilde X\to X$ with $\widetilde X$
projective over $S$ (Theorem [sk-thm-chow-projective]). This lets us
descend proper base change from projective space, where it is computed,
to every proper morphism (Section [sec-pbc-reduction]).

Locally a compactification is easy to find: if $S$ and $X$ are affine,
we take the closure of $X$ in projective space over $S$. The difficulty
is to glue. The difficulty is that compactifications of two opens of $X$ glue to a
scheme that need not be separated, let alone proper. For instance, cover
$X=\mathbf A^1_k$ by $U_1=\mathbf A^1\setminus\{0\}$ and
$U_2=\mathbf A^1\setminus\{1\}$, compactify each by $\mathbf P^1$, and
glue the two copies of $\mathbf P^1$ along $U_1\cap U_2$; the result is
$\mathbf P^1$ with the three points $0$, $1$ and $\infty$ doubled. This
shows why naive gluing destroys separatedness. Blow-ups do not help for
curves, since blowing up a point on a regular curve does nothing, and
they are not needed there. In dimension at least two the
closures of $U_1\setminus U_2$ and $U_2\setminus U_1$ can meet in the
boundary, and there we modify the compactifications by blow-ups whose
centers lie in the boundary, so that $X$ itself is not changed. A
blow-up of this kind can make the closures of two disjoint closed subsets disjoint
(Lemma [sk-lem-nagata-sketch-boundary]), and in this way the two boundaries
are pulled apart before gluing (Proposition [sk-thm-nagata-sketch-two-open]).
Induction over an affine cover proves the theorem over a Noetherian base,
and Noetherian approximation gives the general case
(Section [sec-app-nagata-global-proof]). The general case is needed, because
proper base change is proved over arbitrary qcqs bases.

Nagata proved the theorem for Noetherian schemes in two papers of 1962
and 1963, in the language of his time. The scheme-theoretic proof by blow-ups that we
follow is due to Deligne and was written up by Conrad [conrad07];
the Stacks Project gives the same argument. Besides elementary facts on
blow-ups and Noetherian approximation, we quote Deligne's theorem that a
partial section extends after a blow-up
[conrad07, Theorem 2.4], and we deduce the projective form of
Chow's lemma from the version in [Stacks, Tag 0202](https://stacks.math.columbia.edu/tag/0202). The only result from the
main text that we use is Proposition [sk-prop-sf-open-closed-triangle], in the proof
of Lemma [sk-lem-nagata-density-normalization].
