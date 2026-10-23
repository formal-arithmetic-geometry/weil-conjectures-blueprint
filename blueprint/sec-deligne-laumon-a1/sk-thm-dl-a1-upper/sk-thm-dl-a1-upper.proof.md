+++
kind  = "proof"
of    = "sk-thm-dl-a1-upper"
+++
[sk-l-dl-a1-endpoints] settles every degree except degree
one. Take a finite composition series of the finite-dimensional
Weil representation of $F$. Each irreducible lisse factor is
pure of weight $w$, since its local eigenvalues are eigenvalues of a
subquotient, and it is again unramified at infinity.
An irreducible factor that is geometrically constant is a constant
Weil line, because the geometric action is trivial and an invertible
linear operator over $\Qlb$ has an eigenline. Its middle extension is
constant on the affine line, and its $H_c^1$ vanishes by
[sk-lem-wft-character-integral] in the trivial case.
Every other factor is Fourier-generic by [sk-p-dl-a1-middle], and so
[sk-c-dl-a1-hc1] applies to it.
By [sk-p-dl-a1-exact], the short exact sequences of
the composition series remain exact after applying $j_*$. In the
resulting long exact sequences of compact-support cohomology, each
group in degree one is an extension of a quotient of the preceding
group by a subobject of the group of the factor. Since the bound $w+1$
is preserved under subquotients and extensions
([sk-p-linear-filtration]), induction proves it for $F$.
