+++
kind = "proof"
of = "lemma-abelian-variety-commutative"
order = 1490
uses = ["lemma-uniqueness-maps-dense-open", "lemma-rigidity"]
+++
An abelian variety is geometrically reduced because it is smooth, and
geometrically irreducible because the identity component of a group
scheme over a field is geometrically irreducible [Stacks, [0B7R](https://stacks.math.columbia.edu/tag/0B7R)] and $A$
is connected.

For commutativity, consider $h:A\times A\to A$,
$h(x,y)=xyx^{-1}y^{-1}$. It maps $A\times\{e\}$ to $e$. By
Lemma [lemma-rigidity], applied with the first factor as the
proper one, there are an open $V\ni e$ and $g:V\to A$ with
$h|_{A\times V}=g\circ\operatorname{pr}_2$. Composing with
$(e,\operatorname{id}):V\to A\times V$ gives $g=h(e,-)=e$, so $h=e$ on
$A\times V$. To pass from $A\times V$ to $A\times A$, we compare $h$
with the constant map $e$. Since $A\times A$ is smooth, hence reduced, and
irreducible, the nonempty open $A\times V$ is scheme-theoretically
dense. Two maps to a separated scheme that agree on a
scheme-theoretically dense open agree everywhere
(Lemma [lemma-uniqueness-maps-dense-open]). Hence $h=e$
[Stacks, [056D](https://stacks.math.columbia.edu/tag/056D), [01RH](https://stacks.math.columbia.edu/tag/01RH)].
