+++
kind = "proof"
of = "sk-thm-nagata-compactification"
uses = ["sk-lem-nagata-sketch-affine-cover", "sk-thm-nagata-sketch-two-open", "thm-nagata-noetherian", "prop-nagata-noetherian-inverse-system", "lemma-nagata-separated-eventually", "lemma-nagata-finite-type-fp-model-system", "lemma-nagata-final-basechanged-compactification", "prop-nagata-finite-type-closed-in-fp", "sk-lem-nagata-sketch-closure"]
+++
If $S$ is Noetherian, we choose a cover as in
Lemma [sk-lem-nagata-sketch-affine-cover] and argue by induction on the
unions $U_1\cup\cdots\cup U_r$.
At each step, the overlap with $U_{r+1}$ contains the dense total
intersection, and Proposition [sk-thm-nagata-sketch-two-open] yields a
compactification of the next union. The last union is $X$ itself.

Now let $S$ be a general qcqs scheme, and suppose first that $X\to S$
is separated and of finite presentation. By absolute Noetherian
approximation we can write

$$
S=\varprojlim_i S_i
$$

with $S_i$ Noetherian and affine transition maps [Stacks, Tag 01ZA](https://stacks.math.columbia.edu/tag/01ZA).
Since $X\to S$ is of finite presentation, it descends to a model
$X_i\to S_i$ for some $i$, and after increasing $i$ the model is
separated [Stacks, Tag 01ZM](https://stacks.math.columbia.edu/tag/01ZM), [Stacks, Tag 01ZQ](https://stacks.math.columbia.edu/tag/01ZQ). We compactify this model by
the Noetherian case and base change the compactification to $S$. Open
immersions and proper morphisms are stable under base change, and taking
the schematic closure of $X$ makes the result dense.

Finally, let $X\to S$ be separated of finite type. By [Stacks, Tag 01ZJ](https://stacks.math.columbia.edu/tag/01ZJ),
there is a closed immersion $X\hookrightarrow X_0$ with $X_0\to S$
separated of finite presentation. We compactify $X_0$ by the case
already proved, and take the schematic closure of $X$ in that
compactification. Restricted to the open $X_0$, this closure is
exactly the closed subscheme $X$. Thus $X$ is open and schematically
dense in the closure, which is proper over $S$.
