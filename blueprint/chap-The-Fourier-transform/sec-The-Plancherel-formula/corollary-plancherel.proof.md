+++
kind = "proof"
of = "corollary-plancherel"
order = 1242
uses = ["lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "lemma-perfect-complexes-geometric-point", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary"]
+++
As for the classical transform, the proof is by orthogonality of
characters. We expand the square of the sum in (16.3),
using that the complex conjugate of a character value is its inverse.
This writes the left side as a double sum over $x,z\in\mathbf F_{q^n}^r$
of $\iota t_{K,n}(x)\overline{\iota t_{K,n}(z)}$ times a character sum
over $y$, which we now compute.
For $x,z\in\mathbf F_{q^n}^r$, the orthogonality of characters gives

$$
\sum_y\iota\psi\bigl(\operatorname{Tr}\langle x-z,y\rangle\bigr)
=\begin{cases}q^{nr},&x=z,\\0,&x\ne z.\end{cases}
$$

Indeed, for $x\ne z$ the linear form
$y\mapsto\operatorname{Tr}_{\mathbf F_{q^n}/k_0}\langle x-z,y\rangle$ is
nonzero, since the trace pairing is nondegenerate, and hence
surjective onto $k_0$. As $\psi$ is nontrivial, there is $y_0$ with
$c=\psi(\operatorname{Tr}\langle x-z,y_0\rangle)\ne1$, and
substituting $y+y_0$ for $y$ multiplies the sum by $\iota(c)$, so the sum is zero.
Therefore only the diagonal terms remain, and they
give the asserted identity. On a line, finally, the factor $q^n$ raises
$\nu$ by one.
