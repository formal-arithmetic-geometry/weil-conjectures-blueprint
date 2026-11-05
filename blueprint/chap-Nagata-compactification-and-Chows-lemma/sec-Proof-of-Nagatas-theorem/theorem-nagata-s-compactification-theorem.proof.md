+++
kind = "proof"
of = "theorem-nagata-s-compactification-theorem"
order = 1465
uses = ["lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
If $S$ is Noetherian, we choose a cover as in
Lemma [lemma-affine-covers-dense-intersection] and argue by induction on the
unions $X_r=U_1\cup\cdots\cup U_r$. For $r=1$, the lemma gives a
compactification of $U_1$. If $X_r$ has a compactification, we apply
Proposition [proposition-compactifying-union-two-opens] to
$M=X_{r+1}$, with $M_1=X_r$ and $M_2=U_{r+1}$. Each piece has a
compactification, by induction and by the lemma. The overlap
$X_r\cap U_{r+1}$ is dense in $X_{r+1}$, since it contains the total
intersection, which contains all generic points of $X$. Hence $X_{r+1}$
has a compactification. The last union is $X$ itself, and taking the
schematic closure of $X$ makes the compactification dense.

Now let $S$ be a general qcqs scheme, and suppose first that $X\to S$
is separated and of finite presentation. By absolute Noetherian
approximation we can write

$$
S=\varprojlim_i S_i
$$

with $S_i$ Noetherian and affine transition maps [Stacks, [01ZA](https://stacks.math.columbia.edu/tag/01ZA)].
Since $X\to S$ is of finite presentation, it descends to a model
$X_i\to S_i$ for some $i$, and after increasing $i$ the model is
separated [Stacks, [01ZM](https://stacks.math.columbia.edu/tag/01ZM), [01ZQ](https://stacks.math.columbia.edu/tag/01ZQ)]. We then compactify this model by the Noetherian case and base change the compactification to $S$. The result is a compactification, because open immersions and proper morphisms are stable under base change, and taking
the schematic closure of $X$ makes the result dense.

Finally, let $X\to S$ be separated of finite type. By [Stacks, [01ZJ](https://stacks.math.columbia.edu/tag/01ZJ)],
there is a closed immersion $X\hookrightarrow X_0$ with $X_0\to S$
separated of finite presentation. We compactify $X_0$ by the case
already proved, and take the schematic closure of $X$ in that
compactification. This closure is proper over $S$. Its restriction to
the open $X_0$ is the closed subscheme $X$ itself, so $X$ is open in
the closure, and it is schematically dense there by
Lemma [lemma-schematic-closure-uniqueness].
