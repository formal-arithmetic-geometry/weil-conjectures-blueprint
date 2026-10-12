+++
kind  = "proof"
of    = "lem-embedding-extension"
+++
First extend $\sigma:L\hookrightarrow\mathbf C$ to an isomorphism
between the algebraic closure of $L$ inside $\Qlb$ and the
algebraic closure of $\sigma(L)$ inside $\mathbf C$.
Both are countable algebraically closed fields. Choose
transcendence bases $B_\ell$ and $B_{\mathbf C}$ over these
respective fields. Each basis has cardinality $2^{\aleph_0}$:
an algebraic extension of the rational function field in a basis
$B$ over a countable field has cardinality
$\max(\aleph_0,|B|)$, whereas both ambient fields have
cardinality $2^{\aleph_0}$.
A bijection $B_\ell\to B_{\mathbf C}$, together with the chosen
isomorphism on the algebraic closures of $L$, defines an
isomorphism of the corresponding rational function fields.
Extending it to their algebraic closures gives an isomorphism
$\iota:\Qlb\to\mathbf C$ restricting to $\sigma$.
The algebraic-closure convention is
[def-weil-algebraic-closure-q].

For an embedding $\tau:\mathbf Q(\alpha)\hookrightarrow\mathbf C$, the
composite $\sigma_\tau:=\tau\circ(\jmath|_{\mathbf Q(\alpha)})^{-1}$
embeds the number field $\jmath(\mathbf Q(\alpha))\subset\Qlb$ into
$\mathbf C$; extending it as above gives an abstract field
isomorphism $\iota_\tau:\Qlb\xrightarrow{\sim}\mathbf C$ with
$\iota_\tau(\jmath(\alpha))=\tau(\alpha)$, so the hypothesis applied
to this $\iota_\tau$ gives $|\tau(\alpha)|=q^{i/2}$.

For the Galois stability, let $\gamma\in\operatorname{Gal} (\overline{\mathbf Q}/\mathbf Q)$ and let
$\tau':\mathbf Q(\gamma(\alpha))\hookrightarrow\mathbf C$. Then
$\tau'\circ\gamma:\mathbf Q(\alpha)\hookrightarrow\mathbf C$ is an
embedding, so by the preceding paragraph
$|\tau'(\gamma(\alpha))|=|(\tau'\circ\gamma)(\alpha)|=q^{i/2}$.
Hence $\gamma(\alpha)$ satisfies the $q$-Weil condition of weight
$i$ of [def-weil-numbers], which proves the stability
assertion.
