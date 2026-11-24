+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison"
order = 124
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "lemma-acyclic-resolutions"]
+++
We compute [$R\nu_{X,*}\nu_X^*K$](@proposition-comparison-morphism-inverse-image) with an injective resolution of $K$ on
the étale site. By the lemma its pullback is still acyclic for
[$\nu_{X,*}$](@proposition-comparison-morphism-inverse-image), and by full faithfulness on sheaves the result is
the resolution itself.

Choose a bounded-below injective resolution $K\to I^\bullet$. Since
[$\nu_X^*$](@proposition-comparison-morphism-inverse-image) is exact, [$\nu_X^*I^\bullet$](@proposition-comparison-morphism-inverse-image) represents [$\nu_X^*K$](@proposition-comparison-morphism-inverse-image), and by
Lemma [lemma-acyclicity-pulled-back-injectives] its terms are [$\nu_{X,*}$](@proposition-comparison-morphism-inverse-image)-acyclic,
so [$R\nu_{X,*}\nu_X^*K$](@proposition-comparison-morphism-inverse-image) is computed by the complex
[$\nu_{X,*}\nu_X^*I^\bullet$](@proposition-comparison-morphism-inverse-image). By Theorem [theorem-classical-sheaves-essential-image] the
unit $I^q\to\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*I^q}$ is an isomorphism for every $q$, so
this complex is $I^\bullet$, which proves (2.7).
Since $\Gamma(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},-)=\Gamma(X_{\acute{e}t},-)\circ\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}}$, the statement on
global sections follows by composing the derived functors; see
[Stacks, [099V](https://stacks.math.columbia.edu/tag/099V), [099W](https://stacks.math.columbia.edu/tag/099W)].
