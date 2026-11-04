+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison"
order = 124
uses = ["theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives"]
+++
We compute $R\nu_{X,*}\nu_X^*K$ with an injective resolution of $K$ on
the étale site. By the lemma its pullback is still acyclic for
$\nu_{X,*}$, and by full faithfulness on sheaves the result is
the resolution itself.

Choose a bounded-below injective resolution $K\to I^\bullet$. Since
$\nu_X^*$ is exact, $\nu_X^*I^\bullet$ represents $\nu_X^*K$, and by
Lemma [lemma-acyclicity-pulled-back-injectives] its terms are $\nu_{X,*}$-acyclic,
so $R\nu_{X,*}\nu_X^*K$ is computed by the complex
$\nu_{X,*}\nu_X^*I^\bullet$. By Theorem [theorem-classical-sheaves-essential-image] the
unit $I^q\to\nu_{X,*}\nu_X^*I^q$ is an isomorphism for every $q$, so
this complex is $I^\bullet$, which proves (2.7).
Since $\Gamma(X_{\mathrm{pro}\acute{e}t},-)=\Gamma(X_{\acute{e}t},-)\circ\nu_{X,*}$, the statement on
global sections follows by composing the derived functors; see
[Stacks, [099V](https://stacks.math.columbia.edu/tag/099V), [099W](https://stacks.math.columbia.edu/tag/099W)].
