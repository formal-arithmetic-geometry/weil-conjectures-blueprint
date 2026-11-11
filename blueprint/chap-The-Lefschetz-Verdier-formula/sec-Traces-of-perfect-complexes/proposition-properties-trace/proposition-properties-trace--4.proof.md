+++
kind = "proof"
of = "proposition-properties-trace--4"
order = 896009
uses = ["proposition-properties-trace--2"]
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

*Source:* the proof of Proposition [proposition-properties-trace].
