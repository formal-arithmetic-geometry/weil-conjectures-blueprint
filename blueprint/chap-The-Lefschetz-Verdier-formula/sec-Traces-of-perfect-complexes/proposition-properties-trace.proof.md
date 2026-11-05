+++
kind = "proof"
of = "proposition-properties-trace"
order = 896
+++
Everything follows from the chain formula, which we prove first by
writing evaluation and coevaluation in a finite dual basis.
If $e_1,\dots,e_n$ and $e^1,\dots,e^n$ are dual
bases of $A^n$ and its dual, then $\operatorname{coev}(1)=\sum_je_j\otimes e^j$,
and the composite of the definition sends $1$ to
$\sum_je^j(v(e_j))$, the ordinary trace of a matrix. The same computation
applies to a finite projective module, which is a direct summand of such an $A^n$.
On a complex, the symmetry interchanging a term
of degree $i$ and its dual of degree $-i$ contributes $(-1)^i$, which
proves the chain formula. Its right-hand side is invariant under chain
homotopy, since the supertrace of $dh+hd$ is zero by cyclicity and a shift of
index.

Tensoring a dual basis with $B$ preserves evaluation and coevaluation. Hence
the trace is compatible with extension of scalars for every ring map
$A\to B$. Linearity and invariance under conjugacy follow from the same description. For additivity, note that a two-step filtered object of the filtered derived category may be
represented by a filtered complex of projective modules whose filtration is
split in each degree. The endomorphism is then block triangular, so its
supertrace is the sum of the supertraces on the two graded pieces. Finally, over a field the boundaries
$B^i$ and cycles $Z^i$ are $v$-invariant subspaces
$B^i\subset Z^i\subset P^i$, with $Z^i/B^i=H^i(P)$, and the
differential induces a $v$-equivariant isomorphism $P^i/Z^i\simeq B^{i+1}$.
Hence

$$
\operatorname{Tr}(v^i\mid P^i)=\operatorname{Tr}(v\mid B^i)
+\operatorname{Tr}(H^i(v)\mid H^i(P))+\operatorname{Tr}(v\mid B^{i+1}),
$$

and in the alternating sum the terms for the $B^i$ cancel in pairs,
leaving the cohomological formula.
