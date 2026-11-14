+++
kind = "proof"
of = "proposition-ind-constructible-sheaves--3"
order = 453007
uses = ["definition-lisse-sheaves", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--3", "lemma-constructible-sheaves--3", "proposition-ind-constructible-sheaves--2"]
+++
*Canonical presentations.* The closure properties below involve
several ind-constructible sheaves at once. To compare their
presentations we use a presentation that involves no choices. For $B\in\IndCons(X,\Lambda)$, let $J(B)$ be
the category of constructible sheaves $C$ with a map $C\to B$. We show that
$B=\varinjlim_{J(B)}C$.

The category $J(B)$ is filtered. Two objects $C_1\to B$ and $C_2\to B$
both map to $C_1\oplus C_2\to B$. Two parallel arrows $C\rightrightarrows C'$
over $B$ are equalized by the cokernel of their difference, which is
constructible and still maps to $B$. Now write
$B=\varinjlim_\alpha C_\alpha$. By finite presentation, every
$C\to B$ factors through some $C_\alpha$, and two factorizations agree at
a later stage. This means that the given diagram is cofinal in $J(B)$, and
hence $B=\varinjlim_{J(B)}C$.

*Filtered colimits and direct sums.* Let $B=\varinjlim_\lambda B_\lambda$
be a filtered colimit with $B_\lambda\in\IndCons(X,\Lambda)$. Consider the category
of pairs $(\lambda,C\to B_\lambda)$ with $C$ constructible. It is filtered:
we move finitely many indices to a common upper bound, and then use direct
sums and cokernels in $J(B_\lambda)$. The colimit of the $C$ over this
category is $\varinjlim_\lambda\varinjlim_{J(B_\lambda)}C=B$. A direct sum is the
filtered colimit of its finite subsums, so it lies in $\IndCons(X,\Lambda)$
as well.

*Source:* the proof of Proposition [proposition-ind-constructible-sheaves].
