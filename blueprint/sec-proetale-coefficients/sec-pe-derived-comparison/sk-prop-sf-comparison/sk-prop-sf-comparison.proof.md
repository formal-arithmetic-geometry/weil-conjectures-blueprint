+++
kind = "proof"
of = "sk-prop-sf-comparison"
uses = ["sk-lem-pe-injective-acyclicity", "sk-thm-pe-classical-sheaves"]
+++
Choose a bounded-below injective resolution $K\to I^\bullet$. Since
$\nu_X^*$ is exact, $\nu_X^*I^\bullet$ represents $\nu_X^*K$, and by
Lemma [sk-lem-pe-injective-acyclicity] its terms are $\nu_{X,*}$-acyclic,
so $R\nu_{X,*}\nu_X^*K$ is computed by the complex
$\nu_{X,*}\nu_X^*I^\bullet$. By Theorem [sk-thm-pe-classical-sheaves] the
unit $I^q\to\nu_{X,*}\nu_X^*I^q$ is an isomorphism for every $q$, so
this complex is $I^\bullet$, which proves (2.7).
Since $\Gamma(X_{\mathrm{pro}\acute{e}t},-)=\Gamma(X_{\acute{e}t},-)\circ\nu_{X,*}$, the statement on
global sections follows by composing the derived functors; see
[Stacks, Tag 099V](https://stacks.math.columbia.edu/tag/099V), [Stacks, Tag 099W](https://stacks.math.columbia.edu/tag/099W).
