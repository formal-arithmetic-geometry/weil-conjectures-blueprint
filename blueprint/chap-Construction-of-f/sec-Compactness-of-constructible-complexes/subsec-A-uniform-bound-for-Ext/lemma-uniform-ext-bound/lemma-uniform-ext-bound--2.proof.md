+++
kind = "proof"
of = "lemma-uniform-ext-bound--2"
order = 446005
+++
Clause [lemma-uniform-ext-bound--1] establishes the bound over every finite extension,
uniformly in that extension. *The case $\Lambda=\overline{\mathbf Q}_\ell$.* The bound for
$E$ depends only on the strata and on $\operatorname{cd}_\ell$, not on $E$,
so it passes to the colimit over finite extensions. We first fix everything
that depends on $L$ alone, before the target is given. By
Lemma [lemma-descent-lisse-qbar-sheaves-finite], applied to $L$ alone,
there are a finite extension $E_0/\mathbf Q_\ell$ and a lisse $E_0$-sheaf $L'$ with
$L=L'_{\overline{\mathbf Q}_\ell}$. After refining $S$
(Lemma [lemma-lattices-after-finite-stratification]), $L'$ contains a
lisse $\mathcal O_{E_0}$-lattice $L'_0$; the refinement depends only on $L$.
For every finite extension $E'\supset E_0$, the sheaf
$L'_0\otimes_{\mathcal O_{E_0}}\mathcal O_{E'}$ is a lisse
$\mathcal O_{E'}$-lattice in $(L')_{E'}$ on the same strata, so
clause [lemma-uniform-ext-bound--1] gives $\Ext^q_{E'}\bigl((a_!L')_{E'},N'\bigr)=0$ for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$, for each refined
stratum $S$ and every $N'\in\Cons(X,E')$. This bound depends neither on
$E'$ nor on $N'$.

Now let $b$ and $M$ be given. By
Lemma [lemma-descent-lisse-qbar-sheaves-finite], applied to $M$, there
are a finite extension $E\supset E_0$ and a lisse $E$-sheaf $M'$ with
$M=M'_{\overline{\mathbf Q}_\ell}$. The field $E$ depends on $M$, but neither the strata of the
source nor the lattice $L'_0$ do. Then $a_!L=(a_!L')_{\overline{\mathbf Q}_\ell}$ and
$b_!M=(b_!M')_{\overline{\mathbf Q}_\ell}$, and by
Lemma [lemma-descent-finite-coefficient-field](1),

$$
\Ext^q_{\overline{\mathbf Q}_\ell}(a_!L,b_!M)
=\varinjlim_{E'\supset E}\Ext^q_{E'}\bigl((a_!L')_{E'},(b_!M')_{E'}\bigr).
$$

Every group on the right vanishes for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ by the previous
paragraph, and hence so does the colimit.

*Source:* the proof of Lemma [lemma-uniform-ext-bound].
